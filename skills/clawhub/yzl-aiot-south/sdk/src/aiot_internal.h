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
