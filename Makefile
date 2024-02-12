LANGS  := EN-US KO ZH
MDS    := $(LANGS:%=README.%.md)
IGNORE := VERSION AUTHOR LICENSE COPYRIGHT INSTALL

all: $(MDS)

XLATE := xlate

ifdef IGNORE
$(foreach ignore,$(IGNORE),$(eval \
  GREPLEOPT += --exclude '^\#+[ ]*(?i:$(ignore))\b(?s:.*?)(?=^\#|\z)' \
))
endif

define LANG_PM
README.$1.md: README.md Makefile
	exec > $$@; \
	printf "%s\n\n" \
	"This document is automatically generated from README.md written in Japanese"; \
	$$(XLATE) -t $1 -o md -- $(GREPLEOPT) $$<
endef

$(foreach lang,$(LANGS),$(eval $(call LANG_PM,$(lang))))
