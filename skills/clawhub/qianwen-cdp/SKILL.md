---
name: qianwen-cdp
display_name: 千问浏览器原生 CDP 驱动
description: 用原生 Chrome DevTools Protocol 驱动千问浏览器（qianwen.exe），复用真实登录态做办公自动化。当用户要让"千问浏览器"自动打开网页、填表、点击、抓取内容、截图，或提到 xbrowser/agent-browser 驱动千问失败时，使用本技能。
---

# 千问浏览器原生 CDP 驱动

## 为什么不用 xbrowser / agent-browser

**xbrowser（底层 agent-browser）驱动不了千问**。实测 `agent-browser --cdp <port>` 连千问（真实或干净 profile 都试过）后，驱动**已存在的页面 target** 会静默/挂死（空 profile 跑 2m35s 零输出，最终报 `Auto-launch failed ...:9407`）。xb 的 `run.cjs` 对本地浏览器一律传 `--cdp`，所以 **`xb run --browser qianwen` 彻底走不通**，不要浪费时间在这条路上。

## 根因 & 解法（已验证）

- 千问对「外部 CDP 连接」操作**已存在的页面 target**（通义千问桌面页、AI插件页等）一律静默。
- 但用 **browser 级 WebSocket → `Target.createTarget` 自己新建的页面 target 完全可控**（Runtime / DOM / Input 全可用）。
- 因此驱动千问必须「**原生 CDP + 自建新 target**」，绝不用 `--cdp` 连旧实例。

## 安装

```bash
git clone <本仓库> qianwen-cdp
cd qianwen-cdp
npm install          # 安装 ws 依赖
```

`qw.cjs` 的 WebSocket 依赖优先用本地 `node_modules/ws`；若找不到，会回退到 WorkBuddy 自带 xbrowser 里的 ws（兼容原机环境）。

## 配置（环境变量，均可选）

| 变量 | 默认值（示例） | 说明 |
|---|---|---|
| `QW_EXE` | `C:\Users\<你>\AppData\Local\Programs\QianwenApp\qianwen.exe` | 千问可执行文件 |
| `QW_PROFILE` | `C:/Users/<你>/AppData/Local/Qianwen/User Data` | 千问用户数据目录（**登录态/标签页在这里**） |
| `QW_CDP_PORT` | `9666` | CDP 调试端口 |

不设置则使用脚本内的默认值（指向作者机器路径，clone 后请改环境变量或默认值）。

## 让千问默认带端口（一次性）

有两种方式让千问每次启动都开 CDP 端口：

1. **快捷方式注入**（覆盖桌面/任务栏/开始菜单启动）：`python patch_lnk.py`（需 `pip install pywin32`，仅 Windows）。
2. **注册表自启项注入**（覆盖开机自启）：把 `HKCU\Software\Microsoft\Windows\CurrentVersion\Run\qianwen` 的值追加 ` --remote-debugging-port=9666`。

端口就绪后，千问实例常驻，小虾随时 `qw.cjs ensure` 连上即驱动。

## 工具

`qw.cjs`。调用示例（用任意 node，推荐 managed node）：

```
NODE="你的/node.exe"
$NODE qw.cjs ensure                                  # 确保 9666 实例在跑（真实 profile）
$NODE qw.cjs open "https://www.baidu.com"            # 新建 tab 并导航，输出 targetId
$NODE qw.cjs navigate <id> "https://..."             # 已有 tab 导航
$NODE qw.cjs eval <id> "document.title"              # 执行 JS
$NODE qw.cjs snapshot <id> [css选择器]               # 取标题/文本/链接/输入框
$NODE qw.cjs click <id> "#su"                         # 点击元素（按坐标派发鼠标事件）
$NODE qw.cjs type <id> "#kw" "机器人 ROS2"            # 向输入框填入文本
$NODE qw.cjs screenshot <id> [out.png]               # 截图
$NODE qw.cjs list                                    # 列出所有 target
$NODE qw.cjs close <id>                              # 关闭 tab
$NODE qw.cjs relaunch                                # 实例挂掉时：taskkill + 重拉
```

每个命令都是独立进程，连接到**常驻的千问 CDP 实例**操作，所以可多次调用串起多步自动化。

## 关键常量

- 千问 exe：千问浏览器（阿里 Qwen AI 浏览器，Chromium 内核）
- 真实 profile：`QW_PROFILE`（**登录态/标签页在这里**，驱动走的也是这个实例）
- CDP 固定端口：`9666`

## 已验证的端到端能力

open 百度 → type 搜索框 → click 搜索 → 搜索结果正文读出 ✅。即「开页 + 输入 + 点击 + 读内容」真实交互全通。

## 坑（必记）

1. **必须建新 target**：永远用 `open`/`Target.createTarget` 开新 tab，别去驱动千问自带的桌面页（静默）。
2. **实例挂掉恢复**：千问主进程可被 `Stop-Process -Force` 杀掉，但 `WpkService` 孤儿进程（`--type=utility`，引用真实 profile）可能杀不掉。它们不占主 SingletonLock，新主实例仍能起，只是堆积会拖慢冷启动。恢复用 `qw.cjs relaunch`。
3. **路径正斜杠**：千问对 `--user-data-dir` 反斜杠路径会秒退，必须正斜杠（脚本内已处理）。
4. **强制窗口模式**：千问无头不稳定，必须 headed（脚本内已默认）。
5. 登录态由真实 profile 保留 → 自动化时**就是本人已登录的千问**，对外操作（发消息/发帖）仍遵循"先问再动"。

## 何时用

用户要在千问里做自动操作（查资料、填表、抓页面、定时任务等），且要求保留登录态。直接调 `qw.cjs`，不要走 xbrowser。
