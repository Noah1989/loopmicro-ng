SOURCES := $(shell find $(SOURCEDIR) -name '????-*.txt' | sort)
PDFS := $(SOURCES:%.txt=%.pdf)

.PHONY: date clean all default

all: date book.txt book.pdf

date:
	sed -e "s/[0-9]\{4\}-[0-9][0-9]-[0-9][0-9]/$$(date -I)/" -i 0000-cover.txt

book.txt: $(SOURCES)
	awk 'FNR==1 && NR!=1 {print "--------------------------------------------------------------------------------"}{print}' $(SOURCES) | reformat -w 80 -j > book.txt

%.textonly.raw: %.txt
	./textonly.py < $< | reformat -w 80 -j > $@

%.notext.raw: %.txt
	./notext.py < $< > $@

%.html: %.raw template.htm
	sed -e '/CONTENT/{r $<' -e 'd}' template.htm | ./expand.py > $@

%.pdf: %.html
	wkhtmltopdf -s A5 -O Landscape $< $@

%.nofonts.pdf: %.notext.pdf
	gs -dNoOutputFonts -dNOPAUSE -sDEVICE=pdfwrite -sOUTPUTFILE=$@ -dBATCH $<

%.svg: %.nofonts.pdf
	pdftocairo $< -svg - | grep 'xml\|svg\|rgb(0' > $@

%.flat.pdf: %.svg
	inkscape --actions='select-all;object-to-path;SelectionUnion;export-filename:$@;export-do' $<

%.pdf: %.textonly.pdf %.flat.pdf
	pdftk $*.textonly.pdf stamp $*.flat.pdf output $@

book.pdf: $(PDFS)
	gs -dNOPAUSE -sDEVICE=pdfwrite -sOUTPUTFILE=book.pdf -dBATCH $(PDFS)

clean:
	rm -f book.txt *.raw *.html *.svg *.pdf