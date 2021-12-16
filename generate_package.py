from bs4 import BeautifulSoup
import os
import re
import pandas
from termcolor import colored
import requests

def rewrite_break(file):
    infile = open(file).readlines()

    with open(file, 'w') as f:
        for line in infile:
            if 'class break():' in line:
                f.write(line.replace('class break():', 'class Break()'))
            if '.break' in line:
                f.write(line.replace('.break', '.Break'))
            else:
                f.write(line)
        f.close()


def render_template(template, **kwargs):
    t = open(f'templates/{template}').read()
    for arg in kwargs:
        t = t.replace('{{ %s }}' % arg, kwargs[arg] )
    return t

def get_tag_text(tag, html):
    soup = BeautifulSoup(html, 'html.parser')
    t = soup.find(tag)
    return t.text


def split_html(tag, html):
    sep = f'<{tag}'
    remove_from_first = False if html.startswith(sep) else True
    s = list(map(lambda x: sep + x, html.split(sep)))

    if remove_from_first:
        s[0] = s[0][len(sep):]

    return s


class API_Documentation():
    def __init__(self):
        self.base_dir = os.getcwd() + '/zapy'
        print('Fetching documentation ...')
        self.source = requests.get('https://www.zaproxy.org/docs/api/').text

    def split_source_by_obj(self):
        s = [x for x in split_html('h1', self.source) if '<code>' in x and '<table>' in x][1:]
        return s

    def split_obj_by_methods(self, obj):
        methods = []
        for method in split_html('h2', obj):
            try:
                method_name = get_tag_text('h2', method) # THIS IS NEEDED TO FILTER ERRORS
                methods.append(method)
            except:
                pass
        return methods

    def parse_parameters(self, html_table):
        try:
            return [x for x in pandas.read_html(html_table)[0]['Name'].values]
        except:
            return None

    def stringify_method(self, method):
        name = get_tag_text('h2', method)
        api_url = re.search('<code>(.+)</code>', method)[1].replace('GET ', '')
        parameters_table = re.search('<table>.+</table>', method.replace('\n', ''))[0]
        parameters = self.parse_parameters(parameters_table)

        if parameters:
            parameters_string = ',\n'.join(f'"{parameter}": kwargs.get("{parameter}")' for parameter in parameters)
            return render_template('method.py', METHOD_NAME=name, API_PATH=api_url, PARAMETERS_LIST=parameters_string)

        else:
            return render_template('method_without_param.py', METHOD_NAME=name, API_PATH=api_url)

    def stringify_obj(self, obj):
        string_object = ''
        obj_name = get_tag_text('h1', obj)
        _class = render_template('class.py', CLASS_NAME=obj_name)

        string_object += _class
        for method in self.split_obj_by_methods(obj):
            _method = self.stringify_method(method)

            string_object += '\n' + _method

        return string_object


    def dump(self):
        print('Creating package ...')
        if 'zapy' in os.listdir():
            os.system('rm -rf zapy')
        os.mkdir('zapy')

        # Create API object

        objects = []


        for obj in self.split_source_by_obj():
            try:
                obj_name = get_tag_text('h1', obj)
                objects.append(obj_name)
                print(f'Parsing {colored(obj_name, "cyan")} object ...')
                open(f'{self.base_dir}/{obj_name}.py', 'w').write(self.stringify_obj(obj))
            except KeyboardInterrupt:
                exit()
            except:pass

        print(f'Creating {colored("API class", "green")} ...')
        API_class_string = render_template('api_class.py',
                                           IMPORTS_LIST='\n'.join(list(map(lambda x: f'zapy.{x}', objects))),
                                           API_CLASSES='\n\t'.join(list(map(lambda x: f'self.{x} = zapy.{x}', objects))))
        open(f'{self.base_dir}/API.py', 'w').write(API_class_string)

        open(f'{self.base_dir}/__init__.py', 'w').write(render_template('__init__.py'))


        print('Finalizing ...')
        os.system(f'reindent -n {self.base_dir}/API.py')
        os.system(f"sed s/'class break():'/'class Break():'/ -i {self.base_dir}/break.py")
        os.system(f"sed s/'.break'/'.Break'/g -i {self.base_dir}/API.py")
        os.system(f'mv {self.base_dir}/break.py {self.base_dir}/Break.py')
        os.system(f"sed s/'def coreOtherProxy.pac'/'def coreOtherProxyPac'/ -i {self.base_dir}/core.py")

        print()
        print(f'Package saved at {self.base_dir}')




if __name__ == '__main__':
    doc = API_Documentation()
    doc.dump()









