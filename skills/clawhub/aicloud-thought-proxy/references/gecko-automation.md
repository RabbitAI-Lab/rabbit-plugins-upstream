# Gecko 内核浏览器操控指南（通道 B：GeckoDriver + Marionette）

适用于 Mozilla Firefox（以及 Pale Moon / Waterfox 等 Gecko 内核浏览器）。

## 原理

- Firefox 内置 **Marionette** 自动化协议（远程调试 / 自动化服务）。
- **geckodriver** 是 Mozilla 官方的翻译层：把标准 WebDriver HTTP 协议翻译成 Marionette 命令。
- 因此只要拿到 geckodriver，就能用任何语言的 HTTP 客户端驱动 Firefox，无需额外安装浏览器插件。

## 0. 前置检查

```bash
geckodriver --version    # 检查是否已安装
```

未安装时（**先经用户同意**再安装，流程见 SKILL.md 阶段 1.5 与 `references/tool-installation.md`）：

- Agent 侧自动安装：从 https://github.com/mozilla/geckodriver/releases 下载当前平台最新 zip，解压后将 `geckodriver` 放入 PATH（如 `~/bin`），验证 `geckodriver --version`。
- 或用 Python 安装：`pip install selenium`（selenium 4 内置 Selenium Manager，可自动下载 geckodriver 与 Firefox，需联网）。
- 浏览器侧：Firefox 无需装插件，保持正常打开即可；若弹出"是否允许自动化控制"，请用户点"允许"。

## 1. 关键：保留用户登录态

selenium / 原生驱动默认使用**全新临时 profile**，登录态会丢失。必须复用用户自己的 Firefox profile：

- 路径通常在 `%APPDATA%\Mozilla\Firefox\Profiles\*.default-release`（Windows）。
- selenium 指定方式：
  ```python
  options = webdriver.FirefoxOptions()
  options.profile = "<profile目录绝对路径>"   # 或 options.add_argument("-profile <路径>")
  ```
- 纯 HTTP 方式：`moz:firefoxOptions` 里带 `args: ["-profile", "<路径>"]`。
- 若复用 profile 失败或用户不提供，则正常驱动并在打开网页版 AI 后提示用户手动登录（与本技能阶段 3 一致）。

## 2. 方案一：selenium（推荐，代码短）

```python
# pip install selenium
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service

options = webdriver.FirefoxOptions()
# 可选：复用用户 profile 保留登录态
# options.profile = r"C:\Users\<用户名>\AppData\Roaming\Mozilla\Firefox\Profiles\xxxx.default-release"
# options.add_argument("--headless")  # 需要无界面时再加

driver = webdriver.Firefox(service=Service("geckodriver"), options=options)
try:
    driver.get("https://chat.deepseek.com")   # 换成目标品牌 URL
    time.sleep(3)
    print(driver.title)
    print(driver.find_element(By.TAG_NAME, "body").text[:2000])   # 读取页面纯文本
    # 定位输入框并发送消息
    # box = driver.find_element(By.CSS_SELECTOR, "textarea, [contenteditable='true']")
    # box.send_keys("消息内容")
    # box.send_keys("\n")  # 或找发送按钮 click()
    # time.sleep(8)        # 等待 AI 回复
    # print(driver.find_element(By.TAG_NAME, "body").text[-3000:])  # 读取回复尾部
    # driver.save_screenshot("page.png")   # 截图检查
finally:
    driver.quit()
```

## 3. 方案二：纯 HTTP 调用 geckodriver（零依赖，无需 pip 安装）

geckodriver 提供 `http://localhost:<port>` 的 WebDriver REST API。核心端点：

| 端点 | 用途 |
|---|---|
| `POST /session` | 创建会话（Body 带 `capabilities`） |
| `POST /session/{id}/url` | 导航到 URL |
| `GET /session/{id}/title` | 读标题 |
| `POST /session/{id}/execute/sync` | 执行 JS（读取/滚动页面、点按钮） |
| `POST /session/{id}/element` | 查找元素（`{"using":"css selector","value":"..."}`） |
| `POST /session/{id}/element/{el}/click` | 点击元素 |
| `POST /session/{id}/element/{el}/value` | 输入文本 |
| `GET /session/{id}/screenshot` | 截图（base64） |
| `DELETE /session/{id}` | 关闭会话 |

