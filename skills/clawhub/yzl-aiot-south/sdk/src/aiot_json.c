/*
 * aiot_json.c - 有界字符串构造器 + 轻量 JSON 解析器
 *
 * 这个解析器只做 SDK 需要的事：
 *   - 解析平台下发的单帧 JSON；
 *   - 按 key 取对象成员、按 index 取数组元素；
 *   - 解码字符串（含 \uXXXX）；
 *   - 读取整数。
 * 不分配内存，不依赖 libc 的 strtod/sscanf。
 */

#include "aiot_internal.h"

#include <string.h>

/* ========================================================================= */
/* 字符串构造器                                                              */
/* ========================================================================= */

void aiot_sb_init(aiot_sb_t *sb, char *buf, size_t cap)
{
    sb->buf = buf;
    sb->cap = cap;
    sb->len = 0;
    sb->overflow = (buf == NULL || cap == 0);
    if (buf != NULL && cap > 0) {
        buf[0] = '\0';
    }
}

int aiot_sb_putc(aiot_sb_t *sb, char c)
{
    if (sb->overflow || sb->len + 1 >= sb->cap) {
        sb->overflow = 1;
        return -1;
    }
    sb->buf[sb->len++] = c;
    sb->buf[sb->len] = '\0';
    return 0;
}

int aiot_sb_write(aiot_sb_t *sb, const char *s, size_t len)
{
    if (sb->overflow || len > sb->cap - sb->len - 1) {
        sb->overflow = 1;
        return -1;
    }
    if (len > 0) {
        memcpy(sb->buf + sb->len, s, len);
        sb->len += len;
        sb->buf[sb->len] = '\0';
    }
    return 0;
}

int aiot_sb_puts(aiot_sb_t *sb, const char *s)
{
    return aiot_sb_write(sb, s, strlen(s));
}

static int sb_hex4(aiot_sb_t *sb, unsigned int v)
{
    static const char hex[] = "0123456789abcdef";
    return aiot_sb_putc(sb, hex[(v >> 12) & 0xF]) ||
           aiot_sb_putc(sb, hex[(v >> 8) & 0xF]) ||
           aiot_sb_putc(sb, hex[(v >> 4) & 0xF]) ||
           aiot_sb_putc(sb, hex[v & 0xF]);
}

int aiot_sb_json_strn(aiot_sb_t *sb, const char *s, size_t len)
{
    size_t i;

    if (aiot_sb_putc(sb, '"') != 0) {
        return -1;
    }
    for (i = 0; i < len; i++) {
        unsigned char c = (unsigned char)s[i];
        switch (c) {
        case '"':
            if (aiot_sb_write(sb, "\\\"", 2) != 0) return -1;
            break;
        case '\\':
            if (aiot_sb_write(sb, "\\\\", 2) != 0) return -1;
            break;
        case '\b':
            if (aiot_sb_write(sb, "\\b", 2) != 0) return -1;
            break;
        case '\f':
            if (aiot_sb_write(sb, "\\f", 2) != 0) return -1;
            break;
        case '\n':
            if (aiot_sb_write(sb, "\\n", 2) != 0) return -1;
            break;
        case '\r':
            if (aiot_sb_write(sb, "\\r", 2) != 0) return -1;
            break;
        case '\t':
            if (aiot_sb_write(sb, "\\t", 2) != 0) return -1;
            break;
        default:
            if (c < 0x20) {
                if (aiot_sb_write(sb, "\\u00", 4) != 0) return -1;
                if (sb_hex4(sb, c) != 0) return -1;
            } else {
                if (aiot_sb_putc(sb, (char)c) != 0) return -1;
            }
            break;
        }
    }
    return aiot_sb_putc(sb, '"');
}

int aiot_sb_json_str(aiot_sb_t *sb, const char *s)
{
    return aiot_sb_json_strn(sb, s, strlen(s));
}

int aiot_sb_u32(aiot_sb_t *sb, aiot_u32 v)
{
    char tmp[10];
    int n = 0;

    if (v == 0) {
        return aiot_sb_putc(sb, '0');
    }
    while (v > 0) {
        tmp[n++] = (char)('0' + (v % 10));
        v /= 10;
    }
    while (n > 0) {
        if (aiot_sb_putc(sb, tmp[--n]) != 0) {
            return -1;
        }
    }
    return 0;
}

int aiot_sb_i32(aiot_sb_t *sb, aiot_i32 v)
{
    if (v < 0) {
        aiot_u32 mag;
        if (aiot_sb_putc(sb, '-') != 0) {
            return -1;
        }
        /* 避免 -INT32_MIN 溢出；先加 1 再取反 */
        mag = (aiot_u32)(-(v + 1)) + 1u;
        return aiot_sb_u32(sb, mag);
    }
    return aiot_sb_u32(sb, (aiot_u32)v);
}

