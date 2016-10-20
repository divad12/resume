#Resume was created using:
- YAML source - for the resume content
- LaTeX template - for presentation and layout
- Python script and Cheetah (templating engine) for compiling together the
  YAML and LaTeX
- pdflatex for .tex --> .pdf
- GNU Make for compilation
- Vim and git


The purpose is to avoid data duplication and to separate content from
presentation. For example, I can now create an HTML resume by writing just a
CSS + HTML template without having to copy-paste job descriptions, etc. Editing
and updating is restricted to just one place - the YAML source.


Rough instructions (will update as a blog post when I roll a blog engine):

0. Install dependencies: LaTeX, Python, etc.
1. Install yaml parser. For Python:
    sudo apt-get install python-yaml
   Install tex package for python:
    sudo pip install tex
   Install python-cheetah (templating engine):
    sudo easy_install cheetah
2. Get LaTeX resume templates or use the one here (based on Paciorek's, the first link)
    - http://biosun1.harvard.edu/~paciorek/computing/Latex_template_creating_CV_.html
    - http://linux.dsplabs.com.au/resume-writing-example-latex-template-linux-curriculum-vitae-professional-cv-layout-format-text-p54/
    - http://www.thelinuxdaily.com/2008/10/latex-resume-examples/
    - http://www.yisongyue.com/resume/
3. Write resume in YAML format.
4. Modify a LaTeX resume template with Cheetah tags.
5. Write Makefile.
6. Compile, preview, and edit.


###TODO:
  - custom types to unescape Latex (eg \LaTeX, \url{})
  - clean up this README and convert into markdown
  - add HTML layout
  - keep LinkedIn, Google profile, and Facebook in sync
  - turn this into an easy-to-use web app
