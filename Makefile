all: resume.pdf

publish: resume.pdf resume.html
	scp `find . -maxdepth 1 -type f` dhu@david-hu.com:~/www/resume/
	scp $^ dyhu@csclub.uwaterloo.ca:~/www/

resume.pdf: resume.tex res.cls
	pdflatex resume.tex

resume.tex: template.tex resume.yaml genresumes.py
	./genresumes.py template.tex resume.yaml resume.tex
