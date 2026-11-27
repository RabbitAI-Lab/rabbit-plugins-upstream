/*
 * aiot_sdk.c - AIoT C SDK 单文件合并版（C89，自动生成，请勿手工修改）
 *
 * 生成命令: python tools/amalgamate.py
 * 源文件:   src/aiot_json.c + src/aiot.c
 *
 * Keil/IAR: 把本文件、aiot.h、aiot_types.h 加入工程即可。
 * 需要 MQTT 客户端时，另行添加 port/aiot_port_posix.c 和
 * port/aiot_mqtt_client.c（仅限有 socket 的平台）。
 */

#include "aiot.h"

/* ==================== aiot_internal.h ==================== */
/*
 * aiot_internal.h - SDK 内部使用的 JSON 解析器和字符串构造器。
 * 不属于公开 API，可能随版本变化。
 */

#ifndef AIOT_INTERNAL_H
#define AIOT_INTERNAL_H

#include "aiot.h"

#include <stddef.h>

#ifdef __cplusplus
extern "C" {
#endif

/* ------------------------------------------------------------------------- */
/* 有界字符串构造器                                                          */
/* ------------------------------------------------------------------------- */

typedef struct {
    char *buf;
    size_t cap;
    size_t len;
    int overflow;
} aiot_sb_t;

void aiot_sb_init(aiot_sb_t *sb, char *buf, size_t cap);
int aiot_sb_putc(aiot_sb_t *sb, char c);
int aiot_sb_puts(aiot_sb_t *sb, const char *s);
int aiot_sb_write(aiot_sb_t *sb, const char *s, size_t len);
int aiot_sb_json_str(aiot_sb_t *sb, const char *s);
int aiot_sb_json_strn(aiot_sb_t *sb, const char *s, size_t len);
int aiot_sb_u32(aiot_sb_t *sb, aiot_u32 v);
int aiot_sb_i32(aiot_sb_t *sb, aiot_i32 v);
int aiot_sb_ok(const aiot_sb_t *sb);

/* ------------------------------------------------------------------------- */
/* 轻量 JSON 词法/语法分析                                                   */
/* ------------------------------------------------------------------------- */

typedef enum {
    AIOT_JSON_NULL = 0,
    AIOT_JSON_BOOL,
    AIOT_JSON_NUMBER,
    AIOT_JSON_STRING,
    AIOT_JSON_OBJECT,
    AIOT_JSON_ARRAY
} aiot_json_type_t;

typedef struct {
    aiot_u16 start;  /* 在 JSON 文本中的起始偏移（含引号/括号） */
    aiot_u16 end;    /* 结束偏移（不含），字符串不含结尾引号 */
    aiot_u16 parent; /* 父 token 下标，0xFFFF 表示根 */
    aiot_u8 type;
    aiot_u8 count;   /* object: 键值对数量; array: 元素数量 */
} aiot_json_tok_t;

#ifndef AIOT_JSON_MAX_TOKENS
#define AIOT_JSON_MAX_TOKENS 128
#endif

#ifndef AIOT_JSON_MAX_DEPTH
#define AIOT_JSON_MAX_DEPTH 16
#endif

/*
 * 解析完整 JSON 文本。成功返回 token 数量（>0），失败返回负数。
 * token[0] 为根。文本必须是单个 JSON 值（前后空白允许）。
 */
int aiot_json_parse(const char *json, size_t len,
                    aiot_json_tok_t *tokens, int max_tokens);

/* 对象取键；返回 value token 下标，找不到返回 -1。 */
int aiot_json_obj_get(const char *json, const aiot_json_tok_t *tokens,
                      int ntokens, int obj, const char *key);

/* 数组取元素；返回元素 token 下标，越界返回 -1。 */
int aiot_json_arr_get(const char *json, const aiot_json_tok_t *tokens,
                      int ntokens, int arr, int index);

/* 解码字符串 token 到 out（自动补 0）。返回长度，失败返回负。 */
int aiot_json_get_str(const char *json, const aiot_json_tok_t *tokens,
                      int ntokens, int idx, char *out, size_t cap);

/* 读取整数（支持负号，忽略小数/指数部分）。 */
int aiot_json_get_i32(const char *json, const aiot_json_tok_t *tokens,
                      int ntokens, int idx, aiot_i32 *out);

int aiot_json_get_u32(const char *json, const aiot_json_tok_t *tokens,
                      int ntokens, int idx, aiot_u32 *out);

/* 取 token 原始文本（不补 0）。 */
const char *aiot_json_raw(const char *json, const aiot_json_tok_t *tokens,
                          int ntokens, int idx, size_t *len);

/* 判断 token 是否为字符串且等于给定值。 */
int aiot_json_is_str(const char *json, const aiot_json_tok_t *tokens,
                     int ntokens, int idx, const char *value);

/* ------------------------------------------------------------------------- */
/* 内部小工具                                                                */
/* ------------------------------------------------------------------------- */

/* 把字符串复制到固定缓冲区；超长返回 -1。 */
int aiot_copy_str(char *dst, size_t cap, const char *src);

/* 32 位回绕安全的经过时间判断（C89：用宏代替 inline）。 */
#define AIOT_ELAPSED(now, since, interval) \
    ((aiot_u32)((now) - (since)) >= (aiot_u32)(interval))

#ifdef __cplusplus
}
#endif

#endif /* AIOT_INTERNAL_H */

/* ==================== aiot_json.c ==================== */
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

/* ==================== aiot.c ==================== */
/*
 * aiot.c - 云智联 AIoT 南向协议核心
 *
 * 协议要点（2026-11 实测）：
 *   TCP 41032: 明文 JSON，一行一帧，'\n' 结尾；连接后先发 lgn。
 *   UDP 40501: 一个数据报一帧；低功耗设备用 lgn_facs 免登录。
 *   MQTT 1883: clientId/username=设备ID，password=设备密码；
 *              发布 south/{product}/{device}/up，
 *              订阅 south/{product}/{device}/down/order 和 down/result。
 *
 * 平台回执可能在同一 TCP 读取中返回多行，本模块按行拆分后逐帧处理。
 */

#include "aiot.h"

#include <string.h>

#define AIOT_DEFAULT_KEEPALIVE_SEC 300u
#define AIOT_DEFAULT_HEARTBEAT_SEC 60u
#define AIOT_LOGIN_TIMEOUT_MS 10000u
#define AIOT_MIN_TX_CAP 256u
#define AIOT_MIN_RX_CAP 256u
#define AIOT_MAX_BACKFILL_POINTS 1000u

