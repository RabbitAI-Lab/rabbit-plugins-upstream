# Keil MDK 示例工程说明

本目录只提供 **接入骨架**，不包含具体 MCU 的启动文件、HAL 库和 WiFi/4G 驱动。原因是每块板子的 BSP 差异太大；复制这些文件到你的工程，补 4 个 BSP 函数即可。

## 文件

| 文件 | 作用 |
|---|---|
| `app_aiot.c` | 初始化、事件回调、断线重连、10 秒上报示例 |
| `../../dist/aiot_sdk.c` | SDK 合并版实现，加入工程 |
| `../../dist/aiot.h` | 公开 API 头文件 |
| `../../dist/aiot_types.h` | C89 定宽类型定义 |

## 添加步骤

1. Keil 工程新建组 `AIoT`；
2. 加入 `dist/aiot_sdk.c` 和 `app_aiot.c`；
3. `Options for Target` → `C/C++` → `Include Paths` 加 `dist`；
4. 选择 C90/C89 模式；
5. 在你的 `main.c` 中调用：

```c
app_aiot_init("WANCD2-0000001008", "设备密码");

/* WiFi/4G 连接成功后 */
app_aiot_on_connected();

/* 串口/模组收到 TCP 数据后 */
app_aiot_on_data(data, len);

/* 连接断开 */
app_aiot_on_closed();

/* while (1) */
app_aiot_loop();
```

## 需要实现的 BSP

```c
int bsp_tcp_send(const aiot_u8 *data, aiot_u32 len);
aiot_u32 bsp_ms(void);
void bsp_tcp_close(void);
int bsp_tcp_connect(const char *host, aiot_u16 port);
```

参考实现见 `docs/03-Keil集成.md` 的 ESP8266 AT 章节。

## 注意

- `g_tx`/`g_rx` 必须是静态/全局，不能是 `app_aiot_init` 的局部变量；
- `bsp_ms()` 必须是 1 ms 单调时钟；
- `bsp_tcp_send()` 必须发送全部 `len` 字节，否则返回非 0；
- 不要把设备密码打印到生产日志；
- 测试环境用 `ciot.yzlkj.com`，生产用 `siot.yzlkj.com`。
