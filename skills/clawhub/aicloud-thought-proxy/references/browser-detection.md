# 浏览器内核检测方法详解

目标：判定用户默认浏览器是 **Chromium 内核** 还是 **Gecko 内核**，决定使用哪条操控通道（chrome-mcp/BrowserSkill vs GeckoDriver+Marionette）。

优先级：**用户手动指定路径 > 自动检测默认浏览器 > 常见安装路径兜底**。

## 内核判定表（按可执行文件名）

| 可执行文件（小写） | 内核 | 品牌 |
|---|---|---|
| chrome.exe / chromium.exe | chromium | Google Chrome / Chromium |
| msedge.exe | chromium | Microsoft Edge |
| brave.exe / vivaldi.exe / opera.exe | chromium | Brave / Vivaldi / Opera |
| 360se.exe / 360chrome.exe | chromium | 360 安全 / 极速浏览器 |
| qqbrowser.exe / sogouexplorer.exe / ucbrowser.exe | chromium | QQ / 搜狗 / UC 浏览器 |
| firefox.exe | gecko | Mozilla Firefox |
| palemoon.exe / waterfox.exe | gecko | Pale Moon / Waterfox |

## Windows 检测

### 1. 注册表（首选，得到用户实际默认浏览器）

读取 http / https 协议的默认 ProgId：

```
HKEY_CURRENT_USER\Software\Microsoft\Windows\Shell\Associations\UrlAssociations\http\UserChoice
→ ProgId 值
```

ProgId 到可执行文件名的映射（常见）：
- `ChromeHTML` → chrome.exe
- `MSEdgeHTM` → msedge.exe
- `FirefoxURL-<随机串>`（前缀 FirefoxURL）→ firefox.exe
- `360se<...>` → 360se.exe
- `BraveHTML` → brave.exe
- `VivaldiHTM` → vivaldi.exe
- `OperaStable` → opera.exe

得到可执行文件名后，再通过常见安装路径或 `where <exe>` / 注册表 App Paths 定位完整路径：
`HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\<exe>` → 默认值即为完整路径。

### 2. 常见安装路径兜底

```text
C:\Program Files\Google\Chrome\Application\chrome.exe
C:\Program Files (x86)\Google\Chrome\Application\chrome.exe
%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe
C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe
C:\Program Files\Microsoft\Edge\Application\msedge.exe
C:\Program Files\Mozilla Firefox\firefox.exe
C:\Program Files (x86)\Mozilla Firefox\firefox.exe
```

### 3. 手动指定路径

用户给出浏览器可执行文件路径时，直接按文件名查内核判定表，跳过自动检测。

## macOS 检测

1. 默认浏览器：使用 LaunchServices 查询 http 协议 handler：
   ```bash
   /System/Library/Frameworks/CoreServices.framework/Frameworks/LaunchServices.framework/Support/lsregister -dump | grep -i "http"   # 参考
   ```
   或执行 Swift 一行：`osascript -e 'get URL scheme "http" as default browser'`（部分版本可用）。
2. 常见安装路径：
   ```text
   /Applications/Google Chrome.app/Contents/MacOS/Google Chrome
   /Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge
   /Applications/Firefox.app/Contents/MacOS/firefox
   ```
3. 内核判定：文件名含 chrome/edge/brave/opera → chromium；firefox → gecko。

## Linux 检测

1. 默认浏览器（xdg 标准）：
   ```bash
   xdg-settings get default-web-browser   # 输出如 firefox.desktop / google-chrome.desktop / microsoft-edge.desktop
   ```
2. 按 desktop 文件前缀判定：firefox/palemoon → gecko；chrome/edge/brave/chromium/opera → chromium。
3. 常见路径：`/usr/bin/firefox`、`/usr/bin/google-chrome`、`/usr/bin/microsoft-edge`。

## 输出格式

检测脚本统一输出 JSON，字段：

```json
{
  "engine": "chromium | gecko | unknown",
  "browser": "品牌名（如 Google Chrome / Mozilla Firefox）",
  "path": "浏览器可执行文件完整路径（或 null）",
  "method": "registry:ProgId | common-path | manual | xdg-settings | lsregister | unknown",
  "hint": "对应通道提示：chromium → 通道 A；gecko → 通道 B（需 geckodriver）"
}
```

## 判定后动作

- `chromium` → 通道 A：优先 chrome-mcp 连接器，其次 BrowserSkill / agent-browser（见 chromium-automation.md）。
- `gecko` → 通道 B：确认 geckodriver 可用（`geckodriver --version`），不可用则下载安装（见 gecko-automation.md）。
- `unknown` → 停止并请用户手动指定浏览器路径，不要擅自假定。