/* ========================================================================= */
/* 小工具                                                                    */
/* ========================================================================= */

static aiot_u32 client_now(aiot_client_t *c)
{
    return c->cfg.now_ms(c->cfg.user);
}

static void emit(aiot_client_t *c, aiot_event_t *ev)
{
    if (c->cfg.on_event != NULL) {
        c->cfg.on_event(c->cfg.user, ev);
    }
}

static void emit_simple(aiot_client_t *c, aiot_event_type_t type)
{
    aiot_event_t ev;
    memset(&ev, 0, sizeof ev);
    ev.type = type;
    emit(c, &ev);
}

static int emit_error(aiot_client_t *c, int err)
{
    aiot_event_t ev;
    memset(&ev, 0, sizeof ev);
    ev.type = AIOT_EV_ERROR;
    ev.error = err;
    ev.code = err;
    emit(c, &ev);
    return err;
}

static int copy_bounded(char *dst, size_t cap, const char *src)
{
    size_t n;
    if (src == NULL) {
        if (cap > 0) dst[0] = '\0';
        return 0;
    }
    n = strlen(src);
    if (n >= cap) {
        if (cap > 0) dst[0] = '\0';
        return -1;
    }
    memcpy(dst, src, n + 1);
    return 0;
}

static int make_fid(aiot_client_t *c, const char *fid, char *tmp, size_t cap)
{
    aiot_sb_t sb;

    if (fid != NULL && fid[0] != '\0') {
        if (strlen(fid) > AIOT_EV_FID_MAX) {
            return -1;
        }
        return copy_bounded(tmp, cap, fid);
    }
    c->fid_seq++;
    aiot_sb_init(&sb, tmp, cap);
    aiot_sb_putc(&sb, 'F');
    aiot_sb_u32(&sb, c->fid_seq);
    return aiot_sb_ok(&sb) ? 0 : -1;
}

static int check_state_online(const aiot_client_t *c)
{
    return c->state == AIOT_STATE_ONLINE ? 0 : AIOT_ERR_STATE;
}

static void builder_reset(aiot_client_t *c)
{
    c->builder = 0;
    c->point_count = 0;
    c->first_item = 0;
    c->tx_len = 0;
    c->tx_overflow = 0;
}

/* 在已有 TX 内容后继续追加 */
static void sb_load(aiot_client_t *c, aiot_sb_t *sb)
{
    sb->buf = (char *)c->tx_buf;
    sb->cap = c->tx_cap;
    sb->len = c->tx_len;
    sb->overflow = c->tx_overflow;
}

static void sb_store(aiot_client_t *c, const aiot_sb_t *sb)
{
    c->tx_len = sb->len;
    c->tx_overflow = sb->overflow ? 1 : 0;
}

/* ========================================================================= */
/* 帧构造                                                                    */
/* ========================================================================= */

static int frame_start(aiot_client_t *c, const char *func)
{
    aiot_sb_t sb;

    if (c->builder != 0) {
        return AIOT_ERR_STATE;
    }
    if (func == NULL || func[0] == '\0') {
        return AIOT_ERR_ARG;
    }
    c->tx_len = 0;
    c->tx_overflow = 0;
    aiot_sb_init(&sb, (char *)c->tx_buf, c->tx_cap);

    if (c->cfg.mode != AIOT_MODE_MQTT) {
        aiot_sb_puts(&sb, "{\"top\":\"func\",\"ter\":");
    } else {
        aiot_sb_puts(&sb, "{\"ter\":");
    }
    aiot_sb_json_str(&sb, c->device_id);
    aiot_sb_puts(&sb, ",\"data\":[{\"func\":\"");
    aiot_sb_puts(&sb, func);
    aiot_sb_puts(&sb, "\",\"args\":[");
    sb_store(c, &sb);
    if (!aiot_sb_ok(&sb)) {
        builder_reset(c);
        return emit_error(c, AIOT_ERR_OVERFLOW);
    }
    return 0;
}

static int frame_finish(aiot_client_t *c, const char *fid, const char *ack)
{
    aiot_sb_t sb;
    int rc;

    if (c->builder != 0) {
        return AIOT_ERR_STATE;
    }
    sb_load(c, &sb);
    aiot_sb_putc(&sb, ']'); /* close args */
    if (fid != NULL && fid[0] != '\0') {
        aiot_sb_puts(&sb, ",\"fid\":");
        aiot_sb_json_str(&sb, fid);
    }
    aiot_sb_puts(&sb, "}]"); /* close func object + data array */

    if (c->cfg.mode == AIOT_MODE_UDP && ack != NULL && ack[0] != '\0') {
        aiot_sb_puts(&sb, ",\"ack\":");
        aiot_sb_json_str(&sb, ack);
    }
    aiot_sb_putc(&sb, '}');

    if (c->cfg.mode == AIOT_MODE_TCP) {
        aiot_sb_putc(&sb, '\n');
    }

    if (!aiot_sb_ok(&sb)) {
        builder_reset(c);
        return emit_error(c, AIOT_ERR_OVERFLOW);
    }

    sb_store(c, &sb);
    rc = c->cfg.send(c->cfg.user, c->tx_buf, c->tx_len);
    c->last_tx_ms = client_now(c);
    c->tx_len = 0;
    c->tx_overflow = 0;
    c->builder = 0;
    if (rc != 0) {
        return emit_error(c, AIOT_ERR_IO);
    }
    return 0;
}

static int send_args(aiot_client_t *c, const char *func, const char *fid,
                     const char *args_json, const char *ack)
{
    aiot_sb_t sb;
    size_t len;
    int rc;

    rc = frame_start(c, func);
    if (rc != 0) {
        return rc;
    }
    /* frame_start 已写入 '['，args_json 也带 '['，跳过首字符 */
    len = strlen(args_json);
    sb_load(c, &sb);
    aiot_sb_write(&sb, args_json + 1, len - 2);
    sb_store(c, &sb);
    return frame_finish(c, fid, ack);
}

/* 发送 lgn。允许在 WAIT_LOGIN 状态调用。 */
static int send_login(aiot_client_t *c)
{
    aiot_sb_t sb;
    int rc;

    rc = frame_start(c, "lgn");
    if (rc != 0) {
        return rc;
    }
    sb_load(c, &sb);
    aiot_sb_json_str(&sb, c->password);
    sb_store(c, &sb);
    return frame_finish(c, "L1", NULL);
}

