#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int main(int argc, char* argv[]) {
	// expect 2 args (3 in total)
	if (argc < 3)
		exit(1);
	if (argc > 3)
		exit(1);

	char* path_to_shorten = argv[1];
	char* path_parent = argv[2];
	
	int c = strcmp(path_to_shorten, path_parent);

	// strings are equal
	if (c == 0) {
		printf("%s", argv[1]);
		exit(0);
	}

	int ls = strlen(path_to_shorten);
	int lp = strlen(path_parent);

	// path_to_shorten < path_parent
	if (ls < lp) {
		printf("%s", argv[1]);
		exit(0);
	}

	// check if path_parent is contained within path_to_shorten
	for (int i = 0; i < lp; i++) {
		if (path_to_shorten[i] != path_parent[i]) {
			printf("%s", argv[1]);
			exit(0);
		}
	}

	char* shortened = (char*)malloc(sizeof(path_to_shorten));

	// finally, build the shortened string
	int i = lp;
	while (i < ls) {
		shortened[i-lp] = path_to_shorten[i];
		i++;
	}

	shortened[i-lp] = '\0';

	printf("%s", shortened);
}
