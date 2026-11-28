# 09 · 用 ML307C（中移 OpenCPU）新建一个 AIoT 接入工程

> 适用：模组 **ML307C**（中移物联网 OpenCPU SDK，`custom/` 下写应用，代码跑在模组里）。
> 本文是「从零建工程 → 接平台 → 编译刷机 → 验证」的完整步骤；参考实现未上机实测，按 §5 的验证流程走一遍再定稿。

---

## 1. 先想清楚：为什么 ML307C 用本 SDK 而不是 MQTT 直写

| 方案 | 谁在做协议 | 适用 |
|---|---|---|
| 中移 SDK 自带 `cm_mqtt` 直连（01 项目 MG1CD1 就是这种） | 自己写主题/信封/OTA/去重 | 已经跑通、只要加业务 |
| **本 SDK（aiot-c-sdk）+ lwIP socket** | SDK 负责 `lgn`/`facs`/`hear`/`order`/OTA 帧 | 新项目、想少写协议、要 TCP 长连接、要历史补传 |

ML307C 的 OpenCPU 里已经有 **lwIP socket**（`lwip/lwip/sockets.h`）和 **CMSIS-RTOS2**（`cm_os.h`），
所以本 SDK 的「两个回调 + 主子循环」模型可以直接落地，**不需要外挂 MCU，也不需要 AT 指令**。

---

## 2. 工程骨架：从 01 项目的 OpenCPU SDK 复制

```text
F:\yzl\12DSH_AGENT\01_工业水库闸门项目_261006\固件_MG1CD1\   ← 模板（中移 ML307C OpenCPU SDK + 已验证业务）
```

复制时**只保留 SDK 骨架**，把 MG1CD1 的业务换掉：

| 目录/文件 | 处理 |
|---|---|
| `include\` `kernel\` `prebuild\` `third-party\` `tools\` `SConscript` `SConstruct` | 原样保留 |
| `examples\` `test\` | 不用可删（调试时留着 `examples\socket`、`examples\mqtt` 对照） |
| `custom\custom_main\` | **换成自己的**（文件名、入口、SConscript 的 `module`） |
| `out\` | 删掉（旧产物） |

> ⚠️ **第一件事：工程放纯 ASCII 路径**。`arelease.exe`（串口整包）和 `FBFMake`（FOTA 打包）在中文/空格路径下
> **静默失败**，连报错都没有。路径如 `D:\ml307c_proj`；放进了中文目录就用目录联接应急：
> `cmd /c mklink /J D:\ml307c_proj "<真实目录>"`，从 `D:\ml307c_proj` 编译。

---

## 3. 放进 aiot-c-sdk 三件套

在工程里新建 `custom\aiot_sdk\`，放本 SDK 的合并版：

```text
custom\aiot_sdk\aiot_sdk.c      ← dist\aiot_sdk.c
custom\aiot_sdk\aiot.h          ← dist\aiot.h
custom\aiot_sdk\aiot_types.h    ← dist\aiot_types.h
```

改 `custom\SConscript`（只改这三处，其余照抄）：

```python
module = 'custom_main'

ram_source_files = [
    'custom_main/src/custom_main.c',
    'aiot_sdk/aiot_sdk.c',            # ← 加这一行
]

private_incs = [
    current_dir + '/custom_main/inc',
    current_dir + '/aiot_sdk',        # ← 加这一行（aiot.h 在这里）
]

cpp_defines = [
    'BUILD_ENV_TEST=%s' % ARGUMENTS.get('env_test', '1'),
    'AIOT_HOST="ciot.yzlkj.com"',            # ← 可选：用宏传环境，省得改源码
    'AIOT_DEV_ID="ML307-0000000001"',        # ← 平台上的设备 ID
    'AIOT_DEV_PWD="设备密码"',                 # ← 平台上的设备密码
]
```

> 单文件 `aiot_sdk.c` 已内含 JSON 与协议，**不要**再把 `src/aiot.c`、`src/aiot_json.c`、`port/aiot_port_posix.c` 加进来。

---

## 4. 写移植层：`custom\aiot_sdk\aiot_port_ml307c.c`（参考实现）

三个要点：**DNS + TCP 连接**、**`send` 回调**、**收包线程里驱动 `poll`**。

```c
#include <string.h>
#include "cm_os.h"
#include "cm_modem.h"
#include "lwip/lwip/sockets.h"
#include "lwip/lwip/netdb.h"
#include "aiot.h"

#ifndef AIOT_HOST
#define AIOT_HOST      "ciot.yzlkj.com"   /* 生产：siot.yzlkj.com */
#endif
#ifndef AIOT_DEV_ID
#define AIOT_DEV_ID    "ML307-0000000001"
#endif
#ifndef AIOT_DEV_PWD
#define AIOT_DEV_PWD   "设备密码"
#endif

#define AIOT_TCP_PORT        41032
#define AIOT_RX_BUF_SIZE     4096
#define AIOT_TICK_MS         5          /* ML307C: 1 tick = 5ms，见 portTICK_PERIOD_MS */