/* ========================================================================= */
/* 初始化                                                                    */
/* ========================================================================= */

int aiot_init(aiot_client_t *client, const aiot_config_t *cfg,
              aiot_u8 *tx_buf, size_t tx_cap,
              aiot_u8 *rx_buf, size_t rx_cap)
{
    aiot_u32 keepalive, heartbeat;

    if (client == NULL || cfg == NULL || tx_buf == NULL || rx_buf == NULL) {
        return AIOT_ERR_ARG;
    }
    if (cfg->send == NULL || cfg->now_ms == NULL) {
        return AIOT_ERR_ARG;
    }
    if (cfg->device_id == NULL || cfg->device_id[0] == '\0' ||
        cfg->password == NULL || cfg->password[0] == '\0') {
        return AIOT_ERR_ARG;
    }
    if (cfg->mode != AIOT_MODE_TCP && cfg->mode != AIOT_MODE_UDP &&
        cfg->mode != AIOT_MODE_MQTT) {
        return AIOT_ERR_ARG;
    }
    if (cfg->mode == AIOT_MODE_MQTT &&
        (cfg->product_id == NULL || cfg->product_id[0] == '\0')) {
        return AIOT_ERR_ARG;
    }
    if (tx_cap < AIOT_MIN_TX_CAP || rx_cap < AIOT_MIN_RX_CAP) {
        return AIOT_ERR_ARG;
    }

    memset(client, 0, sizeof *client);
    client->cfg = *cfg;
    client->tx_buf = tx_buf;
    client->tx_cap = tx_cap;
    client->rx_buf = rx_buf;
    client->rx_cap = rx_cap;
    client->state = AIOT_STATE_IDLE;

    if (copy_bounded(client->device_id, sizeof client->device_id, cfg->device_id) != 0 ||
        copy_bounded(client->password, sizeof client->password, cfg->password) != 0) {
        return AIOT_ERR_ARG;
    }
    if (cfg->product_id != NULL &&
        copy_bounded(client->product_id, sizeof client->product_id, cfg->product_id) != 0) {
        return AIOT_ERR_ARG;
    }

    keepalive = cfg->keepalive_sec ? cfg->keepalive_sec : AIOT_DEFAULT_KEEPALIVE_SEC;
    if (keepalive < 30) {
        keepalive = 30;
    }
    heartbeat = cfg->heartbeat_sec ? cfg->heartbeat_sec : AIOT_DEFAULT_HEARTBEAT_SEC;
    if (heartbeat < 10) {
        heartbeat = 10;
    }
    if (heartbeat >= keepalive) {
        heartbeat = keepalive / 2;
        if (heartbeat < 10) {
            heartbeat = 10;
        }
    }
    client->heartbeat_ms = heartbeat * 1000u;
    client->link_timeout_ms = keepalive * 2000u;
    if (client->link_timeout_ms < 60000u) {
        client->link_timeout_ms = 60000u;
    }

    client->cfg.device_id = client->device_id;
    client->cfg.product_id = client->product_id;
    client->cfg.password = client->password;
    return AIOT_OK;
}

int aiot_client_connected(aiot_client_t *client)
{
    aiot_u32 now;
    int rc = 0;

    if (client == NULL) {
        return AIOT_ERR_ARG;
    }
    now = client_now(client);
    client->state = (client->cfg.mode == AIOT_MODE_TCP)
                        ? AIOT_STATE_WAIT_LOGIN
                        : AIOT_STATE_ONLINE;
    client->rx_len = 0;
    client->tx_len = 0;
    client->tx_overflow = 0;
    client->builder = 0;
    client->last_rx_ms = now;
    client->last_tx_ms = now;
    client->login_deadline_ms = now + AIOT_LOGIN_TIMEOUT_MS;

    emit_simple(client, AIOT_EV_CONNECTED);

    if (client->cfg.mode == AIOT_MODE_TCP) {
        rc = send_login(client);
        if (rc != 0) {
            client->state = AIOT_STATE_ERROR;
            return rc;
        }
    } else if (client->cfg.mode == AIOT_MODE_MQTT &&
               !client->cfg.no_auto_heartbeat) {
        rc = aiot_heartbeat(client);
        if (rc != 0) {
            client->state = AIOT_STATE_ERROR;
            return rc;
        }
    }
    return 0;
}

int aiot_client_disconnected(aiot_client_t *client)
{
    if (client == NULL) {
        return AIOT_ERR_ARG;
    }
    client->state = AIOT_STATE_IDLE;
    client->rx_len = 0;
    builder_reset(client);
    emit_simple(client, AIOT_EV_DISCONNECTED);
    return 0;
}

/* ========================================================================= */
/* 回执/指令解析                                                             */
/* ========================================================================= */

static int token_to_buf(const char *json, const aiot_json_tok_t *toks, int ntok,
                        int idx, char *out, size_t cap)
{
    int rc;

    if (idx < 0) {
        if (cap > 0) out[0] = '\0';
        return 0;
    }
    rc = aiot_json_get_str(json, toks, ntok, idx, out, cap);
    if (rc < 0) {
        if (cap > 0) out[0] = '\0';
        return -1;
    }
    return 0;
}

static void fill_result_event(aiot_client_t *c, const char *json,
                              const aiot_json_tok_t *toks, int ntok,
                              int root, int item, const char *ack)
{
    aiot_event_t ev;
    int t, code = 0;

    memset(&ev, 0, sizeof ev);
    ev.type = AIOT_EV_RESULT;
    ev.result_json = "null";
    ev.result_len = 4;
    copy_bounded(ev.ack, sizeof ev.ack, ack);

    t = aiot_json_obj_get(json, toks, ntok, item, "func");
    token_to_buf(json, toks, ntok, t, ev.func, sizeof ev.func);

    t = aiot_json_obj_get(json, toks, ntok, item, "fid");
    token_to_buf(json, toks, ntok, t, ev.fid, sizeof ev.fid);

    t = aiot_json_obj_get(json, toks, ntok, item, "code");
    if (t >= 0) {
        if (aiot_json_get_i32(json, toks, ntok, t, &code) != 0) {
            code = 0;
        }
    }
    ev.code = code;

    t = aiot_json_obj_get(json, toks, ntok, item, "result");
    if (t >= 0) {
        size_t raw_len = 0;
        const char *raw = aiot_json_raw(json, toks, ntok, t, &raw_len);
        ev.result_json = raw;
        ev.result_len = raw_len;
        if (toks[t].type == AIOT_JSON_STRING) {
            (void)aiot_json_get_str(json, toks, ntok, t,
                                    ev.result_text, sizeof ev.result_text);
        }
    }

    if (strcmp(ev.func, "lgn") == 0) {
        ev.type = AIOT_EV_LOGIN;
        if (code == 0) {
            c->state = AIOT_STATE_ONLINE;
            c->last_rx_ms = client_now(c);
        } else {
            c->state = AIOT_STATE_ERROR;
        }
        emit(c, &ev);
        return;
    }

    emit(c, &ev);
    (void)root;
}

