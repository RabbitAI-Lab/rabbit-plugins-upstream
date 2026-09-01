# 故障排查与逆向记录

## 1. `browser_start_session` 必然失败 —— 会话协议跨代不兼容

### 现象
```
qqbrowser-skill browser_start_session --sessionId task-xxx
→ 无输出，退出码 1
```

### 根因（已逆向确认）
- CLI 1.5.4 的 `start_session` 走 **type 协议**：
  `{"type":"start_session","sessionId":...,"callPlatform":"win","callMode":"normal"}`
- QQ 浏览器 21.7.7001.400 内置扩展**只支持 `actionName` + `actionParams` 业务命令**，
  且**完全没有会话生命周期**（扩展源码里搜不到 `start_session`）。
- 扩展收到 type 协议消息后取不到 `actionParams` → `JSON.parse(undefined)` →
  回包 `{'actionResult': 'executeCommand error: Invalid JSON format in command: undefined'}`

### 解法
**绕开会话层，直接调业务命令**（`browser_go_to_url` / `browser_eval_content_js` / `browser_screenshot`）。
业务命令用 `actionName+actionParams`，扩展能正常处理。

### 如何自行验证扩展协议
解包扩展 CRX（它是 zip，从 `PK\x03\x04` 处切分即可）：

```python
raw = open(crx,'rb').read()
zf = zipfile.ZipFile(io.BytesIO(raw[raw.find(b'PK\x03\x04'):]))
```

自动化扩展路径：
`<QQ浏览器安装目录>/<版本>/Extensions/aaplhnhcdcgkjbijfkjdbfmiagjojdjf.crx`
→ `assets/background.js`，搜 `actionParams` / `executeCommand` 即可看到协议解析逻辑。

## 2. pip 镜像滞后（表现为版本诡异地低）

### 现象
```bash
pip index versions qqbrowser-skill   # 显示 LATEST: 1.5.3  ← 镜像滞后
```
实际 pypi.org 上是 1.5.4。版本落后会直接导致协议不匹配（见 §1）。

### 正确安装流程（先比对版本 → 按结果选源 → 失败回退阿里云）
```bash
# ① 官方源最新版
pip index versions qqbrowser-skill --index-url https://pypi.org/simple
# ② 本地镜像源版本
pip index versions qqbrowser-skill
```
- 两源**一致** → 用本地镜像源（更快）：`pip install --upgrade qqbrowser-skill`
- **不一致** → 用官方源：`pip install --index-url https://pypi.org/simple --upgrade qqbrowser-skill`
- 安装**失败** → 改用阿里云镜像源：`pip install --index-url https://mirrors.aliyun.com/pypi/simple/ --upgrade qqbrowser-skill`

## 3. 解析 CLI 输出：双重 JSON 转义

`browser_eval_content_js` 的返回被嵌在 CLI 的 `actionResult` 字符串里，
**引号被转义成 `\"`，换行被转义成 `\\n`（三层）**。

正确提取（见 `scripts/qq_hw.py` 的 `extract_result`）：
1. 定位 `"Result: "` 之后、`">>>>>"` 之前的内容
2. `json.loads('"' + chunk + '"')` 解第一层
3. 若仍失败，退回 `replace('\\"','"').replace('\\\\','\\')`

⚠️ **不要用** `encode().decode('unicode_escape')` —— 它会把 UTF-8 中文当 ASCII 处理，产生乱码。

⚠️ 注意 CLI 输出里有**两个** `Result:`：
- `Action result: ... Result: <你的 JS 返回值>` ← 要这个
- `Action Result: No page navigation triggered.` ← 不要这个（`"Result: "` 会误匹配）

## 4. Word COM 统计页数的坑

```powershell
$doc.ComputeStatistics(2)   # 2 = wdStatisticPages
```

三个坑：
1. **中文文件名可能干扰 COM** → 先 `Copy-Item` 到 ASCII 临时路径再打开
2. **catch 里再调 `$word.Quit()` 会抛 RPC 错误并覆盖真实异常** → 先记录异常再 Quit
3. 残留的 `winword.exe` 进程会让后续调用失败 → 必要时 `Stop-Process -Name winword -Force`

## 5. PowerShell 工具不回传 stdout

本环境下 PowerShell 工具的 stdout 不显示。**一律让脚本把结果写入文件**，再用 Read 读取。

## 6. 单页约束为什么这么难

