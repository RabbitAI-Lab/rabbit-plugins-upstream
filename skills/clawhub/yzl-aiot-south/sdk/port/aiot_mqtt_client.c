/*
 * aiot_mqtt_client.c - 极简 MQTT 3.1.1 客户端（QoS0/1，无 TLS）
 *
 * 支持:
 *   CONNECT / CONNACK
 *   SUBSCRIBE / SUBACK
 *   PUBLISH QoS0/QoS1 / PUBACK
 *   PINGREQ / PINGRESP
 *   DISCONNECT
 *
 * 不处理: 会话恢复、离线消息、遗嘱、TLS、QoS2、重传。
 * 对设备上报场景足够；需要 TLS 时请换用平台/模组自带的 MQTT 栈。
 */

#include "aiot_mqtt.h"

#include <string.h>

static int copy_str(char *dst, size_t cap, const char *src)
{
    size_t n;
    if (src == NULL || cap == 0) {
        return -1;
    }
    n = strlen(src);
    if (n >= cap) {
        return -1;
    }
    memcpy(dst, src, n + 1);
    return 0;
}

typedef struct {
    aiot_u8 *p;
    size_t cap;
    size_t len;
    int err;
} mbuf_t;

static void mb_init(mbuf_t *b, aiot_u8 *p, size_t cap)
{
    b->p = p;
    b->cap = cap;
    b->len = 0;
    b->err = 0;
}

static void mb_u8(mbuf_t *b, aiot_u8 v)
{
    if (b->err || b->len + 1 > b->cap) {
        b->err = 1;
        return;
    }
    b->p[b->len++] = v;
}

static void mb_u16(mbuf_t *b, aiot_u16 v)
{
    mb_u8(b, (aiot_u8)(v >> 8));
    mb_u8(b, (aiot_u8)(v & 0xFF));
}

static void mb_bytes(mbuf_t *b, const aiot_u8 *p, size_t n)
{
    if (b->err || b->len + n > b->cap) {
        b->err = 1;
        return;
    }
    if (n > 0) {
        memcpy(b->p + b->len, p, n);
        b->len += n;
    }
}

static void mb_str(mbuf_t *b, const char *s)
{
    size_t n = strlen(s);
    if (n > 65535) {
        b->err = 1;
        return;
    }
    mb_u16(b, (aiot_u16)n);
    mb_bytes(b, (const aiot_u8 *)s, n);
}

static size_t enc_remaining(aiot_u8 *p, size_t len)
{
    size_t n = 0;
    do {
        aiot_u8 byte = (aiot_u8)(len % 128u);
        len /= 128u;
        if (len > 0) {
            byte |= 0x80;
        }
        p[n++] = byte;
    } while (len > 0);
    return n;
}

/*
 * body 从 m->tx + 5 开始构造；编码 remaining length 后把 body 前移到
 * 长度字段之后，避免额外缓冲区。
 */
static int send_packet(aiot_mqtt_t *m, aiot_u8 header, size_t body_len)
{
    aiot_u8 *p = m->tx;
    size_t n;
    size_t total;

    if (body_len > sizeof m->tx - 5) {
        m->last_error = 1;
        return -1;
    }
    n = enc_remaining(p + 1, body_len);
    if (n > 4) {
        m->last_error = 1;
        return -1;
    }
    memmove(p + 1 + n, p + 5, body_len);
    p[0] = header;
    total = 1 + n + body_len;
    if (aiot_tcp_send(m->sock, p, total) != 0) {
        m->last_error = 2;
        return -1;
    }
    m->last_tx_ms = aiot_port_now_ms();
    return 0;
}

static int send_subscribe(aiot_mqtt_t *m)
{
    mbuf_t b;
    aiot_u16 pid;

    m->next_packet_id++;
    if (m->next_packet_id == 0) {
        m->next_packet_id = 1;
    }
    pid = m->next_packet_id;

    mb_init(&b, m->tx + 5, sizeof m->tx - 5);
    mb_u16(&b, pid);
    mb_str(&b, m->topic_order);
    mb_u8(&b, 1); /* QoS1 */
    mb_str(&b, m->topic_result);
    mb_u8(&b, 1);
    if (b.err) {
        return -1;
    }
    return send_packet(m, 0x82, b.len);
}

