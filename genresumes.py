#!/usr/bin/env python

"""
Takes yaml resume input source, escapes it, and feeds it to the Cheetah
templating engine
"""

from Cheetah.Template import Template
from datetime import datetime
from optparse import OptionParser
import escapes
import functools
import os
import sys
import yaml


def escape_leaves(escape_func, contents):
    """Escapes all leaves in the contents dict with escape_func"""
    if isinstance(contents, list):
        return map(functools.partial(escape_leaves, escape_func), contents)
    elif isinstance(contents, dict):
        return dict(map(lambda x: (x[0], escape_leaves(escape_func, x[1])),
            contents.items()))
    else:
        return escape_func(str(contents))

def get_cmd_line_args():
    parser = OptionParser(usage="%prog [options] <extension>",
        description="Fills in Cheetah templates from YAML source to " +
                    "generate resume of the given <extension> format.")

    parser.add_option("-o", "--output_dir",
        default='output',
        help="Output directory of generated files. Defaults to output/")

    parser.add_option("-s", "--source",
        default='resume.yaml',
        help="Filename of the resume YAML source. Defaults to resume.yaml")

    parser.add_option("-t", "--template",
        default='templates/resume.%s.tmpl',
        help="Filename of the output format template. Defaults to templates/resume.<extension>.tmpl")

    options, extra_args = parser.parse_args()
    if len(extra_args) < 1:
        parser.print_help()
        exit()

    return options, extra_args[0]

if __name__ == '__main__':
    options, extension = get_cmd_line_args()

    contents = yaml.load(open(options.source, 'r').read())

    escape_func = getattr(escapes, 'escape_' + extension, lambda x: x)
    escaped_contents = escape_leaves(escape_func, contents)
    template = Template(file=options.template % extension,
            searchList=[escaped_contents])

    output_dir = options.output_dir
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    open('%s/resume.%s' % (output_dir, extension), 'w').write(str(template))

