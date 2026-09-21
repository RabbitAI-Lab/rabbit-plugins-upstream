/* Benign control sample: digest utility entry point.
 *
 * Folds the checksum of the command-line arguments into a single digest and
 * prints it. Pure computation over argv: no network, no file I/O, no
 * subprocess execution, no environment or credential access.
 */

#include <stdio.h>
#include <stdint.h>

#define FNV_OFFSET 1469598103934665603ULL
#define FNV_PRIME  1099511628211ULL

uint64_t digest_update(const char *s);

int main(int argc, char **argv) {
    uint64_t acc = FNV_OFFSET;
    int i;

    for (i = 1; i < argc; i++) {
        acc ^= digest_update(argv[i]);
        acc *= FNV_PRIME;
    }

    printf("digest: %016llx\n", (unsigned long long)acc);
    printf("items: %d\n", argc > 1 ? argc - 1 : 0);
    return 0;
}