static void handle_result_frame(aiot_client_t *c, const char *json,
                                const aiot_json_tok_t *toks, int ntok,
                                int root, const char *ack)
{
    int data = aiot_json_obj_get(json, toks, ntok, root, "data");

    if (data >= 0 && toks[data].type == AIOT_JSON_ARRAY) {
        int i, count = toks[data].count;
        for (i = 0; i < count; i++) {
            int item = aiot_json_arr_get(json, toks, ntok, data, i);
            if (item >= 0 && toks[item].type == AIOT_JSON_OBJECT) {
                fill_result_event(c, json, toks, ntok, root, item, ack);
            }
        }
    } else {
        /* MQTT down/result 可能是顶层 {"func":...,"code":...} */
        fill_result_event(c, json, toks, ntok, root, root, ack);
    }
}

static void handle_order_frame(aiot_client_t *c, const char *json,
                               const aiot_json_tok_t *toks, int ntok,
                               int root, const char *ack)
{
    int data = aiot_json_obj_get(json, toks, ntok, root, "data");
    int i, count;

    if (data < 0 || toks[data].type != AIOT_JSON_ARRAY) {
        data = -1;
        count = 1;
    } else {
        count = toks[data].count;
    }

    for (i = 0; i < count; i++) {
        aiot_event_t ev;
        int item, t;
        int confirm_rc = 0;

        memset(&ev, 0, sizeof ev);
        ev.type = AIOT_EV_ORDER;
        copy_bounded(ev.ack, sizeof ev.ack, ack);

        if (data >= 0) {
            item = aiot_json_arr_get(json, toks, ntok, data, i);
        } else {
            item = root;
        }
        if (item < 0 || toks[item].type != AIOT_JSON_OBJECT) {
            continue;
        }

        t = aiot_json_obj_get(json, toks, ntok, item, "cmd");
        token_to_buf(json, toks, ntok, t, ev.cmd, sizeof ev.cmd);

        t = aiot_json_obj_get(json, toks, ntok, item, "tra");
        token_to_buf(json, toks, ntok, t, ev.tra, sizeof ev.tra);

        t = aiot_json_obj_get(json, toks, ntok, item, "args");
        if (t >= 0) {
            size_t raw_len = 0;
            const char *raw = aiot_json_raw(json, toks, ntok, t, &raw_len);
            ev.args_json = raw;
            ev.args_len = raw_len;
        } else {
            ev.args_json = "[]";
            ev.args_len = 2;
        }

        if (!c->cfg.no_auto_order_conf && ev.tra[0] != '\0') {
            confirm_rc = aiot_order_confirm(c, ev.tra);
            if (confirm_rc != 0) {
                ev.error = confirm_rc;
            }
        }
        emit(c, &ev);
    }
}

static int handle_frame(aiot_client_t *c, const char *json, size_t len)
{
    aiot_json_tok_t toks[AIOT_JSON_MAX_TOKENS];
    int ntok, root, top;
    char topbuf[12];
    char ack[AIOT_EV_ACK_MAX + 1];

    if (len == 0) {
        return 0;
    }
    ntok = aiot_json_parse(json, len, toks, AIOT_JSON_MAX_TOKENS);
    if (ntok <= 0) {
        return emit_error(c, AIOT_ERR_PARSE);
    }
    root = 0;
    if (toks[root].type != AIOT_JSON_OBJECT) {
        return emit_error(c, AIOT_ERR_PARSE);
    }

    ack[0] = '\0';
    top = aiot_json_obj_get(json, toks, ntok, root, "ack");
    token_to_buf(json, toks, ntok, top, ack, sizeof ack);

    top = aiot_json_obj_get(json, toks, ntok, root, "top");
    if (top >= 0) {
        token_to_buf(json, toks, ntok, top, topbuf, sizeof topbuf);
    } else {
        topbuf[0] = '\0';
    }

    if (strcmp(topbuf, "result") == 0) {
        handle_result_frame(c, json, toks, ntok, root, ack);
        return 0;
    }
    if (strcmp(topbuf, "order") == 0) {
        handle_order_frame(c, json, toks, ntok, root, ack);
        return 0;
    }
    if (topbuf[0] == '\0') {
        /* MQTT down/result 或简化回执 */
        handle_result_frame(c, json, toks, ntok, root, ack);
        return 0;
    }

    return emit_error(c, AIOT_ERR_PARSE);
}

/* ========================================================================= */
/* 接收                                                                      */
/* ========================================================================= */

int aiot_client_rx(aiot_client_t *client, const aiot_u8 *data, size_t len)
{
    size_t start = 0;

    if (client == NULL || (data == NULL && len > 0)) {
        return AIOT_ERR_ARG;
    }
    if (len == 0) {
        return 0;
    }
    if (len > client->rx_cap - client->rx_len - 1) {
        client->rx_len = 0;
        return emit_error(client, AIOT_ERR_OVERFLOW);
    }
    memcpy(client->rx_buf + client->rx_len, data, len);
    client->rx_len += len;
    client->rx_buf[client->rx_len] = '\0';
    client->last_rx_ms = client_now(client);

    while (start < client->rx_len) {
        size_t i = start;
        size_t line_len;
        while (i < client->rx_len && client->rx_buf[i] != '\n') {
            i++;
        }
        if (i >= client->rx_len) {
            break;
        }
        line_len = i - start;
        if (line_len > 0 && client->rx_buf[start + line_len - 1] == '\r') {
            line_len--;
        }
        if (line_len > 0) {
            (void)handle_frame(client, (const char *)client->rx_buf + start, line_len);
        }
        start = i + 1;
    }

    if (start > 0) {
        memmove(client->rx_buf, client->rx_buf + start, client->rx_len - start);
        client->rx_len -= start;
        client->rx_buf[client->rx_len] = '\0';
    }
    return 0;
}

