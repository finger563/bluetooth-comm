CFLAGS = 
CPPFLAGS = 
LDFLAGS = -lbluetooth

% : %.c
	$(CC) $(CFLAGS) $(CPPFLAGS) -o $@ $< $(LDFLAGS)
all: $(basename $(wildcard *.c))


.PHONY: clean
clean:
	rm -rf $(basename $(wildcard *.c))
