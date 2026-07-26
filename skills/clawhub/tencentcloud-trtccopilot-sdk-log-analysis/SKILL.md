---
name: sdk-log-analysis
description: SDK 客户端日志分析 skill。用于本地 .clog/.xlog/文本日志的类型识别、二进制解码，以及 TRTC/IM/TUI 客户端日志时间线解析。
version: "0.1.0"
tags:
  - trtc
  - log-analysis
  - clog
  - timeline
references:
  - references/web-log-patterns.md
  - references/native-log-patterns.md
  - references/miniprogram-log-patterns.md
  - references/audio-troubleshooting.md
---

# SDK 客户端日志分析

本 skill 专注客户端日志：本地 `.clog/.xlog` 二进制解码、本地 TRTC / IM / TUI 日志文件时间线解析。TUI 指 TUICallKit、TUIRoomKit、TUILiveKit、TUIRoomEngine 等上层 SDK。`timeline.js` 支持 TRTC / IM / TUI 自动识别。服务端事件回调、云端录制/混流/转推链路不在本 skill 范围内。

> 内网环境额外可用 Clog / Kibana 主动查询能力（见 `scripts/query-clog.js` / `scripts/query-kibana.js`），但需满足内网条件。运行 `node scripts/internal-check.js`，**仅当返回 `allowed: true` 时**才读取 `references/internal-tools.md` 并按其指引操作。外网或对外部客户场景不要加载该文件，也不要提及这些内部工具。

## 环境配置

本 skill 的预览能力通过环境变量控制：

| 变量 | 值 | 含义 |
|------|-----|------|
| `SDK_LOG_PREVIEW` | 未设置 / `1` / `true` / `on` / `yes` | 启用本地 Web 预览（默认，本地 CodeBuddy / Claude Code） |
| `SDK_LOG_PREVIEW` | `0` / `false` / `off` / `no` / 空字符串 | 禁用预览，仅输出文本结论（云端 agent 平台） |

**Agent 判定流程**：

1. 若 `SDK_LOG_PREVIEW` 命中上表 falsy 行（云端平台），直接走"纯文本结论"模式：跳过 §7 全部内容，结论中不出现任何 `http://127.0.0.1` 链接。
2. 若 `SDK_LOG_PREVIEW` 未设置或命中上表 truthy 行，默认按启用预览处理（向后兼容）。

脚本层会自动遵守该环境变量（`serve-viewer.js` 禁用时 no-op 退出；`analyze-local.js` / `query-clog.js` / `query-kibana.js` 禁用时跳过 `viewer-index.json` 写入）—— agent 无需在调用脚本时传额外参数。

## 0. 本地日志入口快路径（先判类型，再分析）

> 以下所有命令的工作目录为**本 skill 根目录**（即含 `scripts/`、`vendor/`、`data/` 的目录）。
> 请先 `cd` 到该目录再执行，或自行把 `scripts/...` / `vendor/...` 补全为实际安装路径。

当用户直接给本地日志文件（如 `tmp/foo.clog`、`.xlog`、`.log`、`.txt`）时，先走这条路径，避免把二进制 Clog 当文本分析，也避免对 GB 级文本日志直接启动重 CPU 时间线。

### 0.1 默认入口：统一脚本

优先使用统一脚本，它会自动判类型、解码 `.clog/.xlog`，并对超大文本做有界初筛：

```bash
node scripts/analyze-local.js \
  --logs /path/to/input.clog \
  --workers 2
```

默认控制策略：

- `.clog/.xlog` 或二进制文件：先解码到本次 session 目录，再分析解码后的 `.log`。
- `timeline` 默认只对 **≤ 200MB** 的文本做全量计算。
- 解码超时默认 **300s**，时间线超时默认 **120s**。
- 文本超过 200MB 时，默认不跑全量 `timeline`，而是生成 head/tail 有界 sample，再对 sample 跑时间线，并在输出中标记 `[mode] sample`。
- 只有用户明确接受 CPU/耗时成本时，才加 `--force-timeline` 做全量时间线。

### 0.2 什么时候不要直接跑 `timeline.js`

1. 若 `read_file` 提示 binary、`file` 返回 `data`，或扩展名是 `.clog` / `.xlog`，先解码，不要直接跑 `timeline.js` / grep / rg。
2. 若文本日志可能很大（例如 >200MB、百万行级别），不要直接跑全量 `timeline.js`；先用 `analyze-local.js` 默认模式初筛。
3. 如果 `timeline.js` 对 `.clog` 直接输出 `events=0`，先检查是否忘了解码；不要据此得出“日志无关键事件”。

### 0.3 需要手动拆步时

解码本地 Clog/Xlog：

```bash
node vendor/clog-decoder/dist/cjs/node/cli.js \
  /path/to/input.clog \
  /path/to/input.clog.log
```

对已解码且大小可控的文本跑时间线：