`Heading 2` / `List Number` 样式自带 `space_before/after` 和 **1.15 倍行距**，
在段落级别设 `space_after=0` 压不住，必须改**样式本身**：

```python
st = doc.styles['Heading 2']
st.paragraph_format.space_before = st.paragraph_format.space_after = Pt(0)
st.paragraph_format.line_spacing = 1.0
```

再加上：页边距 0.8cm、表格单元格边距清零（`w:tblCellMar` 全设 0），才压得进一页。

## 7. 图片体积

原图可能高达 8192×6144。用 PIL 压到长边 1400px / quality 82，
docx 从 **2.75MB → 0.6MB**，视觉无损。

## 8. 沙箱

浏览器自动化必须 `dangerouslyDisableSandbox: true`，否则：
```
[safe-delete][SAFE_DELETE_FAIL_CLOSED] reason: windows-sandbox-recycle-bin-unavailable
```
该告警本身通常无害（`serve --daemon` 带此告警仍能启动成功），
但 `browser_start_session` 遇到它会直接退出。

## 9. 详情接口偶发 `retcode:2001`（`ptlogin-ex verify fail`）—— 列表接口已含完整文本

### 现象
`day` 子命令调 `get_hw_detail.fcg` 时，部分（或全部）作业返回：
```json
{"retcode":2001,"msg":"ptlogin-ex verify fail[filter]. uin:xxxx"}
```
而列表接口 `get_hw_list.fcg`（`cmd=21`）始终正常。bkn 从 `performance.getEntriesByType('resource')` 能正常探到，说明是**详情接口的二次风控**，不是 bkn 失效。

### 关键事实
**列表接口返回的 `content.c[]` 已包含完整的 `str` 文本**（标题、科目、正文都齐），
只有 `img` 类型会缺 `url`（图片 URL 仅在详情接口里）。所以纯文本作业理论上可用列表文本，
但**仍优先引导登录**——否则含图作业会丢图、生成残缺文档。

### 根因（用户确认）
不是笼统的"二次风控"，而是**尚未在 https://qun.qq.com/#/login 完成登录**，
使详情接口的 ptlogin-ex 校验失败；列表接口校验较松故仍可用。

### 解法（已合入 `scripts/qq_hw.py`）
- `cmd_list` / `cmd_day` 检测到 `retcode==2001` 或返回含 `verify fail` 时，调 `_prompt_login()`：
  自动 `browser_go_to_url` 打开 `https://qun.qq.com/#/login`，并打印醒目提示让用户点击「登录」，返回码 2。
- **不再静默回退**：未登录时直接提示登录，不生成残缺文档；用户登录成功后重跑命令即可。
- `build_docx` 仍对缺 `c` 字段的条目做 `.get("c", [])` 容错，避免异常数据 KeyError。

## 10. docx → PDF（Word COM）的中文路径坑

### 现象（四个坑，逐个踩过）
1. 直接 `SaveAs` 到**中文路径** → Word COM **静默吞掉**，文件没生成也不报错
2. 用 `$env:TEMP` 当临时目录 → 它返回 `HANLEY~1` 这类 **8.3 短路径**，`SaveAs` 报
   「值不在预期的范围内」
3. 中文路径经 `powershell -File x.ps1 -Docx <中文路径>` **命令行参数传递** →
   被按系统编码解码成乱码，`Documents.Open` 找不到文件（表现为 `SAVE_FAIL` / rc=3）
4. here-string 写成**单行** `@'...'@` → 报 `UnexpectedCharactersAfterHereStringHeader`
   （here-string 的结束符必须独占一行，不能单行闭合）

### 解法（已合入 `cmd_pdf`）
1. 路径**不作为命令行参数传递**，而是作为**字面量写入 UTF-8 BOM 的临时 ps1**
   （`_conv_pdf_run.ps1`）；PowerShell `-File` 读文件时按 UTF-8 正确解码中文
2. 路径用**普通单引号**包裹，不要用 here-string
3. `SaveAs` 到**项目目录下的 ASCII 临时名** `_tmp_conv.pdf`（避开 8.3 短路径与中文名），
   再 `Copy-Item` 回中文名
4. `$w.Quit()` 放 `finally` 并吞掉 RPC 异常（`0x800706BE` 无害，不影响产物）

### 页数校验
PDF 由 docx 转出，二者分页一致 —— 用 `pages` 子命令校验 **docx** 为 `PAGES=1` 即可，
PDF 必然也是单页。
