import tex
import re

HYPERLINK_REGEX = re.compile(r'\[([^\]]*)\]\(([^)]*)\)')

def escape_tex(s):
    s = HYPERLINK_REGEX.sub(r'\href{\2}{\1}', s)
    s = tex.escape_latex(s)
    s = s.replace('LaTeX', r'\LaTeX')

    # A bit of a hack... have to reverse some of tex.escape_latex escapes
    s = s.replace('\\textbackslash{}', '\\')
    s = s.replace('\\{', '{').replace('\\}', '}')
    return s

def escape_txt(s):
    # Replace all markdown-esque hyperlinks with just the link text
    s = HYPERLINK_REGEX.sub(r'\1', s)
    return s
