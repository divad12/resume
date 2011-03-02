all: resume.pdf

resume.pdf: resume.tex
	pdflatex resume.tex

resume.tex: template.tex resume.yaml
	./genresumes.py template.tex resume.yaml resume.tex
