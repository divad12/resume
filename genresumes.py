#!/usr/bin/python

from Cheetah.Template import Template
import sys
import tex
import yaml

# TODO: As much as i love functional, do this shorter
def escape_latex_all(o):
    if isinstance(o, list):
        return map(escape_latex_all, o)
    elif isinstance(o, dict):
        return dict(map(lambda x: (x[0], escape_latex_all(x[1])), o.items()))
    else:
        return tex.escape_latex(str(o)).replace('LaTeX', r'\LaTeX').replace('\\textbackslash{}', '\\').replace('\\{', '{').replace('\\}', '}') # TODO: OMG HACK HACK HACK maybe try yaml custom data types

contents = yaml.load(open(sys.argv[2], 'r').read())
escaped = escape_latex_all(contents)
template = Template(file=sys.argv[1], searchList=[escaped])
open(sys.argv[3], 'w').write(str(template))

