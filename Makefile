LANGS = EN-US KO ZH
MDS   = $(LANGS:%=README.%.md)

all: $(MDS)

XLATE = xlate

define LANG_PM
README.$1.md: README.md Makefile
	exec > $$@; \
	printf "%s\n\n" \
	"This document is automatically generated from README.md written in Japanese"; \
	$$(XLATE) -t $1 -o md $$<
endef

$(foreach lang,$(LANGS),$(eval $(call LANG_PM,$(lang))))