Python 示例（仅标准库 urllib）：

```python
import json, time, urllib.request

GECKODRIVER_PORT = 9515
BASE = f"http://127.0.0.1:{GECKODRIVER_PORT}"

def req(method, path, body=None):
    data = json.dumps(body).encode() if body is not None else None
    r = urllib.request.Request(BASE + path, data=data, method=method)
    r.add_header("Content-Type", "application/json")
    with urllib.request.urlopen(r, timeout=30) as resp:
        return json.loads(resp.read().decode())

# 1) 创建会话（复用 profile 时在 moz:firefoxOptions.args 里加 ["-profile", "<路径>"]）
caps = {
    "capabilities": {
        "alwaysMatch": {
            "browserName": "firefox",
            # "moz:firefoxOptions": {"args": ["-profile", r"C:\...\default-release"]},
        }
    }
}
sid = req("POST", "/session", caps)["value"]["sessionId"]

try:
    # 2) 打开网页版 AI
    req("POST", f"/session/{sid}/url", {"url": "https://chat.deepseek.com"})
    time.sleep(4)

    # 3) 读取页面纯文本（前 2000 字，判断登录/模式状态）
    text = req("POST", f"/session/{sid}/execute/sync",
               {"script": "return document.body.innerText.slice(0,2000);", "args": []})
    print(text["value"])

    # 4) 查找输入框并输入（先执行 JS 找候选选择器）
    box = req("POST", f"/session/{sid}/execute/sync",
              {"script": "const el=document.querySelector('textarea,[contenteditable=\"true\"]');"
                         "return el?{tag:el.tagName,text:el.innerText.slice(0,100)}:null;", "args": []})
    print("input box:", box["value"])

    # 5) 输入消息（contenteditable 用 JS 注入 + 派发 input 事件）
    msg = "我是来自用户电脑中的 AI agent，你负责规划步骤 / 编写代码 / 逻辑推理……"
    req("POST", f"/session/{sid}/execute/sync",
        {"script": "const el=document.querySelector('textarea,[contenteditable=\"true\"]');"
                   "if(!el)return false;"
                   "const setter=Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype,'value');"
                   "el.value=arguments[0];el.dispatchEvent(new Event('input',{bubbles:true}));return true;",
         "args": [msg]})

    # 6) 点发送（尝试常见按钮文案）
    req("POST", f"/session/{sid}/execute/sync",
        {"script": "const b=[...document.querySelectorAll('button,div[role=button]')]"
                   ".find(x=>x.innerText&&x.innerText.trim().includes('发送'));if(b){b.click();return true}return false;",
         "args": []})
    time.sleep(10)

    # 7) 读回复（滚动到底后取全文尾部）
    req("POST", f"/session/{sid}/execute/sync",
        {"script": "window.scrollTo(0,document.body.scrollHeight);return true;", "args": []})
    reply = req("POST", f"/session/{sid}/execute/sync",
                {"script": "return document.body.innerText.slice(-4000);", "args": []})
    print("reply:", reply["value"])
finally:
    req("DELETE", f"/session/{sid}")
```

> 提示：不同站点的输入框 / 发送按钮结构不同，先用 `execute/sync` 探查页面再操作；若 JS 注入 value 不触发响应式更新，改为先 `click` 聚焦再派发 `InputEvent`（`new Event('input',{bubbles:true})` 通常足够）。

## 4. 启动 geckodriver（后台运行）

```bash
geckodriver --port 9515 --log trace   # 独立进程启动后，脚本连接 9515 端口
```

或直接由 selenium 自动拉起。

## 5. 常见问题

- **登录态丢失**：未复用 profile → 按阶段 3 提示用户手动登录即可。
- **站点识别自动化并拦截**：部分站点检测 webdriver 特征；如实告知用户，或引导用户在同一 Firefox（非自动化实例）手动登录后复用 profile。
- **找不到元素**：先执行 JS 打印 `document.body.innerText` 前 2000 字定位真实结构。
- **回复未加载完**：加等待时间、滚动到底、轮询读取文本长度直到不再增长。
- **Firefox 版本过旧**：geckodriver 与 Firefox 版本需大致匹配；提示用户升级 Firefox 或换用对应版本 geckodriver。
