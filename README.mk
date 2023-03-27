LANGS    := EN-US

READMES  := $(LANGS:%=README.%.md)
ALL      := $(READMES)

all: $(ALL)

XLATE := xlate -a
XLATE += -p '^(\S.+\n)+|^ *[-*] *\K.+\n'
EXCLUDE += --exclude '^\#.*' --exclude '^\p{ASCII}+\n'
IGNORE := VERSION|AUTHOR|LICENSE|COPYRIGHT
$(foreach title,$(IGNORE),$(eval \
	EXCLUDE+=--exclude '(?i)^\#+ *($(title)).*\n(?s:.*?)(?=^\#|\z)' \
))

define MAKE_README
README.$1.md: README.md README.mk
	exec > $$@.tmp && \
	printf "This document is automatically generated from $$< written in Japanese\n\n" && \
	$(XLATE) -t $1 $$< $(EXCLUDE)
	mv $$@.tmp $$@
endef
$(foreach lang,$(LANGS),$(eval $(call MAKE_README,$(lang))))

clean:
	rm -f $(ALL)