int aiot_client_rx_datagram(aiot_client_t *client, const aiot_u8 *data, size_t len)
{
    if (client == NULL || (data == NULL && len > 0)) {
        return AIOT_ERR_ARG;
    }
    if (len >= client->rx_cap) {
        return emit_error(client, AIOT_ERR_OVERFLOW);
    }
    if (len > 0) {
        memcpy(client->rx_buf, data, len);
    }
    client->rx_buf[len] = '\0';
    client->rx_len = 0;
    client->last_rx_ms = client_now(client);
    while (len > 0 && (client->rx_buf[len - 1] == '\n' ||
                       client->rx_buf[len - 1] == '\r')) {
        len--;
        client->rx_buf[len] = '\0';
    }
    return handle_frame(client, (const char *)client->rx_buf, len);
}

int aiot_mqtt_rx(aiot_client_t *client, const aiot_u8 *payload, size_t len)
{
    if (client == NULL || (payload == NULL && len > 0)) {
        return AIOT_ERR_ARG;
    }
    if (client->cfg.mode != AIOT_MODE_MQTT) {
        return AIOT_ERR_STATE;
    }
    return aiot_client_rx_datagram(client, payload, len);
}

/* ========================================================================= */
/* 周期任务                                                                  */
/* ========================================================================= */

int aiot_client_poll(aiot_client_t *client, aiot_u32 now_ms)
{
    if (client == NULL) {
        return AIOT_ERR_ARG;
    }

    if (client->state == AIOT_STATE_WAIT_LOGIN) {
        if ((aiot_i32)(now_ms - client->login_deadline_ms) >= 0) {
            client->state = AIOT_STATE_ERROR;
            emit_simple(client, AIOT_EV_TIMEOUT);
            return AIOT_ERR_TIMEOUT;
        }
    }

    if (client->state == AIOT_STATE_ONLINE &&
        (client->cfg.mode == AIOT_MODE_TCP || client->cfg.mode == AIOT_MODE_MQTT)) {
        if (!client->cfg.no_auto_heartbeat &&
            AIOT_ELAPSED(now_ms, client->last_tx_ms, client->heartbeat_ms)) {
            int rc = aiot_heartbeat(client);
            if (rc != 0) {
                client->state = AIOT_STATE_ERROR;
                return rc;
            }
        }
        if (client->cfg.mode == AIOT_MODE_TCP &&
            client->last_rx_ms != 0 &&
            AIOT_ELAPSED(now_ms, client->last_rx_ms, client->link_timeout_ms)) {
            client->state = AIOT_STATE_ERROR;
            emit_simple(client, AIOT_EV_TIMEOUT);
            return AIOT_ERR_TIMEOUT;
        }
    }
    return 0;
}

aiot_state_t aiot_client_state(const aiot_client_t *client)
{
    return client != NULL ? client->state : AIOT_STATE_IDLE;
}

aiot_u32 aiot_client_last_rx_ms(const aiot_client_t *client)
{
    return client != NULL ? client->last_rx_ms : 0;
}

/* ========================================================================= */
/* 上行 API                                                                  */
/* ========================================================================= */

int aiot_report_begin(aiot_client_t *client, const char *fid)
{
    int rc;

    if (client == NULL) {
        return AIOT_ERR_ARG;
    }
    if (check_state_online(client) != 0) {
        return AIOT_ERR_STATE;
    }
    if (make_fid(client, fid, client->pending_fid, sizeof client->pending_fid) != 0) {
        return AIOT_ERR_ARG;
    }

    rc = frame_start(client, client->cfg.mode == AIOT_MODE_UDP ? "lgn_facs" : "facs");
    if (rc != 0) {
        return rc;
    }
    if (client->cfg.mode == AIOT_MODE_UDP) {
        aiot_sb_t sb;
        sb_load(client, &sb);
        aiot_sb_json_str(&sb, client->password);
        aiot_sb_putc(&sb, ',');
        aiot_sb_json_str(&sb, client->device_id);
        sb_store(client, &sb);
        if (!aiot_sb_ok(&sb)) {
            builder_reset(client);
            return emit_error(client, AIOT_ERR_OVERFLOW);
        }
        client->first_item = 0;
    } else {
        client->first_item = 1;
    }
    client->builder = 1;
    client->point_count = 0;
    client->total_points = 0;
    return 0;
}

int aiot_report_add(aiot_client_t *client, const char *key, const char *value)
{
    aiot_sb_t sb;

    if (client == NULL || key == NULL || value == NULL) {
        return AIOT_ERR_ARG;
    }
    if (client->builder != 1) {
        return AIOT_ERR_STATE;
    }
    sb_load(client, &sb);
    if (!client->first_item) {
        aiot_sb_putc(&sb, ',');
    }
    aiot_sb_json_str(&sb, key);
    aiot_sb_putc(&sb, ',');
    aiot_sb_json_str(&sb, value);
    sb_store(client, &sb);
    if (!aiot_sb_ok(&sb)) {
        builder_reset(client);
        return emit_error(client, AIOT_ERR_OVERFLOW);
    }
    client->first_item = 0;
    client->point_count++;
    client->total_points++;
    return 0;
}

int aiot_report_end(aiot_client_t *client)
{
    if (client == NULL) {
        return AIOT_ERR_ARG;
    }
    if (client->builder != 1) {
        return AIOT_ERR_STATE;
    }
    if (client->point_count == 0) {
        builder_reset(client);
        return AIOT_ERR_ARG;
    }
    client->builder = 0;
    return frame_finish(client, client->pending_fid, NULL);
}

int aiot_build_abort(aiot_client_t *client)
{
    if (client == NULL) {
        return AIOT_ERR_ARG;
    }
    builder_reset(client);
    return 0;
}

