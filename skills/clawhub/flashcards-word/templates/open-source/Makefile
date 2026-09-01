.PHONY: cards clean
all: cards

cards:
	python3 scripts/words100.py
	python3 scripts/download_emoji.py
	python3 scripts/generate_all.py
	python3 scripts/build_docx.py

clean:
	rm -rf emoji all_front all_back English_Words_DoubleSided.docx