int aiot_mqtt_init(aiot_mqtt_t *m, aiot_sock_t *sock, aiot_client_t *sdk)
{
    if (m == NULL || sock == NULL || sdk == NULL) {
        return AIOT_ERR_ARG;
    }
    memset(m, 0, sizeof *m);
    m->sock = sock;
    m->sdk = sdk;
    m->next_packet_id = 0;

    if (copy_str(m->client_id, sizeof m->client_id, sdk->device_id) != 0 ||
        copy_str(m->username, sizeof m->username, sdk->device_id) != 0 ||
        copy_str(m->password, sizeof m->password, sdk->password) != 0) {
        return AIOT_ERR_ARG;
    }
    if (aiot_mqtt_topic_up(sdk, m->topic_up, sizeof m->topic_up) != 0 ||
        aiot_mqtt_topic_down_order(sdk, m->topic_order, sizeof m->topic_order) != 0 ||
        aiot_mqtt_topic_down_result(sdk, m->topic_result, sizeof m->topic_result) != 0) {
        return AIOT_ERR_NOMEM;
    }
    return 0;
}

int aiot_mqtt_connect(aiot_mqtt_t *m)
{
    mbuf_t b;

    if (m == NULL || m->sock == NULL || !m->sock->opened) {
        return AIOT_ERR_ARG;
    }
    mb_init(&b, m->tx + 5, sizeof m->tx - 5);
    mb_str(&b, "MQTT");
    mb_u8(&b, 4);    /* protocol level 3.1.1 */
    mb_u8(&b, 0xC2); /* clean session + username + password */
    mb_u16(&b, 60);  /* keepalive seconds */
    mb_str(&b, m->client_id);
    mb_str(&b, m->username);
    mb_str(&b, m->password);
    if (b.err) {
        return AIOT_ERR_NOMEM;
    }
    m->rx_len = 0;
    m->connected = 0;
    m->connecting = 1;
    m->last_ping_ms = aiot_port_now_ms();
    if (send_packet(m, 0x10, b.len) != 0) {
        return AIOT_ERR_IO;
    }
    return 0;
}

static void handle_publish(aiot_mqtt_t *m, aiot_u8 header,
                           const aiot_u8 *body, size_t len)
{
    size_t topic_len;
    size_t off;
    aiot_u8 qos = (aiot_u8)((header >> 1) & 0x03);
    aiot_u16 pid = 0;
    const aiot_u8 *payload;
    size_t payload_len;

    if (len < 2) {
        return;
    }
    topic_len = ((size_t)body[0] << 8) | body[1];
    if (len < 2 + topic_len + (qos > 0 ? 2u : 0u)) {
        return;
    }
    off = 2 + topic_len;
    if (qos > 0) {
        pid = (aiot_u16)(((aiot_u16)body[off] << 8) | body[off + 1]);
        off += 2;
    }
    payload = body + off;
    payload_len = len - off;

    if (m->sdk != NULL) {
        (void)aiot_mqtt_rx(m->sdk, payload, payload_len);
    }

    if (qos == 1) {
        mbuf_t b;
        mb_init(&b, m->tx + 5, sizeof m->tx - 5);
        mb_u16(&b, pid);
        if (!b.err) {
            (void)send_packet(m, 0x40, b.len);
        }
    }
}

static void handle_packet(aiot_mqtt_t *m, aiot_u8 header,
                          const aiot_u8 *body, size_t len)
{
    aiot_u8 type = (aiot_u8)(header >> 4);

    switch (type) {
    case 2: /* CONNACK */
        if (len >= 2) {
            if (body[1] == 0) {
                m->connected = 1;
                m->connecting = 0;
                m->last_error = 0;
                (void)send_subscribe(m);
            } else {
                m->connected = 0;
                m->connecting = 0;
                m->last_error = body[1];
            }
        }
        break;
    case 3: /* PUBLISH */
        handle_publish(m, header, body, len);
        break;
    case 4:  /* PUBACK */
    case 9:  /* SUBACK */
    case 13: /* PINGRESP */
        break;
    case 14: /* DISCONNECT */
        m->connected = 0;
        break;
    default:
        break;
    }
}

