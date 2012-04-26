all: resume.pdf resume.txt

files=resume.pdf resume.html resume.tex resume.yaml template.tex

# TODO: use rsync
.PHONY: publish
publish: resume.pdf resume.html
	scp $(files) ec2-user@david-hu.com:~/www/resume/
	scp $(files) dyhu@csclub.uwaterloo.ca:~/www/
	cp resume.pdf submit/davidhu-resume.pdf

resume.pdf: resume.tex res.cls
	pdflatex resume.tex

resume.tex: template.tex resume.yaml genresumes.py
	./genresumes.py tex

resume.txt: template.txt resume.yaml genresumes.py
	./genresumes.py txt

.PHONY: clean
clean:
	echo TODO
