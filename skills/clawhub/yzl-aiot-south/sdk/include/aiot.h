/*
 * aiot.h - 云智联 AIoT 平台南向设备接入 SDK (C89)
 *
 * 目标平台: Keil MDK / IAR EWARM / GCC / Clang / MSVC
 * 语言标准: C89（兼容 C90 / C99 / C11 编译器）
 * 依赖: 仅 stddef.h / string.h；类型定义在 aiot_types.h 中（不依赖 stdint.h）
 *
 * 设计原则:
 *   1. 不依赖 malloc/free，不依赖操作系统；
 *   2. 不依赖 printf/snprintf，方便裸机和低资源 MCU；
 *   3. 网络层完全由用户提供 send/now_ms 回调，可接 lwIP、W5500、
 *      ESP8266/4G AT 模组、Linux/Windows socket；
 *   4. 同一份核心同时支持 TCP 长连接、UDP 低功耗、MQTT 三种南向接入方式。
 *
 * 典型用法:
 *   aiot_client_t cli;
 *   aiot_u8 tx[2048], rx[4096];
 *   aiot_config_t cfg = { ... };
 *   aiot_init(&cli, &cfg, tx, sizeof tx, rx, sizeof rx);
 *   // TCP 连接成功后:
 *   aiot_client_connected(&cli);
 *   // socket 收到数据后:
 *   aiot_client_rx(&cli, data, len);
 *   // 主循环:
 *   aiot_client_poll(&cli, now_ms);
 *
 * 详细说明见 docs/ 目录。
 */

#ifndef AIOT_H
#define AIOT_H

#include "aiot_types.h"

#include <stddef.h>