int aiot_sb_ok(const aiot_sb_t *sb)
{
    return sb != NULL && !sb->overflow;
}

/* ========================================================================= */
/* JSON 解析器                                                               */
/* ========================================================================= */

typedef struct {
    const char *s;
    size_t len;
    size_t pos;
    aiot_json_tok_t *toks;
    int ntok;
    int max;
    int depth;
} aiot_parser_t;

static void skip_ws(aiot_parser_t *p)
{
    while (p->pos < p->len) {
        char c = p->s[p->pos];
        if (c == ' ' || c == '\t' || c == '\r' || c == '\n') {
            p->pos++;
        } else {
            break;
        }
    }
}

static int new_token(aiot_parser_t *p, aiot_u8 type, aiot_u16 start, aiot_u16 parent)
{
    int idx;

    if (p->ntok >= p->max) {
        return -1;
    }
    idx = p->ntok++;
    p->toks[idx].type = type;
    p->toks[idx].start = start;
    p->toks[idx].end = start;
    p->toks[idx].parent = parent;
    p->toks[idx].count = 0;
    return idx;
}

static int hex_val(char c)
{
    if (c >= '0' && c <= '9') return c - '0';
    if (c >= 'a' && c <= 'f') return c - 'a' + 10;
    if (c >= 'A' && c <= 'F') return c - 'A' + 10;
    return -1;
}

static int parse_string(aiot_parser_t *p, aiot_u16 parent)
{
    aiot_u16 start = (aiot_u16)p->pos;
    int idx;

    /* 当前字符是 '"' */
    p->pos++;
    while (p->pos < p->len) {
        char c = p->s[p->pos];
        if (c == '"') {
            p->pos++;
            idx = new_token(p, AIOT_JSON_STRING, start, parent);
            if (idx < 0) return -1;
            p->toks[idx].end = (aiot_u16)p->pos;
            return idx;
        }
        if (c == '\\') {
            p->pos++;
            if (p->pos >= p->len) return -1;
            if (p->s[p->pos] == 'u') {
                int i;
                p->pos++;
                for (i = 0; i < 4; i++) {
                    if (p->pos >= p->len || hex_val(p->s[p->pos]) < 0) return -1;
                    p->pos++;
                }
            } else {
                p->pos++;
            }
            continue;
        }
        if ((unsigned char)c < 0x20) {
            return -1;
        }
        p->pos++;
    }
    return -1;
}

static int parse_number(aiot_parser_t *p, aiot_u16 parent)
{
    aiot_u16 start = (aiot_u16)p->pos;
    int idx;

    if (p->pos < p->len && p->s[p->pos] == '-') {
        p->pos++;
    }
    if (p->pos >= p->len || p->s[p->pos] < '0' || p->s[p->pos] > '9') {
        return -1;
    }
    if (p->s[p->pos] == '0') {
        p->pos++;
    } else {
        while (p->pos < p->len && p->s[p->pos] >= '0' && p->s[p->pos] <= '9') {
            p->pos++;
        }
    }
    if (p->pos < p->len && p->s[p->pos] == '.') {
        p->pos++;
        if (p->pos >= p->len || p->s[p->pos] < '0' || p->s[p->pos] > '9') return -1;
        while (p->pos < p->len && p->s[p->pos] >= '0' && p->s[p->pos] <= '9') {
            p->pos++;
        }
    }
    if (p->pos < p->len && (p->s[p->pos] == 'e' || p->s[p->pos] == 'E')) {
        p->pos++;
        if (p->pos < p->len && (p->s[p->pos] == '+' || p->s[p->pos] == '-')) {
            p->pos++;
        }
        if (p->pos >= p->len || p->s[p->pos] < '0' || p->s[p->pos] > '9') return -1;
        while (p->pos < p->len && p->s[p->pos] >= '0' && p->s[p->pos] <= '9') {
            p->pos++;
        }
    }
    idx = new_token(p, AIOT_JSON_NUMBER, start, parent);
    if (idx < 0) return -1;
    p->toks[idx].end = (aiot_u16)p->pos;
    return idx;
}

static int parse_value(aiot_parser_t *p, aiot_u16 parent);