int aiot_report(aiot_client_t *client, const aiot_kv_t *kvs, size_t count,
                const char *fid)
{
    size_t i;
    char fidbuf[AIOT_EV_FID_MAX + 1];
    int rc;

    if (client == NULL || count == 0 || kvs == NULL) {
        return AIOT_ERR_ARG;
    }
    if (check_state_online(client) != 0) {
        return AIOT_ERR_STATE;
    }

    rc = frame_start(client, client->cfg.mode == AIOT_MODE_UDP ? "lgn_facs" : "facs");
    if (rc != 0) {
        return rc;
    }
    {
        aiot_sb_t sb;
        sb_load(client, &sb);
        if (client->cfg.mode == AIOT_MODE_UDP) {
            aiot_sb_json_str(&sb, client->password);
            aiot_sb_putc(&sb, ',');
            aiot_sb_json_str(&sb, client->device_id);
            for (i = 0; i < count; i++) {
                if (kvs[i].key == NULL || kvs[i].value == NULL) {
                    builder_reset(client);
                    return AIOT_ERR_ARG;
                }
                aiot_sb_putc(&sb, ',');
                aiot_sb_json_str(&sb, kvs[i].key);
                aiot_sb_putc(&sb, ',');
                aiot_sb_json_str(&sb, kvs[i].value);
            }
        } else {
            for (i = 0; i < count; i++) {
                if (kvs[i].key == NULL || kvs[i].value == NULL) {
                    builder_reset(client);
                    return AIOT_ERR_ARG;
                }
                if (i > 0) {
                    aiot_sb_putc(&sb, ',');
                }
                aiot_sb_json_str(&sb, kvs[i].key);
                aiot_sb_putc(&sb, ',');
                aiot_sb_json_str(&sb, kvs[i].value);
            }
        }
        sb_store(client, &sb);
        if (!aiot_sb_ok(&sb)) {
            builder_reset(client);
            return emit_error(client, AIOT_ERR_OVERFLOW);
        }
    }
    if (make_fid(client, fid, fidbuf, sizeof fidbuf) != 0) {
        builder_reset(client);
        return AIOT_ERR_ARG;
    }
    return frame_finish(client, fidbuf, NULL);
}

int aiot_backfill_begin(aiot_client_t *client, aiot_u32 timestamp, const char *fid)
{
    aiot_sb_t sb;
    int rc;

    if (client == NULL) {
        return AIOT_ERR_ARG;
    }
    if (check_state_online(client) != 0) {
        return AIOT_ERR_STATE;
    }
    if (client->cfg.mode == AIOT_MODE_UDP) {
        return AIOT_ERR_UNSUPPORTED;
    }
    if (make_fid(client, fid, client->pending_fid, sizeof client->pending_fid) != 0) {
        return AIOT_ERR_ARG;
    }
    rc = frame_start(client, "facs_his");
    if (rc != 0) {
        return rc;
    }
    sb_load(client, &sb);
    aiot_sb_u32(&sb, timestamp);
    sb_store(client, &sb);
    if (!aiot_sb_ok(&sb)) {
        builder_reset(client);
        return emit_error(client, AIOT_ERR_OVERFLOW);
    }
    client->builder = 2;
    client->point_count = 0;
    client->total_points = 0;
    client->first_item = 1; /* 已有一个 timestamp，后续都需要逗号 */
    return 0;
}

int aiot_backfill_add(aiot_client_t *client, const char *key, const char *value)
{
    aiot_sb_t sb;

    if (client == NULL || key == NULL || value == NULL) {
        return AIOT_ERR_ARG;
    }
    if (client->builder != 2) {
        return AIOT_ERR_STATE;
    }
    if (client->total_points >= AIOT_MAX_BACKFILL_POINTS) {
        return AIOT_ERR_ARG;
    }
    sb_load(client, &sb);
    aiot_sb_putc(&sb, ',');
    aiot_sb_json_str(&sb, key);
    aiot_sb_putc(&sb, ',');
    aiot_sb_json_str(&sb, value);
    sb_store(client, &sb);
    if (!aiot_sb_ok(&sb)) {
        builder_reset(client);
        return emit_error(client, AIOT_ERR_OVERFLOW);
    }
    client->first_item = 1;
    client->point_count++;
    client->total_points++;
    return 0;
}

int aiot_backfill_timestamp(aiot_client_t *client, aiot_u32 timestamp)
{
    aiot_sb_t sb;

    if (client == NULL) {
        return AIOT_ERR_ARG;
    }
    if (client->builder != 2) {
        return AIOT_ERR_STATE;
    }
    if (client->point_count == 0) {
        return AIOT_ERR_ARG;
    }
    sb_load(client, &sb);
    aiot_sb_putc(&sb, ',');
    aiot_sb_u32(&sb, timestamp);
    sb_store(client, &sb);
    if (!aiot_sb_ok(&sb)) {
        builder_reset(client);
        return emit_error(client, AIOT_ERR_OVERFLOW);
    }
    client->point_count = 0;
    return 0;
}

int aiot_backfill_end(aiot_client_t *client)
{
    if (client == NULL) {
        return AIOT_ERR_ARG;
    }
    if (client->builder != 2) {
        return AIOT_ERR_STATE;
    }
    if (client->point_count == 0 || client->total_points == 0) {
        builder_reset(client);
        return AIOT_ERR_ARG;
    }
    client->builder = 0;
    return frame_finish(client, client->pending_fid, NULL);
}

int aiot_heartbeat(aiot_client_t *client)
{
    char fidbuf[AIOT_EV_FID_MAX + 1];
    int rc;

    if (client == NULL) {
        return AIOT_ERR_ARG;
    }
    if (client->state != AIOT_STATE_ONLINE) {
        return AIOT_ERR_STATE;
    }
    if (make_fid(client, NULL, fidbuf, sizeof fidbuf) != 0) {
        return AIOT_ERR_ARG;
    }
    rc = frame_start(client, "hear");
    if (rc != 0) {
        return rc;
    }
    return frame_finish(client, fidbuf, NULL);
}

int aiot_request_time(aiot_client_t *client, const char *fid)
{
    char fidbuf[AIOT_EV_FID_MAX + 1];

    if (client == NULL) {
        return AIOT_ERR_ARG;
    }
    if (check_state_online(client) != 0) {
        return AIOT_ERR_STATE;
    }
    if (make_fid(client, fid, fidbuf, sizeof fidbuf) != 0) {
        return AIOT_ERR_ARG;
    }
    return send_args(client, "get_time", fidbuf, "[\"1\"]", NULL);
}

int aiot_request_order(aiot_client_t *client, const char *ack)
{
    char fidbuf[AIOT_EV_FID_MAX + 1];

    if (client == NULL) {
        return AIOT_ERR_ARG;
    }
    if (check_state_online(client) != 0) {
        return AIOT_ERR_STATE;
    }
    if (make_fid(client, NULL, fidbuf, sizeof fidbuf) != 0) {
        return AIOT_ERR_ARG;
    }
    return send_args(client, "get_order", fidbuf, "[]", ack);
}

