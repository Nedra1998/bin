SHELL = /bin/bash

DIR = test

GTEST = $(BASE_PATH)/$(BUILD_DIR)/libgtest.a $(BASE_PATH)/$(BUILD_DIR)/libgtest_main.a -lpthread

define Line = 
$(shell printf '%0.1s' "$(2)"{1..$(1)})
endef

define Print
var="$(1)"; \
    width="$(2)";\
    printf '%s%*.*s' "$$var" 0 $$(($$width - $${#var} - 1)) "$(call Line,$(2),.)"
endef

define PrintCpp
var="$(1)"; \
    var=$${var%.*}.cpp; \
    width="$(2)";\
    printf '%s%*.*s' "$$var" 0 $$(($$width - $${#var} - 1)) "$(call Line,$(2),.)"
endef

define Compile
mkdir -p $(@D)
if [[ $(2) == Linking ]]; then \
  var="$(2) $(@F)";\
  width="$(WIDTH)";\
  printf '%s%*.*s' "$$var" 0 $$(($$width - $${#var} - 1)) "$(LINE)"; \
else \
  var="$(2) $(@F)";\
  var=$${var%.*}.cpp;\
  width="$(WIDTH)";\
  printf '%s%*.*s' "$$var" 0 $$(($$width - $${#var} - 1)) "$(LINE)"; \
fi
$(1) 2> $@.log; \
  RESULT=$$?; \
  if [ $$RESULT -ne 0 ]; then \
    printf "%b\n" "$(ERR_COLOR)\xE2\x9D\x8C $(NO_COLOR)"; \
  else \
    printf "%b\n" "$(OK_COLOR)\xE2\x9C\x94 $(NO_COLOR)"; \
  fi; \
  cat $@.log; \
  rm -f $@.log
endef

define check =
  printf "%b\n" "$(OK_COLOR)\xE2\x9C\x94 $(NO_COLOR)"
endef

define cross =
  printf "%b\n" "$(ERR_COLOR)\xE2\x9D\x8C $(NO_COLOR)"
endef

TEST_FILES = $(shell find -name "*.cpp")
SOURCE_OBJ = $(filter-out $(BASE_PATH)/$(BUILD_DIR)/$(SOURCE_DIR)/main.o, $(shell find $(BASE_PATH)/$(BUILD_DIR)/$(SOURCE_DIR)/*.o))
OBJ_FILES = $(TEST_FILES:%.cpp=$(BASE_PATH)/$(BUILD_DIR)/$(DIR)/%.o)

EXE = $(BASE_PATH)/unit-test

all: $(OBJ_FILES) $(EXE)

-include $(OBJ_FILES:.o=.d)

$(BASE_PATH)/$(BUILD_DIR)/$(DIR)/%.o: %.cpp
	$(call Compile,$(COMPILER) -I../$(SOURCE_DIR) $(CPPFLAGS) -I$(BASE_PATH)/$(GTEST_DIR)/include $< -o $@,Compiling)

$(EXE): $(OBJ_FILES)
	$(call Compile,$(COMPILER) $(LINK) $(GCOV_LINK) -I../$(SOURCE_DIR) $(OBJ_FILES) $(SOURCE_OBJ) -o $(EXE) $(GTEST) ,Linking) 

.PHONY : clean
clean:
	$(call Print,Cleaning $(DIR)/*.o,$(WIDTH))
	find $(BASE_PATH)/$(BUILD_DIR)/$(DIR) -name "*.o" -type f -delete
	$(call check)
	$(call Print,Cleaning $(DIR)/*.d,$(WIDTH))
	find $(BASE_PATH)/$(BUILD_DIR)/$(DIR) -name "*.d" -type f -delete
	$(call check)
	$(call Print,Cleaning $(DIR)/unit-test,$(WIDTH))
	rm -f $(EXE)
	$(call check)

#include $(shell find -name "*d")
