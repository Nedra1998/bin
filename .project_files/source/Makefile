SHELL = /bin/bash

DIR = source

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

SRC_FILES = $(shell find -name "*.cpp")
OBJ_FILES = $(SRC_FILES:%.cpp=$(BASE_PATH)/$(BUILD_DIR)/$(DIR)/%.o)
EXE = $(BASE_PATH)/$(NAME)

all: $(OBJ_FILES) $(EXE)

-include $(OBJ_FILES:.o=.d)

$(BASE_PATH)/$(BUILD_DIR)/$(DIR)/%.o: %.cpp
	$(call Compile,$(COMPILER) $(CPPFLAGS) $(GCOV_FLAG) $< -o $@,Compiling)


$(EXE): $(OBJ_FILES)
	$(call Compile,$(COMPILER) $(OBJ_FILES) $(GCOV_LINK) -o $(EXE),Linking) 

.PHONY : clean
clean:
	$(call Print,Cleaning $(DIR)/*.o,$(WIDTH))
	find $(BASE_PATH)/$(BUILD_DIR)/$(DIR) -name "*.o" -type f -delete
	$(call check)
	$(call Print,Cleaning $(DIR)/*.d,$(WIDTH))
	find $(BASE_PATH)/$(BUILD_DIR)/$(DIR) -name "*.d" -type f -delete
	$(call check)
	$(call Print,Cleaning $(DIR)/$(NAME),$(WIDTH))
	rm -f $(EXE)
	$(call check)

#include $(shell find -name "*d")
