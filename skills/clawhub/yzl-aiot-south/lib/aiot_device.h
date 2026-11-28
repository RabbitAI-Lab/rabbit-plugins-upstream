/*
 * YZL-AIoT 南向设备接口（C，头文件内联封装）
 *
 * 一个协议功能一个函数，内部转发到 aiot-sdk（dist/aiot_sdk.c）。
 * 用法：
 *     #include "aiot_device.h"
 *     aiot_dev_init(&cli, &cfg, tx, sizeof tx, rx, sizeof rx);
 *     aiot_dev_connected(&cli);
 *     aiot_dev_feed(&cli, buf, n);
 *     aiot_dev_poll(&cli, now_ms());
 *     aiot_dev_report(&cli, kvs, count);
 *
 * 依赖：aiot.h（SDK 头文件）。
 */
#ifndef AIOT_DEVICE_H
#define AIOT_DEVICE_H

#include "aiot.h"

#ifdef __cplusplus
extern "C" {
#endif

/* ---------------------------------------------------------------- 生命周期 */
static inline int aiot_dev_init(aiot_client_t *c, const aiot_config_t *cfg,
                                aiot_u8 *tx, size_t tx_cap, aiot_u8 *rx, size_t rx_cap)
{
    return aiot_init(c, cfg, tx, tx_cap, rx, rx_cap);
}

static inline int aiot_dev_connected(aiot_client_t *c) { return aiot_client_connected(c); }
static inline int aiot_dev_disconnected(aiot_client_t *c) { return aiot_client_disconnected(c); }

/* TCP：喂任意长度字节（SDK 按 '\n' 拆帧）。 */
static inline int aiot_dev_feed(aiot_client_t *c, const aiot_u8 *data, size_t len)
{
    return aiot_client_rx(c, data, len);
}

/* UDP / MQTT：一次一个完整报文。 */
static inline int aiot_dev_feed_datagram(aiot_client_t *c, const aiot_u8 *data, size_t len)
{
    return aiot_client_rx_datagram(c, data, len);
}

static inline int aiot_dev_mqtt_feed(aiot_client_t *c, const aiot_u8 *payload, size_t len)
{
    return aiot_mqtt_rx(c, payload, len);
}

static inline int aiot_dev_poll(aiot_client_t *c, aiot_u32 now_ms)
{
    return aiot_client_poll(c, now_ms);
}

/* ---------------------------------------------------------------- 上行数据 */
/* facs：实时上报多个键值对；fid 可为 NULL。 */
static inline int aiot_dev_report(aiot_client_t *c, const aiot_kv_t *kvs, size_t count)
{
    return aiot_report(c, kvs, count, NULL);
}

/* facs：分步构造（测点数量不定时用）。 */
static inline int aiot_dev_report_begin(aiot_client_t *c, const char *fid)
{
    return aiot_report_begin(c, fid);
}

static inline int aiot_dev_report_add(aiot_client_t *c, const char *key, const char *value)
{
    return aiot_report_add(c, key, value);
}

static inline int aiot_dev_report_end(aiot_client_t *c) { return aiot_report_end(c); }

/* hear：心跳（SDK 默认自动发，需要手动控制时用）。 */
static inline int aiot_dev_heartbeat(aiot_client_t *c) { return aiot_heartbeat(c); }

/* get_time：校时。 */
static inline int aiot_dev_request_time(aiot_client_t *c, const char *fid)
{
    return aiot_request_time(c, fid);
}

/* ---------------------------------------------------------------- 历史补传 */
/* facs_his：ts 为 Unix 秒。begin(ts) → add(key,value)* → timestamp(ts) → ... → end() */
static inline int aiot_dev_backfill_begin(aiot_client_t *c, aiot_u32 ts, const char *fid)
{
    return aiot_backfill_begin(c, ts, fid);
}

static inline int aiot_dev_backfill_add(aiot_client_t *c, const char *key, const char *value)
{
    return aiot_backfill_add(c, key, value);
}

static inline int aiot_dev_backfill_timestamp(aiot_client_t *c, aiot_u32 ts)
{
    return aiot_backfill_timestamp(c, ts);
}

static inline int aiot_dev_backfill_end(aiot_client_t *c) { return aiot_backfill_end(c); }

/* ---------------------------------------------------------------- 指令回执 */
/* order_conf：确认收到（no_auto_order_conf=0 时 SDK 已自动发）。 */
static inline int aiot_dev_order_confirm(aiot_client_t *c, const char *tra)
{
    return aiot_order_confirm(c, tra);
}

/* facs_reply：执行结果 + 实际值；tra 必须原样回传。 */
static inline int aiot_dev_order_reply(aiot_client_t *c, const char *tra,
                                       const aiot_kv_t *kvs, size_t count)
{
    return aiot_order_reply(c, tra, kvs, count);
}

/* ---------------------------------------------------------------- OTA */
static inline int aiot_dev_ota_info(aiot_client_t *c, const char *firmware_id, const char *fid)
{
    return aiot_ota_info(c, firmware_id, fid);
}

static inline int aiot_dev_ota_get(aiot_client_t *c, const char *firmware_id,
                                   aiot_u32 block_no, const char *fid)
{
    return aiot_ota_get(c, firmware_id, block_no, fid);
}

/* ---------------------------------------------------------------- UDP 唤醒 */
/* lgn_facs：密码 + 数据一体上报，无需先登录。 */
static inline int aiot_dev_udp_wakeup(aiot_client_t *c, const aiot_kv_t *kvs, size_t count,
                                      const char *ack)
{
    return aiot_udp_wakeup(c, kvs, count, ack);
}

/* ---------------------------------------------------------------- 通用扩展 */
static inline int aiot_dev_send(aiot_client_t *c, const char *func,
                                const char *args_json, const char *fid)
{
    return aiot_send_func(c, func, args_json, fid);
}

/* ---------------------------------------------------------------- 状态/工具 */
static inline aiot_state_t aiot_dev_state(const aiot_client_t *c)
{
    return aiot_client_state(c);
}

static inline const char *aiot_dev_state_name(aiot_state_t s) { return aiot_state_name(s); }
static inline const char *aiot_dev_strerror(int err) { return aiot_strerror(err); }
static inline const char *aiot_dev_version(void) { return aiot_version(); }

/* ---------------------------------------------------------------- MQTT topic */
static inline int aiot_dev_mqtt_topic_up(const aiot_client_t *c, char *buf, size_t cap)
{
    return aiot_mqtt_topic_up(c, buf, cap);
}

static inline int aiot_dev_mqtt_topic_down_order(const aiot_client_t *c, char *buf, size_t cap)
{
    return aiot_mqtt_topic_down_order(c, buf, cap);
}

static inline int aiot_dev_mqtt_topic_down_result(const aiot_client_t *c, char *buf, size_t cap)
{
    return aiot_mqtt_topic_down_result(c, buf, cap);
}

#ifdef __cplusplus
}
#endif

#endif /* AIOT_DEVICE_H */
