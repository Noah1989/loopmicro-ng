SOURCES := $(shell find $(SOURCEDIR) -name '????-*.txt' | sort)
PDFS := $(SOURCES:%.txt=%.pdf)

.PHONY: clean all

all:
	sed -e "s/[0-9]\{4\}-[0-9][0-9]-[0-9][0-9]/$$(date -I)/" -i 0000-cover.txt
	${MAKE} book.pdf

book.pdf: $(PDFS)
	pdfunite $(PDFS) book.pdf

%.html: %.txt template.htm
	sed -e '/CONTENT/{r $<' -e 'd}' template.htm | ./expand.py > $@

%.pdf: %.html
	wkhtmltopdf -s A5 -O Landscape $< $@

.PRECIOUS: %.html

clean:
	rm -f *.html *.pdf