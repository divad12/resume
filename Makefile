all: resume.pdf

files=resume.pdf resume.html resume.tex resume.yaml template.tex

# TODO: use rsync
publish: resume.pdf resume.html
	scp $(files) dhu@david-hu.com:~/www/resume/
	scp $(files) dyhu@csclub.uwaterloo.ca:~/www/

resume.pdf: resume.tex res.cls
	pdflatex resume.tex

resume.tex: template.tex resume.yaml genresumes.py
	./genresumes.py template.tex resume.yaml resume.tex
