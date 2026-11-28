/*
 * test_all.c - SDK 单元测试（主机运行，不访问网络）
 *
 * 编译:
 *   cc -std=c89 -Iinclude -Isrc tests/test_all.c src/aiot.c src/aiot_json.c -o test_all
 */

#include "aiot.h"
#include "aiot_internal.h"

#include <stdio.h>
#include <string.h>

static int g_checks;
static int g_fails;

#define CHECK(cond)                                                           \
    do {                                                                      \
        g_checks++;                                                           \
        if (!(cond)) {                                                        \
            g_fails++;                                                        \
            printf("FAIL %s:%d: %s\n", __FILE__, __LINE__, #cond);            \
        }                                                                     \
    } while (0)

#define CHECK_STR(actual, expected)                                           \
    do {                                                                      \
        g_checks++;                                                           \
        if (strcmp((actual), (expected)) != 0) {                              \
            g_fails++;                                                        \
            printf("FAIL %s:%d: expected [%s], got [%s]\n",                   \
                   __FILE__, __LINE__, (expected), (actual));                 \
        }                                                                     \
    } while (0)

/* ------------------------------------------------------------------------- */
/* mock 环境                                                                 */
/* ------------------------------------------------------------------------- */

static char g_frame[4096];
static size_t g_frame_len;
static int g_send_count;
static aiot_u32 g_now;
static int g_send_fail;

static int mock_send(void *user, const aiot_u8 *data, size_t len)
{
    (void)user;
    g_send_count++;
    if (g_send_fail) {
        return -1;
    }
    if (len >= sizeof g_frame) {
        len = sizeof g_frame - 1;
    }
    memcpy(g_frame, data, len);
    g_frame[len] = '\0';
    g_frame_len = len;
    return 0;
}

static aiot_u32 mock_now(void *user)
{
    (void)user;
    return g_now;
}

typedef struct {
    aiot_event_type_t type;
    int code;
    int error;
    char func[32];
    char fid[32];
    char cmd[32];
    char tra[48];
    char ack[32];
    char result_text[128];
    char args[512];
} record_t;

static record_t g_events[32];
static int g_event_count;

static void mock_event(void *user, const aiot_event_t *ev)
{
    record_t *r;
    (void)user;
    if (g_event_count >= (int)(sizeof g_events / sizeof g_events[0])) {
        return;
    }
    r = &g_events[g_event_count++];
    memset(r, 0, sizeof *r);
    r->type = ev->type;
    r->code = ev->code;
    r->error = ev->error;
    sprintf(r->func, "%s", ev->func);
    sprintf(r->fid, "%s", ev->fid);
    sprintf(r->cmd, "%s", ev->cmd);
    sprintf(r->tra, "%s", ev->tra);
    sprintf(r->ack, "%s", ev->ack);
    sprintf(r->result_text, "%s", ev->result_text);
    if (ev->args_json != NULL) {
        size_t n = ev->args_len;
        if (n >= sizeof r->args) n = sizeof r->args - 1;
        memcpy(r->args, ev->args_json, n);
        r->args[n] = '\0';
    }
}

static void reset_events(void)
{
    g_event_count = 0;
    memset(g_events, 0, sizeof g_events);
}

static void reset_send(void)
{
    g_send_count = 0;
    g_frame[0] = '\0';
    g_frame_len = 0;
    g_send_fail = 0;
}

static int frame_is_valid_json(void)
{
    aiot_json_tok_t toks[AIOT_JSON_MAX_TOKENS];
    size_t len = g_frame_len;
    if (len > 0 && g_frame[len - 1] == '\n') {
        len--;
    }
    return aiot_json_parse(g_frame, len, toks, AIOT_JSON_MAX_TOKENS) > 0;
}

static int frame_has(const char *needle)
{
    return strstr(g_frame, needle) != NULL;
}

/* ------------------------------------------------------------------------- */
/* JSON                                                                      */
/* ------------------------------------------------------------------------- */

static void test_json(void)
{
    const char *json =
        "{\"top\":\"result\",\"ter\":\"D-1\",\"data\":["
        "{\"func\":\"facs\",\"code\":0,\"result\":null,\"fid\":\"F1\"},"
        "{\"func\":\"get_time\",\"code\":0,\"result\":1792718548,\"fid\":\"T1\"}"
        "],\"ack\":\"99\"}";
    aiot_json_tok_t toks[AIOT_JSON_MAX_TOKENS];
    int n = aiot_json_parse(json, strlen(json), toks, AIOT_JSON_MAX_TOKENS);
    int data, item, v;
    char buf[64];

    CHECK(n > 0);
    CHECK(toks[0].type == AIOT_JSON_OBJECT);
    v = aiot_json_obj_get(json, toks, n, 0, "top");
    CHECK(v >= 0);
    CHECK(aiot_json_is_str(json, toks, n, v, "result"));
    data = aiot_json_obj_get(json, toks, n, 0, "data");
    CHECK(data >= 0 && toks[data].type == AIOT_JSON_ARRAY);
    CHECK(toks[data].count == 2);

    item = aiot_json_arr_get(json, toks, n, data, 0);
    CHECK(item >= 0);
    v = aiot_json_obj_get(json, toks, n, item, "func");
    CHECK(v >= 0);
    CHECK(aiot_json_get_str(json, toks, n, v, buf, sizeof buf) == 4);
    CHECK_STR(buf, "facs");

    item = aiot_json_arr_get(json, toks, n, data, 1);
    CHECK(item >= 0);
    v = aiot_json_obj_get(json, toks, n, item, "result");
    CHECK(v >= 0 && toks[v].type == AIOT_JSON_NUMBER);
    {
        aiot_u32 u = 0;
        CHECK(aiot_json_get_u32(json, toks, n, v, &u) == 0);
        CHECK(u == 1792718548u);
    }

    {
        const char *s = "{\"s\":\"A\\\"B\\\\C\\n\\u4e2d\\u6587\",\"neg\":-123}";
        n = aiot_json_parse(s, strlen(s), toks, AIOT_JSON_MAX_TOKENS);
        CHECK(n > 0);
        v = aiot_json_obj_get(s, toks, n, 0, "s");
        CHECK(v >= 0);
        CHECK(aiot_json_get_str(s, toks, n, v, buf, sizeof buf) > 0);
        CHECK_STR(buf, "A\"B\\C\n\xE4\xB8\xAD\xE6\x96\x87");
        v = aiot_json_obj_get(s, toks, n, 0, "neg");
        {
            aiot_i32 i = 0;
            CHECK(aiot_json_get_i32(s, toks, n, v, &i) == 0);
            CHECK(i == -123);
        }
    }

    CHECK(aiot_json_parse("{\"a\":1} trailing", 16, toks, AIOT_JSON_MAX_TOKENS) < 0);
    CHECK(aiot_json_parse("{\"a\":}", 6, toks, AIOT_JSON_MAX_TOKENS) < 0);
}

/* ------------------------------------------------------------------------- */
/* TCP                                                                       */
/* ------------------------------------------------------------------------- */

static void setup_client(aiot_client_t *cli, aiot_u8 *tx, size_t txcap,
                         aiot_u8 *rx, size_t rxcap, aiot_mode_t mode)
{
    aiot_config_t cfg;
    memset(&cfg, 0, sizeof cfg);
    cfg.device_id = "DEV-1";
    cfg.product_id = "PROD";
    cfg.password = "PWD";
    cfg.mode = mode;
    cfg.send = mock_send;
    cfg.now_ms = mock_now;
    cfg.on_event = mock_event;
    cfg.keepalive_sec = 300;
    cfg.heartbeat_sec = 60;
    CHECK(aiot_init(cli, &cfg, tx, txcap, rx, rxcap) == 0);
}

static void feed(aiot_client_t *cli, const char *s)
{
    CHECK(aiot_client_rx(cli, (const aiot_u8 *)s, strlen(s)) == 0);
}

static void test_tcp(void)
{
    aiot_client_t cli;
    aiot_u8 tx[2048];
    aiot_u8 rx[4096];
    aiot_kv_t one;

    g_now = 1000;
    reset_send();
    reset_events();
    setup_client(&cli, tx, sizeof tx, rx, sizeof rx, AIOT_MODE_TCP);

    CHECK(aiot_client_connected(&cli) == 0);
    CHECK(g_send_count == 1);
    CHECK(frame_has("\"func\":\"lgn\""));
    CHECK(frame_has("\"PWD\""));
    CHECK(frame_is_valid_json());
    CHECK(g_event_count == 1 && g_events[0].type == AIOT_EV_CONNECTED);

    reset_events();
    reset_send();
    feed(&cli,
         "{\"top\":\"result\",\"ter\":\"DEV-1\",\"data\":["
         "{\"func\":\"lgn\",\"code\":0,\"result\":\"tok\",\"fid\":\"L1\"}],"
         "\"ack\":\"\"}\n");
    CHECK(aiot_client_state(&cli) == AIOT_STATE_ONLINE);
    CHECK(g_event_count == 1);
    CHECK(g_events[0].type == AIOT_EV_LOGIN);
    CHECK(g_events[0].code == 0);
    CHECK_STR(g_events[0].fid, "L1");
    CHECK_STR(g_events[0].result_text, "tok");

    {
        aiot_kv_t kv[2];
        kv[0].key = "temp";
        kv[0].value = "25.5";
        kv[1].key = "ver";
        kv[1].value = "A\"B";
        reset_send();
        CHECK(aiot_report(&cli, kv, 2, "F9") == 0);
        CHECK(g_send_count == 1);
        CHECK(frame_has("\"func\":\"facs\""));
        CHECK(frame_has("\"temp\",\"25.5\""));
        CHECK(frame_has("\"ver\",\"A\\\"B\""));
        CHECK(frame_has("\"fid\":\"F9\""));
        CHECK(frame_has("\"top\":\"func\""));
        CHECK(frame_is_valid_json());
    }

    reset_send();
    CHECK(aiot_request_time(&cli, "T9") == 0);
    CHECK(frame_has("\"func\":\"get_time\""));
    CHECK(frame_has("[\"1\"]"));
    CHECK(frame_is_valid_json());

    reset_send();
    CHECK(aiot_heartbeat(&cli) == 0);
    CHECK(frame_has("\"func\":\"hear\""));
    CHECK(frame_is_valid_json());

    reset_send();
    CHECK(aiot_ota_info(&cli, "fw_1a2b3c", "I1") == 0);
    CHECK(frame_has("\"func\":\"gfinfo\""));
    CHECK(frame_has("[\"fw_1a2b3c\"]"));
    CHECK(frame_is_valid_json());

    reset_send();
    CHECK(aiot_ota_get(&cli, "fw_1a2b3c", 7, "I2") == 0);
    CHECK(frame_has("\"func\":\"gfcet\""));
    CHECK(frame_has("[\"fw_1a2b3c\",7]"));
    CHECK(frame_is_valid_json());

    reset_send();
    CHECK(aiot_send_func(&cli, "custom", "[\"x\",1]", "X1") == 0);
    CHECK(frame_has("\"func\":\"custom\""));
    CHECK(frame_has("[\"x\",1]"));
    CHECK(frame_is_valid_json());

    reset_send();
    CHECK(aiot_report_begin(&cli, "B1") == 0);
    CHECK(aiot_report_add(&cli, "k", "v") == 0);
    CHECK(aiot_build_abort(&cli) == 0);
    one.key = "k";
    one.value = "v";
    CHECK(aiot_report(&cli, &one, 1, "B2") == 0);
    CHECK(frame_has("\"fid\":\"B2\""));
    CHECK(frame_is_valid_json());

    reset_send();
    CHECK(aiot_order_confirm(&cli, "T9") == 0);
    CHECK(frame_has("\"func\":\"order_conf\""));
    CHECK(frame_has("[\"T9\"]"));
    CHECK(frame_is_valid_json());

    {
        reset_send();
        CHECK(aiot_backfill_begin(&cli, 1792714948u, "H1") == 0);
        CHECK(aiot_backfill_add(&cli, "wd", "11") == 0);
        CHECK(aiot_backfill_timestamp(&cli, 1792716748u) == 0);
        CHECK(aiot_backfill_add(&cli, "wd", "12") == 0);
        CHECK(aiot_backfill_end(&cli) == 0);
        CHECK(frame_has("\"func\":\"facs_his\""));
        CHECK(frame_has("1792714948,\"wd\",\"11\",1792716748,\"wd\",\"12\""));
        CHECK(frame_is_valid_json());
    }

    reset_events();
    reset_send();
    feed(&cli,
         "{\"top\":\"order\",\"ter\":\"DEV-1\",\"data\":["
         "{\"cmd\":\"set\",\"args\":[\"DEV-1\",\"sw\",\"1\"],\"tra\":\"T1\"}],"
         "\"ack\":\"9\"}\n");
    CHECK(g_send_count == 1);
    CHECK(frame_has("\"func\":\"order_conf\""));
    CHECK(frame_has("\"T1\""));
    CHECK(frame_is_valid_json());
    CHECK(g_event_count == 1);
    CHECK(g_events[0].type == AIOT_EV_ORDER);
    CHECK_STR(g_events[0].cmd, "set");
    CHECK_STR(g_events[0].tra, "T1");
    CHECK_STR(g_events[0].ack, "9");
    CHECK_STR(g_events[0].args, "[\"DEV-1\",\"sw\",\"1\"]");

    {
        aiot_kv_t kv;
        kv.key = "sw";
        kv.value = "1";
        reset_send();
        CHECK(aiot_order_reply(&cli, "T1", &kv, 1) == 0);
        CHECK(frame_has("\"func\":\"facs_reply\""));
        CHECK(frame_has("\"T1\",\"DEV-1\",\"sw\",\"1\""));
        CHECK(frame_is_valid_json());
    }

    /* upfs 大参数（OTA 分片） */
    reset_events();
    reset_send();
    feed(&cli,
         "{\"top\":\"order\",\"data\":[{\"cmd\":\"upfs\","
         "\"args\":[\"0\",\"4\",\"512\",\"A8FF3C\"],\"tra\":\"fw1\"}]}\n");
    CHECK(g_event_count == 1);
    CHECK_STR(g_events[0].cmd, "upfs");
    CHECK_STR(g_events[0].tra, "fw1");
    CHECK(strstr(g_events[0].args, "A8FF3C") != NULL);
    {
        char arg[32];
        aiot_u32 n = 0;
        CHECK(aiot_args_count(g_events[0].args, strlen(g_events[0].args)) == 4);
        CHECK(aiot_args_get_str(g_events[0].args, strlen(g_events[0].args),
                                0, arg, sizeof arg) > 0);
        CHECK_STR(arg, "0");
        CHECK(aiot_args_get_str(g_events[0].args, strlen(g_events[0].args),
                                3, arg, sizeof arg) > 0);
        CHECK_STR(arg, "A8FF3C");
        CHECK(aiot_args_get_u32(g_events[0].args, strlen(g_events[0].args),
                                1, &n) == 0);
        CHECK(n == 4);
    }

    /* 多个结果行一次喂入 */
    reset_events();
    feed(&cli,
         "{\"top\":\"result\",\"data\":[{\"func\":\"facs\",\"code\":0,\"result\":null,\"fid\":\"A\"}]}\n"
         "{\"top\":\"result\",\"data\":[{\"func\":\"hear\",\"code\":0,\"result\":null,\"fid\":\"B\"}]}\n");
    CHECK(g_event_count == 2);
    CHECK_STR(g_events[0].func, "facs");
    CHECK_STR(g_events[1].func, "hear");

    /* 半包 + CRLF */
    reset_events();
    {
        const char *part1 = "{\"top\":\"result\",\"data\":[{\"func\":\"time";
        const char *part2 = "out\",\"code\":0,\"result\":null,\"fid\":\"S1\"}]}\r\n";
        feed(&cli, part1);
        CHECK(g_event_count == 0);
        feed(&cli, part2);
        CHECK(g_event_count == 1);
        CHECK_STR(g_events[0].func, "timeout");
        CHECK_STR(g_events[0].fid, "S1");
    }

    /* 坏密码 */
    g_now = 2000;
    reset_events();
    reset_send();
    setup_client(&cli, tx, sizeof tx, rx, sizeof rx, AIOT_MODE_TCP);
    CHECK(aiot_client_connected(&cli) == 0);
    feed(&cli,
         "{\"top\":\"result\",\"data\":[{\"func\":\"lgn\",\"code\":3,\"result\":\"bad password\",\"fid\":\"L1\"}]}\n");
    CHECK(aiot_client_state(&cli) == AIOT_STATE_ERROR);
    CHECK(g_event_count == 2);
    CHECK(g_events[1].type == AIOT_EV_LOGIN);
    CHECK(g_events[1].code == 3);
}

/* ------------------------------------------------------------------------- */
/* UDP                                                                       */
/* ------------------------------------------------------------------------- */

static void test_udp(void)
{
    aiot_client_t cli;
    aiot_u8 tx[2048];
    aiot_u8 rx[4096];
    aiot_kv_t kv[2];

    g_now = 1000;
    reset_send();
    reset_events();
    setup_client(&cli, tx, sizeof tx, rx, sizeof rx, AIOT_MODE_UDP);
    CHECK(aiot_client_connected(&cli) == 0);
    CHECK(g_send_count == 0);
    CHECK(aiot_client_state(&cli) == AIOT_STATE_ONLINE);

    kv[0].key = "wd";
    kv[0].value = "26.5";
    kv[1].key = "sf";
    kv[1].value = "61";
    CHECK(aiot_report(&cli, kv, 2, "F1") == 0);
    CHECK(g_send_count == 1);
    CHECK(frame_has("\"func\":\"lgn_facs\""));
    CHECK(frame_has("\"PWD\",\"DEV-1\""));
    CHECK(frame_has("\"wd\",\"26.5\""));
    CHECK(frame_has("\"top\":\"func\"")); /* UDP 也带 top */
    CHECK(frame_is_valid_json());

    reset_send();
    CHECK(aiot_udp_wakeup(&cli, kv, 2, "A1") == 0);
    CHECK(frame_has("\"ack\":\"A1\""));
    CHECK(frame_is_valid_json());

    reset_send();
    CHECK(aiot_request_order(&cli, "G1") == 0);
    CHECK(frame_has("\"func\":\"get_order\""));
    CHECK(frame_has("\"ack\":\"G1\""));
    CHECK(frame_is_valid_json());

    reset_events();
    {
        const char *resp =
            "{\"top\":\"result\",\"ter\":\"DEV-1\",\"data\":["
            "{\"func\":\"get_order\",\"code\":0,\"result\":null,\"fid\":\"G1\"}],"
            "\"ack\":\"A1\"}";
        CHECK(aiot_client_rx_datagram(&cli, (const aiot_u8 *)resp, strlen(resp)) == 0);
        CHECK(g_event_count == 1);
        CHECK(g_events[0].type == AIOT_EV_RESULT);
        CHECK_STR(g_events[0].func, "get_order");
        CHECK_STR(g_events[0].ack, "A1");
    }
}

/* ------------------------------------------------------------------------- */
/* MQTT                                                                      */
/* ------------------------------------------------------------------------- */

static void test_mqtt(void)
{
    aiot_client_t cli;
    aiot_u8 tx[2048];
    aiot_u8 rx[4096];
    aiot_config_t cfg;
    aiot_kv_t kv;
    char topic[128];

    memset(&cfg, 0, sizeof cfg);
    cfg.device_id = "DEV-1";
    cfg.product_id = "PROD";
    cfg.password = "PWD";
    cfg.mode = AIOT_MODE_MQTT;
    cfg.send = mock_send;
    cfg.now_ms = mock_now;
    cfg.on_event = mock_event;
    cfg.no_auto_heartbeat = 1;
    g_now = 1000;
    reset_send();
    reset_events();
    CHECK(aiot_init(&cli, &cfg, tx, sizeof tx, rx, sizeof rx) == 0);
    CHECK(aiot_client_connected(&cli) == 0);
    CHECK(g_send_count == 0);

    kv.key = "temp";
    kv.value = "24.5";
    CHECK(aiot_report(&cli, &kv, 1, "F1") == 0);
    CHECK(g_send_count == 1);
    CHECK(frame_has("\"ter\":\"DEV-1\""));
    CHECK(!frame_has("\"top\":\"func\""));
    CHECK(g_frame[g_frame_len - 1] != '\n');
    CHECK(frame_is_valid_json());

    CHECK(aiot_mqtt_topic_up(&cli, topic, sizeof topic) == 0);
    CHECK_STR(topic, "south/PROD/DEV-1/up");
    CHECK(aiot_mqtt_topic_down_order(&cli, topic, sizeof topic) == 0);
    CHECK_STR(topic, "south/PROD/DEV-1/down/order");
    CHECK(aiot_mqtt_topic_down_result(&cli, topic, sizeof topic) == 0);
    CHECK_STR(topic, "south/PROD/DEV-1/down/result");

    reset_events();
    reset_send();
    {
        const char *order =
            "{\"top\":\"order\",\"ter\":\"DEV-1\",\"data\":["
            "{\"cmd\":\"get\",\"args\":[\"DEV-1\",\"temp\"],\"tra\":\"T2\"}]}";
        CHECK(aiot_mqtt_rx(&cli, (const aiot_u8 *)order, strlen(order)) == 0);
        CHECK(g_event_count == 1);
        CHECK(g_events[0].type == AIOT_EV_ORDER);
        CHECK_STR(g_events[0].cmd, "get");
        CHECK_STR(g_events[0].tra, "T2");
        CHECK(g_send_count == 1);
        CHECK(frame_has("\"func\":\"order_conf\""));
        CHECK(!frame_has("\"top\":\"func\""));
    }
}

/* ------------------------------------------------------------------------- */
/* 边界                                                                      */
/* ------------------------------------------------------------------------- */

static void test_limits(void)
{
    aiot_client_t cli;
    aiot_u8 tx[256];
    aiot_u8 rx[256];
    aiot_config_t cfg;

    memset(&cfg, 0, sizeof cfg);
    cfg.device_id = "D";
    cfg.product_id = "P";
    cfg.password = "W";
    cfg.mode = AIOT_MODE_TCP;
    cfg.send = mock_send;
    cfg.now_ms = mock_now;
    cfg.on_event = mock_event;
    CHECK(aiot_init(&cli, &cfg, tx, 32, rx, sizeof rx) == AIOT_ERR_ARG);
    CHECK(aiot_init(&cli, &cfg, tx, sizeof tx, rx, 32) == AIOT_ERR_ARG);

    cfg.mode = AIOT_MODE_MQTT;
    cfg.product_id = NULL;
    CHECK(aiot_init(&cli, &cfg, tx, sizeof tx, rx, sizeof rx) == AIOT_ERR_ARG);

    cfg.product_id = "P";
    cfg.device_id = "0123456789012345678901234567890123";
    CHECK(aiot_init(&cli, &cfg, tx, sizeof tx, rx, sizeof rx) == AIOT_ERR_ARG);

    /* 超长上报应返回 overflow，而不是越界 */
    cfg.device_id = "D";
    g_now = 1;
    reset_send();
    CHECK(aiot_init(&cli, &cfg, tx, sizeof tx, rx, sizeof rx) == 0);
    CHECK(aiot_client_connected(&cli) == 0);
    feed(&cli, "{\"top\":\"result\",\"data\":[{\"func\":\"lgn\",\"code\":0,\"result\":\"\",\"fid\":\"L1\"}]}\n");
    {
        char big[400];
        aiot_kv_t kv;
        memset(big, 'x', sizeof big - 1);
        big[sizeof big - 1] = '\0';
        kv.key = "k";
        kv.value = big;
        CHECK(aiot_report(&cli, &kv, 1, "F1") == AIOT_ERR_OVERFLOW);
        CHECK(aiot_client_state(&cli) == AIOT_STATE_ONLINE);
    }

    /* 断线复位 */
    reset_events();
    CHECK(aiot_client_disconnected(&cli) == 0);
    CHECK(aiot_client_state(&cli) == AIOT_STATE_IDLE);
    CHECK(g_event_count == 1 && g_events[0].type == AIOT_EV_DISCONNECTED);
}

int main(void)
{
    test_json();
    test_tcp();
    test_udp();
    test_mqtt();
    test_limits();

    printf("\n%d checks, %d failures\n", g_checks, g_fails);
    return g_fails ? 1 : 0;
}