#ifdef __cplusplus
extern "C" {
#endif

#define AIOT_VERSION_MAJOR 1
#define AIOT_VERSION_MINOR 0
#define AIOT_VERSION_PATCH 0
#define AIOT_VERSION_STRING "1.0.0"

/* ------------------------------------------------------------------------- */
/* 基础类型                                                                  */
/* ------------------------------------------------------------------------- */

typedef enum {
    AIOT_OK = 0,
    AIOT_ERR_ARG = -1,       /* 参数非法 */
    AIOT_ERR_NOMEM = -2,     /* 缓冲区不足 */
    AIOT_ERR_STATE = -3,     /* 当前状态不允许该操作 */
    AIOT_ERR_IO = -4,        /* 用户 send 回调返回失败 */
    AIOT_ERR_PARSE = -5,     /* JSON 解析失败 */
    AIOT_ERR_OVERFLOW = -6,  /* 报文超出缓冲区 */
    AIOT_ERR_TIMEOUT = -7,   /* 登录/链路超时 */
    AIOT_ERR_AUTH = -8,      /* 设备密码错误 */
    AIOT_ERR_UNSUPPORTED = -9
} aiot_err_t;

typedef enum {
    AIOT_MODE_TCP = 0,  /* TCP 长连接，默认端口 41032 */
    AIOT_MODE_UDP = 1,  /* UDP 低功耗，默认端口 40501 */
    AIOT_MODE_MQTT = 2  /* MQTT，默认端口 1883 */
} aiot_mode_t;

typedef enum {
    AIOT_STATE_IDLE = 0,     /* 未连接 */
    AIOT_STATE_WAIT_LOGIN,   /* TCP 已连接，等待 lgn 回执 */
    AIOT_STATE_ONLINE,       /* 已登录/已就绪 */
    AIOT_STATE_ERROR         /* 登录失败或链路超时，需重连 */
} aiot_state_t;

typedef enum {
    AIOT_EV_CONNECTED = 0,   /* 调用了 aiot_client_connected */
    AIOT_EV_LOGIN,           /* TCP lgn 回执（code=0 成功） */
    AIOT_EV_RESULT,          /* 任意 func 的平台回执 */
    AIOT_EV_ORDER,           /* 平台下行指令 set/get/upfs */
    AIOT_EV_DISCONNECTED,    /* 调用了 aiot_client_disconnected */
    AIOT_EV_ERROR,           /* 本地错误，见 event.error */
    AIOT_EV_TIMEOUT          /* 登录超时或链路长时间无数据 */
} aiot_event_type_t;

/* 设备 ID / 型号 ID / 密码最大长度（不含结尾 0） */
#define AIOT_DEVICE_ID_MAX 31
#define AIOT_PRODUCT_ID_MAX 31
#define AIOT_PASSWORD_MAX 63

/* 事件内联字符串长度 */
#define AIOT_EV_FUNC_MAX 15
#define AIOT_EV_FID_MAX 23
#define AIOT_EV_CMD_MAX 15
#define AIOT_EV_TRA_MAX 39
#define AIOT_EV_ACK_MAX 23
#define AIOT_EV_TEXT_MAX 95

typedef struct {
    const char *key;
    const char *value; /* 字符串形式；数值也以字符串传入，平台会按测点类型转换 */
} aiot_kv_t;

/*
 * 事件对象只在回调期间有效；args_json/result_json 指向 client 的 RX 缓冲，
 * 回调返回后可能被下一帧覆盖。需要跨回调保存时请自行拷贝。
 */
typedef struct {
    aiot_event_type_t type;
    int code;                 /* result.code；order 事件为 0 */
    int error;                /* AIOT_EV_ERROR 时的 aiot_err_t */
    char func[AIOT_EV_FUNC_MAX + 1];
    char fid[AIOT_EV_FID_MAX + 1];
    char cmd[AIOT_EV_CMD_MAX + 1];
    char tra[AIOT_EV_TRA_MAX + 1];
    char ack[AIOT_EV_ACK_MAX + 1];
    char result_text[AIOT_EV_TEXT_MAX + 1]; /* result 为字符串时解码后的文本 */
    const char *args_json;    /* order.args 原始 JSON 数组，不含结尾 0 */
    size_t args_len;
    const char *result_json;  /* result 原始 JSON（可能是对象/数组/字符串/数字/null） */
    size_t result_len;
} aiot_event_t;

/* ------------------------------------------------------------------------- */
/* 回调                                                                      */
/* ------------------------------------------------------------------------- */

/*
 * 发送数据。TCP 模式收到的是带 '\n' 的完整帧；UDP 模式收到的是一个完整
 * 数据报；MQTT 模式收到的是要发布到 up topic 的 payload（不带 '\n'）。
 * 返回 0 成功，非 0 失败。
 */
typedef int (*aiot_send_fn)(void *user, const aiot_u8 *data, size_t len);

/* 单调递增毫秒时钟，允许 32 位回绕。 */
typedef aiot_u32 (*aiot_now_fn)(void *user);

typedef void (*aiot_event_fn)(void *user, const aiot_event_t *event);

/* ------------------------------------------------------------------------- */
/* 配置与客户端                                                              */
/* ------------------------------------------------------------------------- */

typedef struct {
    const char *device_id;  /* 必填，如 WANCD2-0000001008 */
    const char *product_id; /* MQTT 必填；TCP/UDP 可填 NULL */
    const char *password;   /* 必填，设备详情页“认证密钥” */
    aiot_mode_t mode;

    aiot_send_fn send;      /* 必填 */
    aiot_now_fn now_ms;     /* 必填 */
    aiot_event_fn on_event; /* 可选，但强烈建议 */
    void *user;             /* 原样传给上述回调 */

    /*
     * 保活时间（秒）。平台型号默认 keepalive_sec=300。
     * 0 表示使用 300。
     */
    aiot_u16 keepalive_sec;

    /*
     * 心跳发送周期（秒）。0 表示 keepalive_sec/2，且最小 30 秒。
     * 必须小于 keepalive_sec。
     */
    aiot_u16 heartbeat_sec;

    /*
     * 默认 0：收到 order 后自动先回 order_conf，应用只需执行并调
     *          aiot_order_reply()。
     * 置 1：关闭自动确认，应用自行调 aiot_order_confirm()。
     */
    aiot_u8 no_auto_order_conf;

    /* 默认 0：TCP/MQTT 在线时自动发送 hear 心跳。置 1 关闭。 */
    aiot_u8 no_auto_heartbeat;
} aiot_config_t;

/*
 * 客户端对象。字段仅供 SDK 内部使用，请勿直接修改。
 * 采用公开结构是为了让裸机工程可以静态分配，避免 malloc。
 */
typedef struct aiot_client {
    aiot_config_t cfg;

    aiot_u8 *tx_buf;
    size_t tx_cap;
    aiot_u8 *rx_buf;
    size_t rx_cap;

    size_t rx_len;
    size_t tx_len;
    aiot_u8 tx_overflow;
    aiot_u8 builder;      /* 0=无, 1=facs, 2=facs_his */
    aiot_u16 point_count;
    aiot_u16 total_points;
    aiot_u8 first_item;

    aiot_state_t state;
    aiot_u32 last_rx_ms;
    aiot_u32 last_tx_ms;
    aiot_u32 login_deadline_ms;
    aiot_u32 fid_seq;
    aiot_u32 heartbeat_ms;
    aiot_u32 link_timeout_ms;

    char pending_fid[AIOT_EV_FID_MAX + 1];
    char device_id[AIOT_DEVICE_ID_MAX + 1];
    char product_id[AIOT_PRODUCT_ID_MAX + 1];
    char password[AIOT_PASSWORD_MAX + 1];
} aiot_client_t;

/* ------------------------------------------------------------------------- */
/* 初始化 / 生命周期                                                         */
/* ------------------------------------------------------------------------- */

/*
 * 初始化。tx_cap 建议 >= 512，rx_cap 建议 >= 1024（OTA 场景建议 4096）。
 * device_id/password 会被复制到 client 内部；cfg 中其它指针只保存不复制。
 */
int aiot_init(aiot_client_t *client, const aiot_config_t *cfg,
              aiot_u8 *tx_buf, size_t tx_cap,
              aiot_u8 *rx_buf, size_t rx_cap);

/* TCP: 连接成功后调用，SDK 会发送 lgn。UDP/MQTT: 直接标记为 ONLINE。 */
int aiot_client_connected(aiot_client_t *client);

/* 连接断开时调用，复位 RX 行缓存并回到 IDLE。 */
int aiot_client_disconnected(aiot_client_t *client);

/* TCP 流式数据入口；可一次传入任意长度，SDK 内部按 '\n' 拆帧。 */
int aiot_client_rx(aiot_client_t *client, const aiot_u8 *data, size_t len);

/* UDP 数据报入口；每次传入一个完整 JSON。 */
int aiot_client_rx_datagram(aiot_client_t *client, const aiot_u8 *data, size_t len);

/* 主循环周期调用：心跳、登录超时、链路超时检测。 */
int aiot_client_poll(aiot_client_t *client, aiot_u32 now_ms);

aiot_state_t aiot_client_state(const aiot_client_t *client);
aiot_u32 aiot_client_last_rx_ms(const aiot_client_t *client);

/* ------------------------------------------------------------------------- */
/* 上行数据                                                                  */
/* ------------------------------------------------------------------------- */

/* 实时数据：一次性上报多个键值对。fid 可为 NULL（自动生成）。 */
int aiot_report(aiot_client_t *client, const aiot_kv_t *kvs, size_t count,
                const char *fid);

/*
 * 实时数据分步构造（适合测点数量不定的场景）：
 *   aiot_report_begin(); aiot_report_add(...); ... aiot_report_end();
 * 构造期间不可调用其它发送 API。
 */
int aiot_report_begin(aiot_client_t *client, const char *fid);
int aiot_report_add(aiot_client_t *client, const char *key, const char *value);
int aiot_report_end(aiot_client_t *client);

/* 放弃正在构造的 facs/facs_his 帧，释放构造状态。 */
int aiot_build_abort(aiot_client_t *client);

/*
 * 历史数据补传。一个 facs_his 帧可包含多个时间点，每个时间点多个键值对。
 * 单帧最多 1000 个数据点。
 *   aiot_backfill_begin(ts, fid);
 *   aiot_backfill_add("wd", "25.1");
 *   aiot_backfill_timestamp(ts2);
 *   aiot_backfill_add("wd", "25.2");
 *   aiot_backfill_end();
 */
int aiot_backfill_begin(aiot_client_t *client, aiot_u32 timestamp, const char *fid);
int aiot_backfill_add(aiot_client_t *client, const char *key, const char *value);
int aiot_backfill_timestamp(aiot_client_t *client, aiot_u32 timestamp);
int aiot_backfill_end(aiot_client_t *client);

/* 心跳（hear）。一般由 poll 自动发送，也可手动调用。 */
int aiot_heartbeat(aiot_client_t *client);

/* 校时。结果通过 AIOT_EV_RESULT(func="get_time") 返回。 */
int aiot_request_time(aiot_client_t *client, const char *fid);

/* UDP 低功耗：主动拉取一条挂起指令。ack 可为 NULL。 */
int aiot_request_order(aiot_client_t *client, const char *ack);

/* OTA：查询固件信息 / 获取指定分片。 */
int aiot_ota_info(aiot_client_t *client, const char *firmware_id, const char *fid);
int aiot_ota_get(aiot_client_t *client, const char *firmware_id,
                 aiot_u32 block_no, const char *fid);

/*
 * UDP 低功耗：密码+数据一体上报（lgn_facs），无需先登录。
 * 若只是普通实时上报，可直接用 aiot_report()，UDP 模式下会自动使用 lgn_facs。
 */
int aiot_udp_wakeup(aiot_client_t *client, const aiot_kv_t *kvs, size_t count,
                    const char *ack);

/*
 * 通用扩展：发送任意 func。args_json 必须是合法 JSON 数组文本，
 * 例如 "[\"wd\",\"25.5\"]"。SDK 不校验数组内部结构。
 */
int aiot_send_func(aiot_client_t *client, const char *func,
                   const char *args_json, const char *fid);

/* ------------------------------------------------------------------------- */
/* 下行指令回执                                                              */
/* ------------------------------------------------------------------------- */

/* 仅回 order_conf（收到确认）。no_auto_order_conf=0 时 SDK 已自动发送。 */
int aiot_order_confirm(aiot_client_t *client, const char *tra);

/* 回 facs_reply（执行结果 + 实际值）。执行完指令后调用。 */
int aiot_order_reply(aiot_client_t *client, const char *tra,
                     const aiot_kv_t *kvs, size_t count);

/* ------------------------------------------------------------------------- */
/* MQTT 辅助                                                                 */
/* ------------------------------------------------------------------------- */

/*
 * MQTT 模式下，aiot_config_t.send 应把 payload 发布到
 * south/{product}/{device}/up。
 */
int aiot_mqtt_topic_up(const aiot_client_t *client, char *buf, size_t cap);
int aiot_mqtt_topic_down_order(const aiot_client_t *client, char *buf, size_t cap);
int aiot_mqtt_topic_down_result(const aiot_client_t *client, char *buf, size_t cap);

/*
 * MQTT 收到 down/order 或 down/result 的 payload 后调用。
 * 与 aiot_client_rx 的区别：不需要 '\n'，也不会做 TCP 拆行。
 */
int aiot_mqtt_rx(aiot_client_t *client, const aiot_u8 *payload, size_t len);

/* ------------------------------------------------------------------------- */
/* 工具                                                                      */
/* ------------------------------------------------------------------------- */

/*
 * 解析下行指令的 args_json（例如 set 的 ["DEV","sw","1"]）。
 * 这些函数在内部复制一份 token，不修改输入，失败返回负值。
 */
int aiot_args_count(const char *args_json, size_t len);
int aiot_args_get_str(const char *args_json, size_t len, int index,
                      char *out, size_t cap);
int aiot_args_get_u32(const char *args_json, size_t len, int index,
                      aiot_u32 *out);

const char *aiot_version(void);
const char *aiot_strerror(int err);
const char *aiot_state_name(aiot_state_t state);

#ifdef __cplusplus
}
#endif

#endif /* AIOT_H */
