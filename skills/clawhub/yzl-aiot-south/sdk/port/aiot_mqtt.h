/*
 * aiot_mqtt.h - 可选的 MQTT 3.1.1 客户端（QoS0/1，无 TLS）
 *
 * 仅用于没有现成 MQTT 栈的 PC/网关/RTOS 项目。裸机项目通常已经有
 * lwIP MQTT、ESP-IDF MQTT 或模组 AT MQTT，直接把它们收到的 payload
 * 交给 aiot_mqtt_rx() 即可，不需要这个文件。
 */

#ifndef AIOT_MQTT_H
#define AIOT_MQTT_H

#include "aiot.h"
#include "aiot_port.h"

#include <stddef.h>

#ifdef __cplusplus
extern "C" {
#endif

#ifndef AIOT_MQTT_BUF_SIZE
#define AIOT_MQTT_BUF_SIZE 2048
#endif

typedef struct {
    aiot_sock_t *sock;
    aiot_client_t *sdk;

    char client_id[AIOT_DEVICE_ID_MAX + 1];
    char username[AIOT_DEVICE_ID_MAX + 1];
    char password[AIOT_PASSWORD_MAX + 1];
    char topic_up[160];
    char topic_order[160];
    char topic_result[160];

    aiot_u8 tx[AIOT_MQTT_BUF_SIZE];
    aiot_u8 rx[AIOT_MQTT_BUF_SIZE];
    size_t rx_len;

    aiot_u16 next_packet_id;
    aiot_u32 last_tx_ms;
    aiot_u32 last_ping_ms;
    aiot_u8 connected;
    aiot_u8 connecting;
    aiot_u8 last_error;
} aiot_mqtt_t;

/* 绑定已连接的 TCP socket 和 SDK client，并生成三个 topic。 */
int aiot_mqtt_init(aiot_mqtt_t *m, aiot_sock_t *sock, aiot_client_t *sdk);

/* 发送 CONNECT（clientId/username=设备ID，password=设备密码）。 */
int aiot_mqtt_connect(aiot_mqtt_t *m);

/* 驱动收包、CONNACK/SUBACK、PUBLISH、PING。主循环调用。 */
int aiot_mqtt_poll(aiot_mqtt_t *m);

/* 发布到 up topic（QoS1）。可作为 aiot_config_t.send 的底层实现。 */
int aiot_mqtt_publish(aiot_mqtt_t *m, const aiot_u8 *data, size_t len);

int aiot_mqtt_is_connected(const aiot_mqtt_t *m);
int aiot_mqtt_last_error(const aiot_mqtt_t *m);

void aiot_mqtt_close(aiot_mqtt_t *m);

#ifdef __cplusplus
}
#endif

#endif /* AIOT_MQTT_H */