static int parse_array(aiot_parser_t *p, aiot_u16 parent)
{
    aiot_u16 start = (aiot_u16)p->pos;
    int idx;

    idx = new_token(p, AIOT_JSON_ARRAY, start, parent);
    if (idx < 0) return -1;
    p->pos++; /* '[' */
    skip_ws(p);
    if (p->pos < p->len && p->s[p->pos] == ']') {
        p->pos++;
        p->toks[idx].end = (aiot_u16)p->pos;
        return idx;
    }
    while (1) {
        int v;
        if (p->depth++ >= AIOT_JSON_MAX_DEPTH) return -1;
        v = parse_value(p, (aiot_u16)idx);
        p->depth--;
        if (v < 0) return -1;
        if (p->toks[idx].count < 255) {
            p->toks[idx].count++;
        }
        skip_ws(p);
        if (p->pos >= p->len) return -1;
        if (p->s[p->pos] == ',') {
            p->pos++;
            skip_ws(p);
            continue;
        }
        if (p->s[p->pos] == ']') {
            p->pos++;
            p->toks[idx].end = (aiot_u16)p->pos;
            return idx;
        }
        return -1;
    }
}

static int parse_object(aiot_parser_t *p, aiot_u16 parent)
{
    aiot_u16 start = (aiot_u16)p->pos;
    int idx;

    idx = new_token(p, AIOT_JSON_OBJECT, start, parent);
    if (idx < 0) return -1;
    p->pos++; /* '{' */
    skip_ws(p);
    if (p->pos < p->len && p->s[p->pos] == '}') {
        p->pos++;
        p->toks[idx].end = (aiot_u16)p->pos;
        return idx;
    }
    while (1) {
        int k, v;
        if (p->pos >= p->len || p->s[p->pos] != '"') return -1;
        k = parse_string(p, (aiot_u16)idx);
        if (k < 0) return -1;
        skip_ws(p);
        if (p->pos >= p->len || p->s[p->pos] != ':') return -1;
        p->pos++;
        skip_ws(p);
        if (p->depth++ >= AIOT_JSON_MAX_DEPTH) return -1;
        v = parse_value(p, (aiot_u16)idx);
        p->depth--;
        if (v < 0) return -1;
        if (p->toks[idx].count < 255) {
            p->toks[idx].count++;
        }
        skip_ws(p);
        if (p->pos >= p->len) return -1;
        if (p->s[p->pos] == ',') {
            p->pos++;
            skip_ws(p);
            continue;
        }
        if (p->s[p->pos] == '}') {
            p->pos++;
            p->toks[idx].end = (aiot_u16)p->pos;
            return idx;
        }
        return -1;
    }
}

static int parse_value(aiot_parser_t *p, aiot_u16 parent)
{
    char c;

    skip_ws(p);
    if (p->pos >= p->len) return -1;
    c = p->s[p->pos];
    switch (c) {
    case '{':
        return parse_object(p, parent);
    case '[':
        return parse_array(p, parent);
    case '"':
        return parse_string(p, parent);
    case 't':
        if (p->len - p->pos >= 4 && memcmp(p->s + p->pos, "true", 4) == 0) {
            int idx = new_token(p, AIOT_JSON_BOOL, (aiot_u16)p->pos, parent);
            if (idx < 0) return -1;
            p->pos += 4;
            p->toks[idx].end = (aiot_u16)p->pos;
            return idx;
        }
        return -1;
    case 'f':
        if (p->len - p->pos >= 5 && memcmp(p->s + p->pos, "false", 5) == 0) {
            int idx = new_token(p, AIOT_JSON_BOOL, (aiot_u16)p->pos, parent);
            if (idx < 0) return -1;
            p->pos += 5;
            p->toks[idx].end = (aiot_u16)p->pos;
            return idx;
        }
        return -1;
    case 'n':
        if (p->len - p->pos >= 4 && memcmp(p->s + p->pos, "null", 4) == 0) {
            int idx = new_token(p, AIOT_JSON_NULL, (aiot_u16)p->pos, parent);
            if (idx < 0) return -1;
            p->pos += 4;
            p->toks[idx].end = (aiot_u16)p->pos;
            return idx;
        }
        return -1;
    default:
        if (c == '-' || (c >= '0' && c <= '9')) {
            return parse_number(p, parent);
        }
        return -1;
    }
}

int aiot_json_parse(const char *json, size_t len,
                    aiot_json_tok_t *tokens, int max_tokens)
{
    aiot_parser_t p;
    int root;

    if (json == NULL || tokens == NULL || max_tokens <= 0 || len > 65535) {
        return AIOT_ERR_ARG;
    }
    memset(&p, 0, sizeof p);
    p.s = json;
    p.len = len;
    p.toks = tokens;
    p.max = max_tokens;

    root = parse_value(&p, 0xFFFF);
    if (root < 0) {
        return AIOT_ERR_PARSE;
    }
    skip_ws(&p);
    if (p.pos != p.len) {
        return AIOT_ERR_PARSE;
    }
    return p.ntok;
}

