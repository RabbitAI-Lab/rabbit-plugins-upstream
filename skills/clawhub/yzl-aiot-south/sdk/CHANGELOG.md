# Changelog

## 1.0.0 - 2026-11-04

首个可用版本。

### 协议

- TCP 41032：`lgn`、`facs`、`facs_his`、`hear`、`facs_reply`、`order_conf`、`get_time`
- UDP 40501：`lgn_facs`、`get_order`、`get_time`、`ack` 回传
- MQTT 1883：`south/{product}/{device}/up`、`down/order`、`down/result`
- 下行：`set`、`get`、`upfs`
- OTA：`gfinfo`、`gfcet`，以及 `upfs` 下行解析

### SDK

- C89，无 `malloc`，无 OS 依赖
- 可配置 TX/RX 缓冲，调用方静态分配
- 按 `\n` 拆 TCP 帧，支持粘包/半包
- 轻量 JSON 构造器 + 解析器（支持 `\uXXXX`、代理对）
- 自动登录、自动心跳、自动 `order_conf`
- 事件回调：登录、回执、下行、超时、错误
- UDP 模式自动使用 `lgn_facs`
- MQTT payload/topic 辅助
- 可选 MQTT 3.1.1 客户端（QoS0/1，无 TLS）
- POSIX/Windows socket 适配层
- Keil/IAR 接入骨架

### 验证

- 主机单元测试 183 项，0 失败
- 真实平台测试设备验证 TCP/UDP/MQTT 登录、上报、下行闭环


