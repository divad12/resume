#!/usr/bin/python

# Glue between the yaml source and the Cheetah templating engine to produce
# LaTeX input for pdflatex (HTML soon to come)

from Cheetah.Template import Template
import sys
import tex
import yaml

# TODO: there's gotta be a better way of doing this...
def escape_latex_all(o):
    if isinstance(o, list):
        return map(escape_latex_all, o)
    elif isinstance(o, dict):
        return dict(map(lambda x: (x[0], escape_latex_all(x[1])), o.items()))
    else:
        # TODO: HACK HACK HACK. Use Cheetah custom types.
        return tex.escape_latex(str(o)).replace('LaTeX', r'\LaTeX').replace('\\textbackslash{}', '\\').replace('\\{', '{').replace('\\}', '}')

contents = yaml.load(open(sys.argv[2], 'r').read())
escaped = escape_latex_all(contents)
template = Template(file=sys.argv[1], searchList=[escaped])
open(sys.argv[3], 'w').write(str(template))

