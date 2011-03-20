all: davidhu-resume.pdf

publish: resume.pdf resume.html
	scp `find . -maxdepth 1 -type f` dhu@david-hu.com:~/www/resume/
	scp $^ dyhu@csclub.uwaterloo.ca:~/www/

davidhu-resume.pdf: resume.pdf
	cp resume.pdf davidhu-resume.pdf

resume.pdf: resume.tex res.cls
	pdflatex resume.tex

resume.tex: template.tex resume.yaml genresumes.py
	./genresumes.py template.tex resume.yaml resume.tex