int aiot_ota_info(aiot_client_t *client, const char *firmware_id, const char *fid)
{
    char fidbuf[AIOT_EV_FID_MAX + 1];
    aiot_sb_t sb;
    int rc;

    if (client == NULL || firmware_id == NULL || firmware_id[0] == '\0') {
        return AIOT_ERR_ARG;
    }
    if (check_state_online(client) != 0) {
        return AIOT_ERR_STATE;
    }
    if (make_fid(client, fid, fidbuf, sizeof fidbuf) != 0) {
        return AIOT_ERR_ARG;
    }
    rc = frame_start(client, "gfinfo");
    if (rc != 0) {
        return rc;
    }
    sb_load(client, &sb);
    aiot_sb_json_str(&sb, firmware_id);
    sb_store(client, &sb);
    return frame_finish(client, fidbuf, NULL);
}

int aiot_ota_get(aiot_client_t *client, const char *firmware_id,
                 aiot_u32 block_no, const char *fid)
{
    char fidbuf[AIOT_EV_FID_MAX + 1];
    aiot_sb_t sb;
    int rc;

    if (client == NULL || firmware_id == NULL || firmware_id[0] == '\0') {
        return AIOT_ERR_ARG;
    }
    if (check_state_online(client) != 0) {
        return AIOT_ERR_STATE;
    }
    if (make_fid(client, fid, fidbuf, sizeof fidbuf) != 0) {
        return AIOT_ERR_ARG;
    }
    rc = frame_start(client, "gfcet");
    if (rc != 0) {
        return rc;
    }
    sb_load(client, &sb);
    aiot_sb_json_str(&sb, firmware_id);
    aiot_sb_putc(&sb, ',');
    aiot_sb_u32(&sb, block_no);
    sb_store(client, &sb);
    return frame_finish(client, fidbuf, NULL);
}

int aiot_udp_wakeup(aiot_client_t *client, const aiot_kv_t *kvs, size_t count,
                    const char *ack)
{
    aiot_sb_t sb;
    size_t i;
    char fidbuf[AIOT_EV_FID_MAX + 1];
    int rc;

    if (client == NULL || (kvs == NULL && count > 0)) {
        return AIOT_ERR_ARG;
    }
    if (client->cfg.mode != AIOT_MODE_UDP) {
        return AIOT_ERR_UNSUPPORTED;
    }
    if (client->state != AIOT_STATE_ONLINE) {
        return AIOT_ERR_STATE;
    }
    if (make_fid(client, NULL, fidbuf, sizeof fidbuf) != 0) {
        return AIOT_ERR_ARG;
    }
    rc = frame_start(client, "lgn_facs");
    if (rc != 0) {
        return rc;
    }
    sb_load(client, &sb);
    aiot_sb_json_str(&sb, client->password);
    aiot_sb_putc(&sb, ',');
    aiot_sb_json_str(&sb, client->device_id);
    for (i = 0; i < count; i++) {
        if (kvs[i].key == NULL || kvs[i].value == NULL) {
            builder_reset(client);
            return AIOT_ERR_ARG;
        }
        aiot_sb_putc(&sb, ',');
        aiot_sb_json_str(&sb, kvs[i].key);
        aiot_sb_putc(&sb, ',');
        aiot_sb_json_str(&sb, kvs[i].value);
    }
    sb_store(client, &sb);
    return frame_finish(client, fidbuf, ack);
}

int aiot_send_func(aiot_client_t *client, const char *func,
                   const char *args_json, const char *fid)
{
    char fidbuf[AIOT_EV_FID_MAX + 1];
    size_t len;

    if (client == NULL || func == NULL || func[0] == '\0' || args_json == NULL) {
        return AIOT_ERR_ARG;
    }
    len = strlen(args_json);
    if (len < 2 || args_json[0] != '[' || args_json[len - 1] != ']') {
        return AIOT_ERR_ARG;
    }
    if (check_state_online(client) != 0) {
        return AIOT_ERR_STATE;
    }
    if (make_fid(client, fid, fidbuf, sizeof fidbuf) != 0) {
        return AIOT_ERR_ARG;
    }
    return send_args(client, func, fidbuf, args_json, NULL);
}

/* ========================================================================= */
/* 下行回执                                                                  */
/* ========================================================================= */

int aiot_order_confirm(aiot_client_t *client, const char *tra)
{
    char fidbuf[AIOT_EV_FID_MAX + 1];
    aiot_sb_t sb;
    int rc;

    if (client == NULL || tra == NULL || tra[0] == '\0') {
        return AIOT_ERR_ARG;
    }
    if (check_state_online(client) != 0) {
        return AIOT_ERR_STATE;
    }
    if (make_fid(client, NULL, fidbuf, sizeof fidbuf) != 0) {
        return AIOT_ERR_ARG;
    }
    rc = frame_start(client, "order_conf");
    if (rc != 0) {
        return rc;
    }
    sb_load(client, &sb);
    aiot_sb_json_str(&sb, tra);
    sb_store(client, &sb);
    return frame_finish(client, fidbuf, NULL);
}

int aiot_order_reply(aiot_client_t *client, const char *tra,
                     const aiot_kv_t *kvs, size_t count)
{
    aiot_sb_t sb;
    size_t i;
    char fidbuf[AIOT_EV_FID_MAX + 1];
    int rc;

    if (client == NULL || tra == NULL || tra[0] == '\0' ||
        (kvs == NULL && count > 0)) {
        return AIOT_ERR_ARG;
    }
    if (check_state_online(client) != 0) {
        return AIOT_ERR_STATE;
    }
    if (make_fid(client, NULL, fidbuf, sizeof fidbuf) != 0) {
        return AIOT_ERR_ARG;
    }
    rc = frame_start(client, "facs_reply");
    if (rc != 0) {
        return rc;
    }
    sb_load(client, &sb);
    aiot_sb_json_str(&sb, tra);
    aiot_sb_putc(&sb, ',');
    aiot_sb_json_str(&sb, client->device_id);
    for (i = 0; i < count; i++) {
        if (kvs[i].key == NULL || kvs[i].value == NULL) {
            builder_reset(client);
            return AIOT_ERR_ARG;
        }
        aiot_sb_putc(&sb, ',');
        aiot_sb_json_str(&sb, kvs[i].key);
        aiot_sb_putc(&sb, ',');
        aiot_sb_json_str(&sb, kvs[i].value);
    }
    sb_store(client, &sb);
    return frame_finish(client, fidbuf, NULL);
}

