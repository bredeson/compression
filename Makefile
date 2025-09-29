
PREFIX     := /usr/local

PACKAGE     = compression
SOURCE_DIR  = src
BUILD_DIR   = build
TEST_DIR    = test

LIB_DIR     = $(BUILD_DIR)/lib

ECHO       := echo
PYTHON     := $(filter /%,$(shell /bin/sh -c 'type python'))
INSTALL    := $(filter /%,$(shell /bin/sh -c 'type install'))
MKDIR      := $(filter /%,$(shell /bin/sh -c 'type mkdir'))
AWK        := $(filter /%,$(shell /bin/sh -c 'type awk'))
CAT        := $(filter /%,$(shell /bin/sh -c 'type cat'))
CP         := $(filter /%,$(shell /bin/sh -c 'type cp'))
RM         := $(filter /%,$(shell /bin/sh -c 'type rm'))

CP_R        = $(CP) -R
RM_R        = $(RM) -r

PYTHON_VER := $(shell $(PYTHON) --version 2>&1 | awk '{if (/Python/) {split($$2,v,".");print "python"v[1]"."v[2]}}')
INSTALL_REG = $(INSTALL) -p -m 644 -D
MKDIR_P     = $(MKDIR) -p

LICENSE    := LICENSE

INSTALL_PATH ?= \
	$(PREFIX)/lib/$(PYTHON_VER)/site-packages

BUILD_TARGETS = $(BGZ_BUILD_TARGETS) $(COMPRESSION_BUILD_TARGETS)

BGZ_SOURCE_FILES = $(SOURCE_DIR)/bgzip.py
BGZ_BUILD_TARGETS = $(patsubst $(SOURCE_DIR)/%,$(LIB_DIR)/%,$(BGZ_SOURCE_FILES))
BGZ_INSTALL_TARGETS = $(patsubst $(SOURCE_DIR)/%,$(INSTALL_PATH)/%,$(BGZ_SOURCE_FILES))

COMPRESSION_SOURCE_FILES = $(wildcard $(SOURCE_DIR)/$(PACKAGE)/*.py)
COMPRESSION_BUILD_TARGETS = $(patsubst $(SOURCE_DIR)/%,$(LIB_DIR)/%,$(COMPRESSION_SOURCE_FILES))
COMPRESSION_INSTALL_TARGETS = $(patsubst $(SOURCE_DIR)/%,$(INSTALL_PATH)/%,$(COMPRESSION_SOURCE_FILES))


.SUFFIXES:
.SUFFIXES: .py

.PHONY: install activate test clean 

all: build



build: $(LIB_DIR) $(BGZ_BUILD_TARGETS) $(COMPRESSION_BUILD_TARGETS)

$(LIB_DIR):
	@$(MKDIR_P) $@

$(LIB_DIR)/%: $(SOURCE_DIR)/%
	@$(MKDIR_P) $(@D)
	@$(AWK) '{print "#",$$_}' $(LICENSE) | $(CAT) - $< >$@



test: $(COMPRESSION_BUILD_TARGETS)
	cd $(TEST_DIR) && PYTHONPATH="$(PWD)/$(LIB_DIR)" $(PYTHON) test.py



activate:
	@$(ECHO) 'export PYTHONPATH="$(INSTALL_PATH)$${PYTHONPATH:+:$${PYTHONPATH}}";' >activate
	@$(ECHO) '#setenv PYTHONPATH "$(INSTALL_PATH):$$PYTHONPATH";' >>activate



install: test install-bgzip install-compression

install-bgzip: $(BGZ_INSTALL_TARGETS)

install-compression: test $(COMPRESSION_INSTALL_TARGETS)

$(INSTALL_PATH)/%.py: $(LIB_DIR)/%.py
	$(INSTALL_REG) $< $@

$(INSTALL_PATH)/$(PACKAGE)/%.py: $(LIB_DIR)/$(PACKAGE)/%.py
	$(INSTALL_REG) $< $@



clean:
	-$(RM_R) $(BUILD_DIR) $(TEST_DIR)/test.caller.* $(TEST_DIR)/test.stream.* $(TEST_DIR)/test.stdio.* 