static aiot_client_t s_cli;
static aiot_u8  s_tx[2048];
static aiot_u8  s_rx[AIOT_RX_BUF_SIZE];
static int      s_sock = -1;
static osMutexId_t s_lock;              /* SDK 非线程安全：所有 aiot_* 调用都要串行 */

static void lock(void)   { osMutexAcquire(s_lock, osWaitForever); }
static void unlock(void) { osMutexRelease(s_lock); }

/* ① 发送回调：SDK 里所有上行帧都从这里出去 */
static int port_send(void *user, const aiot_u8 *data, size_t len)
{
    (void)user;
    if (s_sock < 0) return -1;
    return (send(s_sock, data, len, 0) == (int)len) ? 0 : -1;
}

/* ② 毫秒时钟：单调递增、32 位回绕，SDK 能接受 */
static aiot_u32 port_now(void *user)
{
    (void)user;
    return (aiot_u32)osKernelGetTickCount() * AIOT_TICK_MS;
}

/* ③ 事件回调：登录成功上报，收到指令回执 */
static void port_event(void *user, const aiot_event_t *ev)
{
    (void)user;
    switch (ev->type) {
    case AIOT_EV_LOGIN:
        cm_log_printf(0, "[aiot] login code=%ld\n", (long)ev->code);
        if (ev->code == 0) {
            aiot_kv_t kv[] = {{"temp", "25.5"}, {"hum", "60"}};
            aiot_report(&s_cli, kv, 2, "F1");
        }
        break;
    case AIOT_EV_ORDER: {
        /* set: args = [设备ID, 键, 值]；tra 必须原样回传 */
        char key[32] = {0}, val[32] = {0};
        if (aiot_args_get_str(ev->args_json, ev->args_len, 1, key, sizeof key) >= 0 &&
            aiot_args_get_str(ev->args_json, ev->args_len, 2, val, sizeof val) >= 0) {
            cm_log_printf(0, "[aiot] ORDER %s %s=%s\n", ev->cmd, key, val);
            aiot_kv_t kv = {key, val};
            aiot_order_reply(&s_cli, ev->tra, &kv, 1);   /* order_conf 已由 SDK 自动发 */
        }
        break;
    }
    case AIOT_EV_ERROR:
        cm_log_printf(0, "[aiot] error %d\n", (int)ev->error);
        break;
    default:
        break;
    }
}

/* DNS：gethostbyname 在 ML307C 上可用，返回后取第一个地址 */
static int resolve(const char *host, char *out, size_t cap)
{
    struct hostent *h = gethostbyname(host);
    if (!h || !h->h_addr_list || !h->h_addr_list[0]) return -1;
    return inet_ntop(h->h_addrtype, h->h_addr_list[0], out, cap) ? 0 : -1;
}

static int tcp_connect(const char *host, int port)
{
    char ip[64] = {0};
    struct sockaddr_in addr;
    struct in_addr tmp;
    int one = 1;

    if (inet_aton(host, &tmp) == 0) {              /* 不是 IP，就按域名解析 */
        if (resolve(host, ip, sizeof ip) < 0) return -1;
    } else {
        strncpy(ip, host, sizeof ip - 1);
    }

    s_sock = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);
    if (s_sock < 0) return -1;

    memset(&addr, 0, sizeof addr);
    addr.sin_len = sizeof addr;
    addr.sin_family = AF_INET;
    addr.sin_port = htons((uint16_t)port);
    addr.sin_addr.s_addr = inet_addr(ip);

    if (connect(s_sock, (const struct sockaddr *)&addr, sizeof addr) < 0) {
        close(s_sock); s_sock = -1; return -1;
    }
    setsockopt(s_sock, SOL_SOCKET, SO_KEEPALIVE, &one, sizeof one);
    return 0;
}

