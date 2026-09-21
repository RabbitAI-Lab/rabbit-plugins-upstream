/* Benign control sample: local checksum primitive.
 *
 * FNV-1a over a C string. Pure computation: no network, no file I/O,
 * no subprocess execution, no environment or credential access.
 */

#include <stdint.h>

#define FNV_OFFSET 1469598103934665603ULL
#define FNV_PRIME  1099511628211ULL

uint64_t digest_update(const char *s) {
    uint64_t h = FNV_OFFSET;
    while (*s != '\0') {
        h ^= (unsigned char)(*s++);
        h *= FNV_PRIME;
    }
    return h;
}