```bash
node scripts/timeline.js \
  --logs /path/to/input.clog.log \
  --workers 2 \
  --loop-all-rule
```

然后根据 `timeline.md` 的行号回读解码后的 `.log`，并按症状关键词补充搜索。

## 1. 数据源

本 skill 默认处理**用户提供的本地日志文件**（`.clog/.xlog/.log/.txt`），使用 agent 的内置文件搜索/读取能力或本 skill 的脚本进行分析。

强规则：

- 分析前先判类型：二进制 `.clog/.xlog` 必须先解码再分析（见 §0）。
- 查询/搜索后必须读取原文上下文，不能只看摘要下结论。
- 结论必须标明依据来自哪份日志。

## 2. Clog decoder 策略

脚本按以下顺序选择 decoder：

1. skill 内 vendored decoder：`vendor/clog-decoder/dist/cjs/node/cli.js`。
2. npm fallback：`npx --yes @tencent/sdk-log-decoder`。

vendored decoder 是 `@tencent/sdk-log-decoder` 的纯 TypeScript 实现（esbuild bundle，fflate 内联，无 `node_modules` 依赖），不绑定 OS/CPU，整个 `vendor/clog-decoder` 目录 copy 即可跨平台运行，无需按平台分别构建。

## 3. 生成时间线

时间线脚本只做规则匹配与文案渲染，不做额外巡检。规则集合、错误码解释来自 `data/api/*.json`，不要在脚本中写死业务文案。脚本会自动检测日志类型并映射 SDK 维度：`trtc → 实时音视频TRTC`、`im → 即时通信IM`、`tui → RTCRoomEngine`。不再接受 `--timeline` / `--timeline-id` / `--rule-ids`，默认使用识别到的 SDK 下所有 timeline 的规则集合。

```bash
node scripts/timeline.js \
  --logs /path/to/logs.txt \
  --workers 2
```

可选参数：

- `--api-dir <dir>`：覆盖接口 JSON 数据目录。
- `--workers <n>`：按逻辑日志条目分片并行匹配；默认 `1`；大日志不建议盲目加大，避免 CPU 打满。
- `--loop-all-rule`：单条日志命中多条规则时全部保留；默认每条日志只取第一条命中规则。
- `--no-cache`：忽略已有同输入产物，重新计算。
- `--max-input-bytes <bytes>`：文本日志全量时间线大小上限，默认 200MB。
- `--force-large`：明确接受 CPU/内存成本时，允许超过上限的文本日志跑全量时间线。

保护行为：`timeline.js` 会拒绝 `.clog/.xlog` / 二进制输入；也会拒绝超过默认上限的文本输入。遇到这两类情况，改用 `analyze-local.js`。

输出：

- `timeline.md`：关键事件时间线。
- `timeline.json`：结构化时间线事件。
- `manifest.json`：输入文件、API 数据、workers、cacheKey 等产物元信息。

同一份日志、同一份 API 数据、同一组选项会复用 `tmp/sessions/timeline-cache/<cacheKey>/` 下的既有产物，并输出 `[cache] hit`。

## 4. 接口数据目录

`data/api/` 存放固化下来的 JSON 数据：

- `data/api/log-rule.json`：`DescribeSdkLogRuleList` 形态的日志规则，顶层按 `SdkName` 归属；`RuleRegList[].Reg` 用于匹配一条逻辑日志（IM 以 `TIM:` 开头分段，TRTC/TUI 以 `[` 开头分段），`RegDesc` 使用 art-template 语法渲染命中文案。
- `data/api/timeline.json`：`DescribeSdkTimelineList` 形态的时间线分组，顶层按 `SdkName` 归属；`TimelineList[].LogRuleList` 是该分组要启用的日志规则 ID 集合。
- `data/api/error-code.json`：`DescribeSdkErrorCodeList` 形态的错误码解释，顶层按 `SdkName` 归属，供模板中的 `errorCode` / `__errorCode` 过滤器使用。

`references/` 保留给 Agent 阅读的 Markdown 知识文档；机器消费的接口数据放 `data/api/`，避免被误当成 reference 文档加载。

## 5. Reference 使用规则

分析前按场景读取参考文档：

| 场景 | 必读 |
|---|---|
| Web 日志 | `references/web-log-patterns.md` |
| Native 日志 | `references/native-log-patterns.md` |
| 小程序日志 | `references/miniprogram-log-patterns.md` + `references/native-log-patterns.md` |
| 音频问题 | `references/audio-troubleshooting.md` + 对应端文档 |

## 6. 结论格式

输出分析结论时，**必须给出可供人工核验的证据**：每条关键判断都要附上对应的原始日志行（含行号），并主动提供预览链接让人工在页面核对。

