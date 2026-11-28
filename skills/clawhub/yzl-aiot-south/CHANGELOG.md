# 更新日志

## v1.3.0 (2026-11-27) — 自带接口库（C / Python）

- 🧰 新增 `lib/south_client.py`（lgn/facs/hear/get_time/order_conf/order_reply/facs_his/OTA/UDP）
- 🧰 新增 `lib/aiot_device.h`（C 内联封装，每个协议功能一个函数）
- 🖥️ `tool.py` 改用自带库
- 🧪 新增 `tests/`：本地 mock TCP + 13 项自测
- 📄 新增 `lib/README.md`：功能 ↔ 方法 ↔ 函数对照

## v1.2.0 (2026-11-27) — 增加 C / Python 示例

- 📁 新增 `examples/c/minimal_device.c`（SDK 骨架）与 `examples/python`（probe、simulate_device）
- 📝 SKILL.md、README.md 增加示例入口与运行说明
- ⚠️ SDK 协议行为不变

## v1.1.0 (2026-11-27) — 文档重写 + 联调工具

- 📝 **SKILL.md 重写**：按 `yzl-open-api` 的结构统一（平台边界、运行时要求、限频说明、快速集成、协议端口、API 速查、常见坑、验证、安全、版本历史）。
- 🧰 **新增 `tool.py`**：`frames`（标准帧）、`probe`（TCP 41032 登录探测）、`report`（登录后上报）、`check`（固件工程自检）、`check-update`。
- 📄 **补齐包结构**：`README.md`、`CHANGELOG.md`、`skill-card.md`、`_meta.json`、`sync.sh`。
- 📏 **限频口径**：南向链路不适用北向 REST 配额；按心跳/保活设计上报节奏。
- ⚠️ 行为无变化：SDK 源码与协议实现不变。

## v1.0.0 — 南向首版

- 🧩 C89 SDK：TCP 41032 / UDP 40501 / MQTT 1883、`lgn` / `facs` / `hear` / `set` / `get` / `facs_his` / OTA。
- 🧪 183 项主机单测；Keil / IAR / GCC 示例；ML307C OpenCPU 移植指南。
- 📏 资源预算：约 12–18 KB Flash、约 300 B RAM。
