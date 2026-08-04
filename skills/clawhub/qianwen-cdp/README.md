# qianwen-cdp

用**原生 Chrome DevTools Protocol** 驱动千问浏览器（`qianwen.exe`），复用真实登录态做办公自动化。

> 为什么不用 xbrowser / agent-browser？因为它们用 `--cdp` 连千问后，驱动「已存在的页面」会静默挂死。本工具改用 browser 级 WebSocket 调 `Target.createTarget` **自建新 tab** 来驱动，完全可控。详见 [SKILL.md](./SKILL.md)。

## 功能

- 确保千问 CDP 实例常驻（真实 profile，登录态保留）
- 新建标签、导航、执行 JS、抓取页面文本/链接/输入框
- 模拟点击、输入文本、截图
- 列出 / 关闭标签

## 快速开始

```bash
git clone <本仓库> qianwen-cdp
cd qianwen-cdp
npm install
```

### 1. 让千问带调试端口

任选其一（或都做）：

**A. 注入快捷方式（Windows，需 pywin32）**

```bash
pip install pywin32
python patch_lnk.py     # 给已有快捷方式追加端口 + 新建「千问(调试).lnk」
```

**B. 注入开机自启项（注册表）**

把 `HKCU\Software\Microsoft\Windows\CurrentVersion\Run\qianwen` 的值改为：

```
"C:\你的路径\QianwenApp\qianwen.exe" --launch-from=loginitem --remote-debugging-port=9666
```

然后**重启千问**（或重启电脑），确认 9666 端口已监听：

```bash
curl http://127.0.0.1:9666/json/version
```

### 2. 驱动

```bash
NODE="你的/node.exe"

# 确保实例在跑
$NODE qw.cjs ensure

# 开一个百度页，拿 targetId
$NODE qw.cjs open "https://www.baidu.com"
# => { "targetId": "xxxx" }

# 在搜索框输入并搜索
$NODE qw.cjs type "<targetId>" "#kw" "机器人 ROS2"
$NODE qw.cjs click "<targetId>" "#su"

# 读结果
$NODE qw.cjs snapshot "<targetId>"
```

## 环境变量

| 变量 | 默认 | 说明 |
|---|---|---|
| `QW_EXE` | 作者机器路径 | 千问可执行文件 |
| `QW_PROFILE` | 作者机器路径 | 千问用户数据目录（登录态） |
| `QW_CDP_PORT` | `9666` | CDP 调试端口 |

clone 后请按需设置环境变量，或改 `qw.cjs` 顶部默认值。

## 命令一览

| 命令 | 说明 |
|---|---|
| `ensure` | 确保 9666 实例在跑（无则拉起真实 profile） |
| `open <url>` | 新建 tab 并导航，输出 targetId |
| `navigate <id> <url>` | 已有 tab 导航 |
| `eval <id> <js>` | 执行 JS |
| `snapshot <id> [selector]` | 取标题/文本/链接/输入框 |
| `click <id> <selector>` | 点击元素 |
| `type <id> <selector> <text>` | 向输入框填文本 |
| `screenshot <id> [out.png]` | 截图 |
| `list` | 列出所有 target |
| `close <id>` | 关闭 tab |
| `relaunch` | 实例挂掉时：taskkill + 重拉 |

## 依赖

- Node.js（脚本用 CommonJS）
- `ws`（已列入 package.json，`npm install` 即可）
- 仅 Windows 的 `patch_lnk.py` 需要 `pywin32`

## 许可证

MIT