```markdown
## 分析结论

### 数据源
- 本地日志: ...

### 关键时间线
| 时间 | 用户 | 数据源 | 事件 | 说明 | 证据(行号) |
|---|---|---|---|---|---|
| ... | ... | ... | ... | ... | L1234 |

### 定位
- 根因：...
- 关键日志（证据原文）：
  - `L1234: [E][...] onEnterRoom err:-3319 ...`
  - `L1250: [W][...] ...`
- 置信度：高/中/低

### 建议
1. ...

### 人工核验

**启用预览时**（本地平台，默认）：
- 预览链接：http://127.0.0.1:<port>（见 §7），可在页面按行号跳转核对上述证据

**禁用预览时**（云端平台，`SDK_LOG_PREVIEW=0`）：
- 不提供任何本地 URL（云端用户无法访问 127.0.0.1）
- 在结论中展开关键事件原文（时间戳 + 行号 + 上下文行），让用户在对话内核验
- 必要时附上 timeline 关键事件列表（按时间排序）
```

强规则：

- 不要只给结论，要给**结论所依赖的原始日志原文 + 行号**，方便人工复核。
- 涉及关键判断（进房失败、错误码、断连等）时：
  - **启用预览**：主动启动 Web 预览并把链接给用户（见 §7），引导人工在页面验证，而不是等用户来问。
  - **禁用预览**（`SDK_LOG_PREVIEW=0`）：在结论中展开该关键事件的原文（时间戳 + 行号 + 上下文），让用户在对话内直接核验。

## 7. Web 预览界面（条件性，受 SDK_LOG_PREVIEW 控制）

> **当 `SDK_LOG_PREVIEW=0` 时，本节全部跳过** —— 不启动预览服务、不提供本地链接、不写 `viewer-index.json`。分析结论直接以文本形式（timeline 摘要 + 异常片段原文）返回。以下内容仅在**启用预览**（默认）时生效。

本地浏览器 UI：monaco 暗黑编辑器（按日志类型语法高亮）+ 时间线（连续同规则事件合并折叠、点击跳转原文）+ 房间列表，顶部下拉切换不同解码日志。

### 何时使用

- 给出分析结论后，**主动启动预览并把链接附在结论里**，让人工按行号核对证据日志。
- 用户想交互式翻看日志、时间线、房间信息时。

### 启动

**必须用 `--daemon` 后台启动**（serve-viewer 是常驻进程，前台直接跑会一直阻塞，等 agent 当前命令轮次结束被 SIGTERM 杀掉，表现为 `Exit Code 143`）：

```bash
node scripts/serve-viewer.js --dir <解码后的日志目录> --daemon
# 或使用生成期标注好类型的索引（推荐，kibana 类型权威）：
node scripts/serve-viewer.js --index <run-dir>/viewer-index.json --daemon
```

- `--daemon` 会 fork 一个 detached 子进程承载服务，命令**立即返回并打印链接**，不阻塞、不会被轮次结束杀掉。
- 默认端口 8717；**端口被占用时自动顺延**（8718、8719…），无需手动处理冲突。
- **同一份日志若已有服务在跑，会直接复用其链接、不再新起进程**（避免端口/进程堆积）。需要强制新建用 `--force`。
- 从输出里读取实际地址：`[viewer] http://127.0.0.1:<port>`，把该链接提供给用户。

> 不要在前台直接 `node scripts/serve-viewer.js ...`（不带 `--daemon`）——那会阻塞当前命令直至超时被杀（Exit 143）。前台模式仅用于调试。

### 服务管理（避免无限堆积）

每个服务是常驻进程。**反复启动前先复用、用完记得停**：

```bash
node scripts/serve-viewer.js --list        # 列出运行中的预览服务（端口/pid/目标）
node scripts/serve-viewer.js --stop <port> # 停止指定端口的服务
node scripts/serve-viewer.js --stop-all     # 停止全部预览服务
```

- 启动时默认会复用同目标的已有服务，正常不会堆积。
- 注册表会**自愈**：已退出的进程在 `--list` 时自动清除。
- 分析任务结束、或不再需要预览时，用 `--stop <port>` / `--stop-all` 收尾。

> 如果 8717 已被占用：优先 `--list` 看是不是自己之前起的服务，能复用就复用；否则本命令会自动换端口。**不要因端口冲突反复盲启**。

### 类型标注

`analyze-local.js` / `query-clog.js` / `query-kibana.js` 各自在 run 目录产出 `viewer-index.json`；clog/local 走内容判别（trtc/im/tui/web），kibana 由 `--type` 决定（kibana_native/kibana_web）。优先用 `--index` 让 kibana 日志分类权威。

### 说明

`viewer/` 是随 skill 附带的预构建静态产物；服务端是纯 Node（零 `node_modules`），整体 copy 后即可运行。

不要在回复中泄露内部服务地址、token 等敏感信息（与 §8 禁止事项一致）；`http://127.0.0.1:<port>` 这类本地预览地址可以提供给用户。

## 8. 禁止事项

- 禁止编造日志内容。
- 禁止未读取原文就输出确定结论。
- 禁止在回复中泄露内部服务地址、下载 URL 中的临时签名参数、token、密码等敏感信息。