/* ========================================================================= */
/* MQTT 辅助                                                                 */
/* ========================================================================= */

static int mqtt_topic(const aiot_client_t *client, const char *suffix,
                      char *buf, size_t cap)
{
    aiot_sb_t sb;

    if (client == NULL || suffix == NULL || buf == NULL || cap == 0) {
        return AIOT_ERR_ARG;
    }
    if (client->product_id[0] == '\0') {
        return AIOT_ERR_ARG;
    }
    aiot_sb_init(&sb, buf, cap);
    aiot_sb_puts(&sb, "south/");
    aiot_sb_puts(&sb, client->product_id);
    aiot_sb_putc(&sb, '/');
    aiot_sb_puts(&sb, client->device_id);
    aiot_sb_puts(&sb, suffix);
    return aiot_sb_ok(&sb) ? 0 : AIOT_ERR_NOMEM;
}

int aiot_mqtt_topic_up(const aiot_client_t *client, char *buf, size_t cap)
{
    return mqtt_topic(client, "/up", buf, cap);
}

int aiot_mqtt_topic_down_order(const aiot_client_t *client, char *buf, size_t cap)
{
    return mqtt_topic(client, "/down/order", buf, cap);
}

int aiot_mqtt_topic_down_result(const aiot_client_t *client, char *buf, size_t cap)
{
    return mqtt_topic(client, "/down/result", buf, cap);
}

/* ========================================================================= */
/* 工具                                                                      */
/* ========================================================================= */

/* ========================================================================= */
/* 参数小工具                                                                */
/* ========================================================================= */

static int parse_args(const char *args_json, size_t len,
                      aiot_json_tok_t *toks, int *ntok)
{
    int n;

    if (args_json == NULL || toks == NULL || ntok == NULL) {
        return AIOT_ERR_ARG;
    }
    n = aiot_json_parse(args_json, len, toks, AIOT_JSON_MAX_TOKENS);
    if (n <= 0 || toks[0].type != AIOT_JSON_ARRAY) {
        return AIOT_ERR_PARSE;
    }
    *ntok = n;
    return 0;
}

int aiot_args_count(const char *args_json, size_t len)
{
    aiot_json_tok_t toks[AIOT_JSON_MAX_TOKENS];
    int ntok = 0;
    int rc = parse_args(args_json, len, toks, &ntok);

    if (rc != 0) {
        return rc;
    }
    return (int)toks[0].count;
}

int aiot_args_get_str(const char *args_json, size_t len, int index,
                      char *out, size_t cap)
{
    aiot_json_tok_t toks[AIOT_JSON_MAX_TOKENS];
    int ntok = 0, t;
    int rc = parse_args(args_json, len, toks, &ntok);

    if (rc != 0) {
        return rc;
    }
    if (out == NULL || cap == 0 || index < 0) {
        return AIOT_ERR_ARG;
    }
    t = aiot_json_arr_get(args_json, toks, ntok, 0, index);
    if (t < 0) {
        return AIOT_ERR_ARG;
    }
    if (toks[t].type == AIOT_JSON_STRING) {
        return aiot_json_get_str(args_json, toks, ntok, t, out, cap);
    }
    {
        size_t raw_len = 0;
        const char *raw = aiot_json_raw(args_json, toks, ntok, t, &raw_len);
        if (raw == NULL || raw_len >= cap) {
            return AIOT_ERR_NOMEM;
        }
        memcpy(out, raw, raw_len);
        out[raw_len] = '\0';
        return (int)raw_len;
    }
}

int aiot_args_get_u32(const char *args_json, size_t len, int index,
                      aiot_u32 *out)
{
    aiot_json_tok_t toks[AIOT_JSON_MAX_TOKENS];
    int ntok = 0, t;
    int rc = parse_args(args_json, len, toks, &ntok);

    if (rc != 0) {
        return rc;
    }
    if (out == NULL || index < 0) {
        return AIOT_ERR_ARG;
    }
    t = aiot_json_arr_get(args_json, toks, ntok, 0, index);
    if (t < 0) {
        return AIOT_ERR_ARG;
    }
    if (toks[t].type == AIOT_JSON_NUMBER) {
        return aiot_json_get_u32(args_json, toks, ntok, t, out);
    }
    if (toks[t].type == AIOT_JSON_STRING) {
        char tmp[16];
        int n = aiot_json_get_str(args_json, toks, ntok, t, tmp, sizeof tmp);
        aiot_u32 v = 0;
        int i;
        if (n <= 0) {
            return AIOT_ERR_PARSE;
        }
        for (i = 0; i < n; i++) {
            aiot_u32 digit;
            if (tmp[i] < '0' || tmp[i] > '9') {
                return AIOT_ERR_PARSE;
            }
            digit = (aiot_u32)(tmp[i] - '0');
            if (v > (0xFFFFFFFFu - digit) / 10u) {
                return AIOT_ERR_OVERFLOW;
            }
            v = v * 10u + digit;
        }
        *out = v;
        return 0;
    }
    return AIOT_ERR_ARG;
}

const char *aiot_version(void)
{
    return AIOT_VERSION_STRING;
}

const char *aiot_strerror(int err)
{
    switch (err) {
    case AIOT_OK: return "ok";
    case AIOT_ERR_ARG: return "invalid argument";
    case AIOT_ERR_NOMEM: return "buffer too small";
    case AIOT_ERR_STATE: return "invalid state";
    case AIOT_ERR_IO: return "send failed";
    case AIOT_ERR_PARSE: return "json parse error";
    case AIOT_ERR_OVERFLOW: return "frame overflow";
    case AIOT_ERR_TIMEOUT: return "timeout";
    case AIOT_ERR_AUTH: return "authentication failed";
    case AIOT_ERR_UNSUPPORTED: return "unsupported";
    default: return "unknown error";
    }
}

const char *aiot_state_name(aiot_state_t state)
{
    switch (state) {
    case AIOT_STATE_IDLE: return "idle";
    case AIOT_STATE_WAIT_LOGIN: return "wait_login";
    case AIOT_STATE_ONLINE: return "online";
    case AIOT_STATE_ERROR: return "error";
    default: return "?";
    }
}