int aiot_json_obj_get(const char *json, const aiot_json_tok_t *tokens,
                      int ntokens, int obj, const char *key)
{
    int i;
    size_t klen;

    if (obj < 0 || obj >= ntokens || tokens[obj].type != AIOT_JSON_OBJECT || key == NULL) {
        return -1;
    }
    klen = strlen(key);
    for (i = obj + 1; i + 1 < ntokens; i++) {
        int v;
        if (tokens[i].parent != (aiot_u16)obj || tokens[i].type != AIOT_JSON_STRING) {
            continue;
        }
        v = i + 1;
        if (v >= ntokens || tokens[v].parent != (aiot_u16)obj) {
            continue;
        }
        {
            size_t raw_len = (size_t)(tokens[i].end - tokens[i].start);
            if (raw_len == klen + 2) {
                if (memcmp(json + tokens[i].start + 1, key, klen) == 0) {
                    return v;
                }
            } else if (raw_len > klen + 2) {
                char tmp[48];
                if (aiot_json_get_str(json, tokens, ntokens, i, tmp, sizeof tmp) >= 0 &&
                    strlen(tmp) == klen && memcmp(tmp, key, klen) == 0) {
                    return v;
                }
            }
        }
    }
    return -1;
}

int aiot_json_arr_get(const char *json, const aiot_json_tok_t *tokens,
                      int ntokens, int arr, int index)
{
    int i, n = 0;

    (void)json;
    if (arr < 0 || arr >= ntokens || tokens[arr].type != AIOT_JSON_ARRAY || index < 0) {
        return -1;
    }
    for (i = arr + 1; i < ntokens; i++) {
        if (tokens[i].parent != (aiot_u16)arr) {
            continue;
        }
        if (n == index) {
            return i;
        }
        n++;
    }
    return -1;
}

const char *aiot_json_raw(const char *json, const aiot_json_tok_t *tokens,
                          int ntokens, int idx, size_t *len)
{
    if (idx < 0 || idx >= ntokens) {
        if (len) *len = 0;
        return NULL;
    }
    if (len) {
        *len = (size_t)(tokens[idx].end - tokens[idx].start);
    }
    return json + tokens[idx].start;
}

static int utf8_put(char *out, size_t cap, size_t *n, aiot_u32 cp)
{
    if (cp <= 0x7F) {
        if (*n + 1 >= cap) return -1;
        out[(*n)++] = (char)cp;
    } else if (cp <= 0x7FF) {
        if (*n + 2 >= cap) return -1;
        out[(*n)++] = (char)(0xC0 | (cp >> 6));
        out[(*n)++] = (char)(0x80 | (cp & 0x3F));
    } else if (cp <= 0xFFFF) {
        if (*n + 3 >= cap) return -1;
        out[(*n)++] = (char)(0xE0 | (cp >> 12));
        out[(*n)++] = (char)(0x80 | ((cp >> 6) & 0x3F));
        out[(*n)++] = (char)(0x80 | (cp & 0x3F));
    } else {
        if (*n + 4 >= cap) return -1;
        out[(*n)++] = (char)(0xF0 | (cp >> 18));
        out[(*n)++] = (char)(0x80 | ((cp >> 12) & 0x3F));
        out[(*n)++] = (char)(0x80 | ((cp >> 6) & 0x3F));
        out[(*n)++] = (char)(0x80 | (cp & 0x3F));
    }
    return 0;
}

static aiot_u32 parse_hex4(const char *s)
{
    aiot_u32 v = 0;
    int i;
    for (i = 0; i < 4; i++) {
        v = (v << 4) | (aiot_u32)hex_val(s[i]);
    }
    return v;
}