static int process_rx(aiot_mqtt_t *m)
{
    size_t pos = 0;

    while (m->rx_len - pos >= 2) {
        size_t i = pos + 1;
        size_t rl = 0;
        size_t mul = 1;
        size_t total;
        int complete = 0;

        while (i < m->rx_len) {
            aiot_u8 byte = m->rx[i++];
            rl += (size_t)(byte & 0x7F) * mul;
            if ((byte & 0x80) == 0) {
                complete = 1;
                break;
            }
            mul *= 128;
            if (mul > 128u * 128u * 128u * 128u) {
                m->rx_len = 0;
                m->last_error = 3;
                return -1;
            }
        }
        if (!complete) {
            break;
        }
        total = (i - pos) + rl;
        if (m->rx_len - pos < total) {
            break;
        }
        handle_packet(m, m->rx[pos], m->rx + i, rl);
        pos += total;
    }

    if (pos > 0) {
        memmove(m->rx, m->rx + pos, m->rx_len - pos);
        m->rx_len -= pos;
    }
    if (m->rx_len >= sizeof m->rx) {
        m->rx_len = 0;
        m->last_error = 4;
        return -1;
    }
    return 0;
}

int aiot_mqtt_poll(aiot_mqtt_t *m)
{
    aiot_u8 buf[512];
    int n;

    if (m == NULL || m->sock == NULL || !m->sock->opened) {
        return AIOT_ERR_ARG;
    }
    n = aiot_tcp_recv(m->sock, buf, sizeof buf, 10);
    if (n > 0) {
        if ((size_t)n > sizeof m->rx - m->rx_len) {
            m->rx_len = 0;
            m->last_error = 4;
            return AIOT_ERR_OVERFLOW;
        }
        memcpy(m->rx + m->rx_len, buf, (size_t)n);
        m->rx_len += (size_t)n;
        if (process_rx(m) != 0) {
            return AIOT_ERR_PARSE;
        }
    } else if (n < 0) {
        m->connected = 0;
        return AIOT_ERR_IO;
    }

    if (m->connected &&
        (aiot_u32)(aiot_port_now_ms() - m->last_ping_ms) >= 30000u) {
        if (send_packet(m, 0xC0, 0) != 0) {
            return AIOT_ERR_IO;
        }
        m->last_ping_ms = aiot_port_now_ms();
    }
    return 0;
}

int aiot_mqtt_publish(aiot_mqtt_t *m, const aiot_u8 *data, size_t len)
{
    mbuf_t b;
    aiot_u16 pid;

    if (m == NULL || !m->connected || (data == NULL && len > 0)) {
        return AIOT_ERR_STATE;
    }
    m->next_packet_id++;
    if (m->next_packet_id == 0) {
        m->next_packet_id = 1;
    }
    pid = m->next_packet_id;

    mb_init(&b, m->tx + 5, sizeof m->tx - 5);
    mb_str(&b, m->topic_up);
    mb_u16(&b, pid);
    mb_bytes(&b, data, len);
    if (b.err) {
        return AIOT_ERR_NOMEM;
    }
    return send_packet(m, 0x32, b.len) == 0 ? 0 : AIOT_ERR_IO;
}

int aiot_mqtt_is_connected(const aiot_mqtt_t *m)
{
    return m != NULL && m->connected;
}

int aiot_mqtt_last_error(const aiot_mqtt_t *m)
{
    return m != NULL ? m->last_error : -1;
}

void aiot_mqtt_close(aiot_mqtt_t *m)
{
    if (m == NULL) {
        return;
    }
    if (m->connected) {
        (void)send_packet(m, 0xE0, 0);
    }
    m->connected = 0;
    m->connecting = 0;
}
