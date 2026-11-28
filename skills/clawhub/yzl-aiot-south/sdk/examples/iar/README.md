# IAR EWARM 示例工程说明

本目录是接入骨架，不包含具体 MCU 的启动文件、链接脚本和 BSP。复制 `app_aiot.c` 到你的 IAR 工程，并把 `dist/aiot_sdk.c` 一起加入。

## 添加步骤

1. IAR 工程右键 `Add` → `Add Files...`，加入 `dist/aiot_sdk.c` 和 `app_aiot.c`；
2. `Project` → `Options` → `C/C++ Compiler` → `Preprocessor`，把 `dist` 加到 include 路径；
3. `Language` 选 C89/C90；
4. 在 `main.c` 中调用 `app_aiot_init()`、`app_aiot_on_connected()`、`app_aiot_on_data()`、`app_aiot_loop()`。

需要 `dist/aiot_sdk.c`、`dist/aiot.h`、`dist/aiot_types.h` 三个文件。

## 需要实现的 BSP

```c
int bsp_tcp_send(const aiot_u8 *data, aiot_u32 len);
aiot_u32 bsp_ms(void);
void bsp_tcp_close(void);
int bsp_tcp_connect(const char *host, aiot_u16 port);
```

BSP 可以是 lwIP、W5500、ESP8266 AT、4G 模组。示例见 `docs/05-移植指南.md`。

## 注意

- `g_tx`/`g_rx` 必须静态分配；
- `bsp_ms()` 返回 1 ms 单调时间；
- 如果使用 FreeRTOS，`aiot_*` 调用放在同一个任务里，或自行加锁；
- IAR 如果启用 `--no_lib`，确认 `memcpy/memmove/memset/strlen/strcmp` 可用；
- 栈至少留 2 KB（`handle_frame` 约 1 KB）。