int aiot_json_get_str(const char *json, const aiot_json_tok_t *tokens,
                      int ntokens, int idx, char *out, size_t cap)
{
    size_t i, n = 0;
    aiot_u16 start, end;

    if (idx < 0 || idx >= ntokens || tokens[idx].type != AIOT_JSON_STRING ||
        out == NULL || cap == 0) {
        return AIOT_ERR_ARG;
    }
    start = tokens[idx].start;
    end = tokens[idx].end;
    if (end < start + 2) {
        return AIOT_ERR_PARSE;
    }
    for (i = (size_t)start + 1; i + 1 < end; i++) {
        char c = json[i];
        if (c == '\\') {
            char e;
            i++;
            if (i + 1 > end) return AIOT_ERR_PARSE;
            e = json[i];
            switch (e) {
            case '"': c = '"'; break;
            case '\\': c = '\\'; break;
            case '/': c = '/'; break;
            case 'b': c = '\b'; break;
            case 'f': c = '\f'; break;
            case 'n': c = '\n'; break;
            case 'r': c = '\r'; break;
            case 't': c = '\t'; break;
            case 'u': {
                aiot_u32 cp;
                if (i + 4 >= end) return AIOT_ERR_PARSE;
                cp = parse_hex4(json + i + 1);
                i += 4;
                /* 代理对 */
                if (cp >= 0xD800 && cp <= 0xDBFF && i + 6 < end &&
                    json[i + 1] == '\\' && json[i + 2] == 'u') {
                    aiot_u32 lo = parse_hex4(json + i + 3);
                    if (lo >= 0xDC00 && lo <= 0xDFFF) {
                        cp = 0x10000 + ((cp - 0xD800) << 10) + (lo - 0xDC00);
                        i += 6;
                    }
                }
                if (cp == 0) cp = 0x20; /* C 字符串不能含 NUL，替换为空格 */
                if (utf8_put(out, cap, &n, cp) != 0) return AIOT_ERR_NOMEM;
                continue;
            }
            default:
                return AIOT_ERR_PARSE;
            }
            if (n + 1 >= cap) return AIOT_ERR_NOMEM;
            out[n++] = c;
        } else {
            if (n + 1 >= cap) return AIOT_ERR_NOMEM;
            out[n++] = c;
        }
    }
    out[n] = '\0';
    return (int)n;
}

int aiot_json_get_i32(const char *json, const aiot_json_tok_t *tokens,
                      int ntokens, int idx, aiot_i32 *out)
{
    size_t i;
    int neg = 0;
    unsigned long v = 0;

    if (out == NULL || idx < 0 || idx >= ntokens || tokens[idx].type != AIOT_JSON_NUMBER) {
        return AIOT_ERR_ARG;
    }
    i = tokens[idx].start;
    if (json[i] == '-') {
        neg = 1;
        i++;
    }
    for (; i < tokens[idx].end; i++) {
        char c = json[i];
        unsigned long digit;
        if (c < '0' || c > '9') {
            break;
        }
        digit = (unsigned long)(c - '0');
        if (v > (2147483648UL - digit) / 10UL) {
            return AIOT_ERR_OVERFLOW;
        }
        v = v * 10UL + digit;
    }
    if (neg) {
        if (v == 2147483648UL) {
            *out = (-2147483647 - 1);
        } else {
            *out = -(aiot_i32)v;
        }
    } else {
        if (v > 2147483647UL) {
            return AIOT_ERR_OVERFLOW;
        }
        *out = (aiot_i32)v;
    }
    return 0;
}

int aiot_json_get_u32(const char *json, const aiot_json_tok_t *tokens,
                      int ntokens, int idx, aiot_u32 *out)
{
    size_t i;
    unsigned long v = 0;

    if (out == NULL || idx < 0 || idx >= ntokens || tokens[idx].type != AIOT_JSON_NUMBER) {
        return AIOT_ERR_ARG;
    }
    i = tokens[idx].start;
    if (json[i] == '-') {
        return AIOT_ERR_ARG;
    }
    for (; i < tokens[idx].end; i++) {
        char c = json[i];
        unsigned long digit;
        if (c < '0' || c > '9') {
            break;
        }
        digit = (unsigned long)(c - '0');
        if (v > (4294967295UL - digit) / 10UL) {
            return AIOT_ERR_OVERFLOW;
        }
        v = v * 10UL + digit;
    }
    *out = (aiot_u32)v;
    return 0;
}

int aiot_json_is_str(const char *json, const aiot_json_tok_t *tokens,
                     int ntokens, int idx, const char *value)
{
    char tmp[32];
    int n;
    size_t vlen;

    if (idx < 0 || idx >= ntokens || tokens[idx].type != AIOT_JSON_STRING ||
        value == NULL) {
        return 0;
    }
    vlen = strlen(value);
    if (vlen + 1 > sizeof tmp) {
        return 0;
    }
    n = aiot_json_get_str(json, tokens, ntokens, idx, tmp, sizeof tmp);
    return n >= 0 && (size_t)n == vlen && memcmp(tmp, value, vlen) == 0;
}

int aiot_copy_str(char *dst, size_t cap, const char *src)
{
    size_t n;

    if (dst == NULL || cap == 0 || src == NULL) {
        return -1;
    }
    n = strlen(src);
    if (n >= cap) {
        return -1;
    }
    memcpy(dst, src, n + 1);
    return 0;
}