/* ④ 主线程：等 PDP → 连 → 收包 + poll → 断线重连 */
static void aiot_task(void *arg)
{
    int backoff = 4;
    (void)arg;

    aiot_config_t cfg = {0};
    cfg.device_id     = AIOT_DEV_ID;        /* 宏传进来，≤31 字符 */
    cfg.password      = AIOT_DEV_PWD;       /* ≤63 字符 */
    cfg.mode          = AIOT_MODE_TCP;
    cfg.send          = port_send;
    cfg.now_ms        = port_now;
    cfg.on_event      = port_event;
    cfg.keepalive_sec = 300;
    cfg.heartbeat_sec = 60;                 /* 必须 < keepalive */
    aiot_init(&s_cli, &cfg, s_tx, sizeof s_tx, s_rx, sizeof s_rx);

    for (;;) {
        /* 等网络 */
        while (cm_modem_get_pdp_state(1) != 1) osDelay(200);

        if (tcp_connect(AIOT_HOST, AIOT_TCP_PORT) < 0) {
            cm_log_printf(0, "[aiot] connect fail, retry in %ds\n", backoff);
            osDelay(backoff * 1000 / AIOT_TICK_MS);
            if (backoff < 60) backoff *= 2;
            continue;
        }
        cm_log_printf(0, "[aiot] tcp connected\n");
        lock(); aiot_client_connected(&s_cli); unlock();   /* TCP：SDK 自动发 lgn */
        backoff = 4;

        for (;;) {
            fd_set rfds; struct timeval tv = {0, 100 * 1000};   /* 100ms */
            FD_ZERO(&rfds); FD_SET(s_sock, &rfds);
            if (select(s_sock + 1, &rfds, NULL, NULL, &tv) > 0) {
                int n = recv(s_sock, s_rx, sizeof s_rx, 0);
                if (n <= 0) break;                             /* 断线 */
                lock(); aiot_client_rx(&s_cli, s_rx, (size_t)n); unlock();
            }
            lock(); aiot_client_poll(&s_cli, port_now(NULL)); unlock();
            if (aiot_client_state(&s_cli) == AIOT_STATE_ERROR) break;
        }

        lock(); aiot_client_disconnected(&s_cli); unlock();
        close(s_sock); s_sock = -1;
        cm_log_printf(0, "[aiot] disconnected, reconnect in 3s\n");
        osDelay(3000 / AIOT_TICK_MS);
    }
}
```

启动（放进 `cm_opencpu_entry()`，和 01 项目的入口同一个套路）：

```c
static void aiot_boot(void)
{
    osThreadAttr_t attr = {0};
    s_lock = osMutexNew(NULL);
    attr.name = "aiot_task";
    attr.stack_size = 10 * 1024;      /* lwIP + 解析栈，10KB 起步 */
    attr.priority = osPriorityNormal;
    osThreadNew((osThreadFunc_t)aiot_task, NULL, &attr);
}
```

要点：

- **一条线程跑完所有 `aiot_*`**，外面再包一把 `osMutex`；业务线程要上报时，把数据丢队列，由这条线程发，别直接跨线程调 `aiot_report`。
- `select` 超时设 100ms 左右，正好当 `poll` 的节拍；`poll` 负责心跳与登录/链路超时。
- UDP 模式（40501）不是长连接：改用 `aiot_client_rx_datagram()`，并且 `aiot_udp_wakeup`/`request_order` 有节奏要求（见 SKILL 的「坑」第 4 条）。

---

## 5. 编译 → 刷机 → 验证

```powershell
# 纯 ASCII 路径下
cd D:\ml307c_proj
python -m SCons                      # 或 scons；产物 out\image\ML307C_APP.bin
python -m SCons env_test=0 out\image\ML307C_APP.bin   # 生产环境变体（如果沿用 env 开关）
```

若 `arelease.exe` 报 `open raw image "rd" failed` 或 zip 没生成 → **路径里有中文**，按 §2 处理。

刷机用中移 OpenCPU 的下载工具（串口整包 `out\image\ML307C_APP.zip`），或走平台的 FOTA。

验证顺序（缺一步就别往下走）：

1. 日志出现 `[aiot] tcp connected` → `[aiot] login code=0`；
2. 平台设备变**在线**，遥测里有你上报的键（键名要与平台设施**逐字一致**）；
3. 平台下发 `set`（`[设备ID, sw, 1]`）→ 日志 `[aiot] ORDER set sw=1` → 平台指令状态 `succeeded`；
4. 拔 4G/断网 30s 再恢复 → 自动重连、平台重新在线；
5. 连续跑 2 小时看 `hear` 是否被上报节奏饿死（心跳与上报计数器必须分开）。

---

## 6. ML307C 特有的坑（按踩坑概率排序）

1. **tick 是 5ms**：`osKernelGetTickCount()` 换算成 ms 必须 ×5，`osDelay(100)` 是 500ms 不是 100ms。
2. **必须先等 PDP**：`cm_modem_get_pdp_state(1) == 1` 再 socket；连不上先怀疑网络没起来。
3. **DNS 需要时间**：`gethostbyname` 同步阻塞，放在连接线程里，别放事件回调。
4. **单文件 `aiot_sdk.c` 已含 JSON**：别再链 `src/*.c`，否则重复定义。
5. **`select` 返回 0 是正常超时**，不是错误；返回 -1 且 socket 已关才需要重连。
6. **栈**：lwIP + SDK 解析栈，任务栈 10KB 起步；OTA 的 `upfs` 大包要求 `rx` ≥4096。
7. **明文端口**：41032 无 TLS，公网必须靠 APN/VPN 或网关 TLS 终结。
8. **中文路径**：编译 bin 不受影响，打包/OTA 必失败且无有效报错。

---

## 7. 平台侧配套

- 平台上**建型号 + 设备**，设备 ID 前缀 = 型号段（主题按 ID 的 `-` 前部分切）；设备密码一机一密。
- 遥测键（如 `temp`/`hum`/`sw`）要与平台设施定义**完全一致**，否则页面不显示。
- 测试环境 `ciot.yzlkj.com`、生产 `siot.yzlkj.com`，**两套设备服务器**，刷错环境表现为「设备不存在 / 一直离线」。
- 平台 REST 限流约 10 次/10 秒；设备侧的上报节奏别按秒级压。
