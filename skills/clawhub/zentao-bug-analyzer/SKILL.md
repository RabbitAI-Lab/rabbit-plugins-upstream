---
name: zentao-bug-analyzer
description: "禅道缺陷自动分析：从飞书消息解析Bug链接，自动模块分类+分支定位+代码分析，Playwright评论+飞书通知双通道输出。"
---

# 禅道缺陷自动分析 (zentao-bug-analyzer)

禅道实例：`http://zentao.gxatek.com:20080/`（企业版 12.1）

## ⚠️ 执行守则（最高优先级）

> 🔴 分析前必须先读完 `SKILL.checklist.md` 的全部检查项，每条逐项完成。

1. **只用 scripts/ 下的 5 个脚本操作禅道**，禁止手写临时 Playwright 文件
2. **一个 Bug 只启动一次浏览器**，所有操作复用同一 WS endpoint
3. **脚本报错 = 诊断脚本的输入条件**（WS 是否有效？参数是否正确？），不是另起炉灶的理由
4. **分析完成后保持仓库不动**：`git checkout <commit-id>` 分析完后不做任何恢复操作。
5. **分析完输出报告**：步骤 4d 产出分析报告后，根据 `auto_comment` 配置决定是否评论禅道：
   - `auto_comment === true`：运行 `zentao-post-comment.js` 评论 + 飞书摘要
   - `auto_comment === false`：仅飞书摘要，不评论禅道

## 触发方式

### 方式一：邮件转发触发
飞书 Bot 收到包含禅道 Bug 链接的消息时自动触发。

正则模式：`zentao\.gxatek\.com:20080/bug-view-(\d+)\.html`

### 方式二：自然语言触发
用户直接在飞书对话中：
- 发送禅道 Bug 链接
- 「帮我分析我名下所有未解决的缺陷」
- 「分析最近 3 天指派给我的严重缺陷」

**批量分析**：批量触发时，先通过 Playwright 会话查询 Bug 列表，每个 Bug 独立走完整流水线。不同 Bug 按第三章并发规则处理。

**无有效链接时**：飞书私聊回复「未识别到有效的禅道缺陷链接，请确认消息内容」。

---

## 配置文件

依赖 `{workspace}/bug-analyzer-config.json`。

```jsonc
{
  "zentao": {
    "url": "http://zentao.gxatek.com:20080",
    "account": "wyhe",
    "password": "你的禅道登录密码"
  },
  "notify": {
    "feishu_open_id": "飞书私聊通知目标用户 Open ID，步骤 3/4b 等所有飞书通知场景使用"
  },
  "auto_comment": true,
  "modules": [
    {
      "name": "车机设置",
      "aliases": ["桌面卡片", "设置", "systemui", "SystemUI"],
      "code_dir": "D:/code/car-settings",
      "commit_extract": "日志中以 'Build commit:' 开头的那一行，取后面的 8 位 hash",
      "analyzer": "default",
      "analyze_hint": "重点关注桌面卡片相关代码，常见问题是侧滑返回时的 Activity 生命周期处理"
    },
    {
      "name": "蓝牙模块",
      "aliases": ["蓝牙", "BT", "bluetooth", "bt-stack"],
      "code_dir": "D:/code/bt-stack",
      "commit_extract": "日志里搜索 'git_hash='，取等号后面的完整 hash",
      "analyzer": "default",
      "analyze_hint": "蓝牙相关缺陷通常与连接状态机有关，优先检查 BluetoothManager 的状态流转"
    }
  ]
}
```

字段说明：
- `name`：模块名称
- `aliases`：模块别名列表（字符串数组），用于精确匹配。**匹配规则**：将 Bug 的 title、module.name、product.name 与所有模块的 name + aliases 做**子串匹配**（忽略大小写），任一命中即判定为该模块。此规则为硬规则，优先于 AI 主观判断
- `code_dir`：模块本地代码仓库绝对路径
- `commit_extract`：自然语言，告诉 AI 如何从日志提取 commit id
- `analyzer`：`"default"` | `"skill:技能名"`。default 走通用 AI 分析流程；skill:xxx 委派给对应 Skill
- `analyze_hint`：模块专属分析提示词（可选），无论哪种分析器都会传给分析器
- `auto_comment`：布尔值，控制分析完成后是否自动将报告评论到禅道 Bug 下。`true` = 自动评论（默认行为）；`false` = 仅生成报告 + 飞书通知，不评论禅道

### 首次配置引导

配置文件不存在时启动对话式引导。流程：

1. 「请提供禅道的登录账号和密码（用于 Playwright 登录禅道。密码会存储在本地配置文件中，不会泄露）」
2. 「你负责哪些模块？请列出模块名称（用逗号分隔，如：车机设置, 蓝牙模块, 语音助手）」
3. 对每个模块依次询问：
   - 「对于"{模块名}"模块，有哪些别名/关键词可以用来识别？（用逗号分隔，如：桌面卡片, systemui, 设置）」
   - 「对于"{模块名}"模块，本地代码目录路径是什么？（请使用绝对路径）」
   - 「对于"{模块名}"模块，日志中如何提取 commit id？请用自然语言描述提取规则」
   - 「对于"{模块名}"模块，是否需要使用专用分析 Skill？（目前可用的 Skill：[列出]。输入 Skill 名或留空走默认分析）」
   - 「对于"{模块名}"模块，有什么分析提示或重点关注方向？（可选，留空则用默认分析策略）」
4. 「分析完成后，是否需要自动将分析报告评论到禅道 Bug 下？（回复"是"=自动评论，"否"=仅飞书通知，不评论禅道）」
5. 「配置完成！请确认你已创建邮件收信规则：当发件人为 `zentao@syncore.space` 时，自动将邮件转发/分享到本 Bot 的对话中。」

---

## 分析流水线

### 步骤 1：消息解析

从消息内容提取禅道 Bug 链接，正则：`zentao\.gxatek\.com:20080/bug-view-(\d+)\.html`

### 步骤 2：重复分析检查

> ⚠️ 此步骤是强制检查点，无论通过哪种触发方式（邮件转发或自然语言）进入分析流水线，必须先走步骤 2。已评论过的 Bug 绝对不允许直接进入后续步骤。

1. 运行 `scripts/zentao-get-bug.js` 获取 Bug 详情（含历史评论，后续步骤复用）
2. 检查历史评论中是否已有 `zentao.account` 配置账号的评论

**已有我的评论**：飞书私聊询问「该 Bug 你已评论过，是否需要重新分析？（回复"是"或"分析"继续，回复"否"或"取消"跳过）」
- 确认「是」→ 继续步骤 3
- 确认「否」或 5 分钟内未回复 → 流程终止

**没有我的评论**：直接继续步骤 3。

### 步骤 3：模块分类

**匹配规则（优先级从高到低）**：

1. **硬别名匹配（优先）**：遍历配置中每个 module 的 `aliases` 数组，将每个别名与 Bug 的 `title`、`module.name`、`product.name` 做**子串匹配**（忽略大小写）。只要任一副本字段包含任一个别名（或 `name` 本身），即判定命中该模块。
   - 例如：Bug标题含"桌面卡片"，配置别名中有"桌面卡片" → 直接命中
   - ⚠️ 此规则是机械规则，不依赖 AI 判断，直接执行
2. **AI 语义判断（兜底）**：硬别名未命中时，AI 综合判断 Bug 归属模块，对照配置文件 `modules` 列表

**结果处理**：
- **在范围**：继续步骤 4
- **不在范围**：飞书私聊通知（Bug 标题、链接、AI 判断的模块归属），提醒模块确认和手动流转。流程结束
- **置信度低**：飞书私聊通知（Bug 链接 + 关键信息），告知无法确定模块，请手动确认。流程结束

### 步骤 4：深度分析

#### 4a. 下载附件和日志
运行 `scripts/zentao-download-files.js` 下载 Bug 所有附件到 `bugs/{bug_id}/`。（script 自动处理大文件分块传输，支持 160MB+ 附件）

> ⚠️ 步骤 4a 完成后必须先执行 4b（确定 Bug 发生时间），再进入 4c。

#### 4b. 确定 Bug 发生时间

> ⚠️ 硬约束：Bug 发生时间必须从可靠来源直接获取，禁止猜测或间接推断。

**获取优先级**：
1. **Bug 描述文本**中明确写出的时间（如「17:33 复现」「12:05 发现」）
2. **附件视频/截图**中可见的系统时间（状态栏、水印等），需打开查看
3. **飞书询问用户**：以上均不可用时，私聊询问「该 Bug 发生的精确时间是什么？」

**禁止行为**：
- ❌ 用附件文件名中的时间戳猜测
- ❌ 用 Bug 创建时间、最后修改时间间接推断
- ❌ 用聊天消息转发时间、邮件接收时间推断
- ❌ 任何不在上述优先级列表内的间接推演

**时间用于**：
- 日志分析：定位 Bug 发生时刻前后 ±5 分钟的日志片段
- Git blame：确定相关代码变更时间线
- 匹配历史评论中提到的复现时间

#### 4c. 分支定位
1. 解压并读取日志文件：
   - Android logcat 的 `.gz` 文件**必须使用 Node.js zlib 解压**，禁止使用 PowerShell `tar`、`System.IO.Compression.GZipStream` 或类似 .NET 解压工具
   - ⚠️ .NET GZipStream 对 Android logd 生成的某些 gzip 流存在兼容性 bug（提前终止解压，实际 30MB 仅解出 ~65KB），会导致日志内容严重缺失
   - 推荐命令：`node -e "const zlib=require('zlib');const fs=require('fs');const buf=fs.readFileSync('<log.gz>');zlib.gunzip(buf,(e,r)=>{if(e){console.error(e);return}const s=r.toString('utf8');/* 搜索/处理 s */})"`
2. 按配置中 `commit_extract` 从日志提取 commit id
3. `cd {code_dir}` → `git branch --contains <commit-id>` 确认 commit 在哪些分支上。结果写入分析报告的「分支信息」字段（格式：`分支名 | commit-id`）
4. 同模块已有其他分析任务时，用 `git worktree add .claude/worktrees/bug-{bug_id}/ <commit-id>` 创建隔离工作区
5. `git checkout <commit-id>`（进入 detached HEAD 是正常行为，分析完成后保持不动即可）+ `git submodule update --init --recursive`

**commit id 提取失败**：飞书私聊通知（附带日志片段），流程终止。

> ⚠️ 硬约束：只使用配置中 commit_extract 指定的提取规则，禁止 AI 自行更换搜索关键词（如换 TAG、换正则）。搜不到就是搜不到，不允许"近似匹配"或"换成类似的 TAG 试试"。
> Self-Check：若在分析过程中进行了 commit_extract 规则以外的额外搜索，应立即停止、丢弃中间产物，回到步骤 4c 标准路径并报告提取失败。

**commit id 不在任何分支**：飞书私聊通知（附带 commit id），流程终止

> ⚠️ 硬约束：`git checkout <commit-id>` 后必须执行 `git submodule update --init --recursive`，确保所有 submodule 都已 checkout 到对应版本。未 checkout submodule 可能导致分析时缺少依赖代码、漏掉跨仓库 API 不一致问题。

#### 4d. AI 综合深度分析

历史评论已在步骤 2 获取，此处直接使用。

根据 `analyzer` 字段：
- `"default"`：AI 综合 Bug 详情 + 附件/日志 + 历史评论 + 本地代码分析
- `"skill:xxx"`：委派给指定 Skill，传入分析上下文

无论哪种方式，`analyze_hint` 都作为上下文传入。

输出格式（Markdown，AI 直接产出此结构）：

### 分支信息
- **commit**: `abc12345`
- **分支**: `branch/name`

### 根因定位
- **文件**：`path/to/file.ext:行号`
- **代码片段**：
  ```lang
  // 关键代码
  ```
- **判断依据**：（结合日志/历史评论/代码逻辑的推理过程）

### 修复建议
1. 具体修复方向（可操作步骤，非抽象建议）

### 风险评估
- **影响范围**：（哪些功能/模块受影响）
- **严重程度**：（低/中/高/严重 + 理由）

### 步骤 5：结果输出

> ⚠️ **auto_comment 开关**：步骤 5 开始前，检查配置文件中 `auto_comment` 字段（默认为 `true`）。
> - `auto_comment === false`：跳过禅道评论（步骤 5.1），仅生成 `report.md` + 执行飞书私聊通知（步骤 5.2）
> - `auto_comment === true` 或未配置：执行完整双通道（禅道评论 + 飞书通知）

1. **禅道评论**（仅在 `auto_comment !== false` 时执行）：
   a. 将分析报告写入 `bugs/{bug_id}/report.md`（按步骤 4d 输出格式）
   b. 运行 `node scripts/zentao-build-comment.js bugs/{bug_id}/report.md --out bugs/{bug_id}/comment.html` 生成 HTML
   c. 运行 `node scripts/zentao-post-comment.js --ws=<wsEndpoint> --bug-id=<id> --comment-file=bugs/{bug_id}/comment.html` 发布（**必须用 `--comment-file`，禁止用 `--comment` 传 HTML 内容**）
   d. ⚠️ 禁止手写临时 Playwright 脚本发布评论
2. **飞书私聊**：简要摘要 + 禅道 Bug 链接

### 步骤 6：清理

分析完成后必须清理残留进程，避免占用系统资源：

1. **杀掉 login 常驻进程（连带 Chrome）**：`taskkill /PID <login-PID> /F /T`，PID 来自 `zentao-login.js` 输出行 `PID=<value>`。`/T` 会连带终结 Chrome 子进程树
2. **清理 git worktree**：`git worktree list` 检查是否有 `.claude/worktrees/bug-{bug_id}/` 残留，有则 `git worktree remove .claude/worktrees/bug-{bug_id}/`
3. **检查残留脚本进程**：`Get-Process node` 检查是否还有 `zentao-*.js` 相关进程，有则 `taskkill /F /PID <pid>` 清理
4. **确认清理完毕**：最终应只剩 OpenClaw 自身的 node 进程（gateway/worker），不应有其他 `zentao-*.js` 残留

> ⚠️ 注意：不要杀掉 OpenClaw 自身的 node 进程（gateway/worker），只清理 `zentao-*.js` 和 Chrome headless 相关进程。

---

## 并发处理

- **不同模块**：代码目录不同，全部并行处理
- **同一模块同时分析多个 Bug 时**：用 `git worktree` 为每个 Bug 创建隔离工作区，分析完成后 `git worktree remove` 清理

---

## 禅道交互方式

> ⚠️ 企业版 12.1 不支持 Bearer Token 认证（`POST /api.php/v1/tokens` 不可用），所有读写操作统一走 Playwright。

### 🔴 铁律：单次 Playwright 会话

**一个 Bug 的分析全程只允许启动一次 Playwright 浏览器**。登录后所有操作（读详情、下载附件、写评论）复用同一会话，禁止：

- ❌ 分多个脚本文件各启动一次 Playwright
- ❌ 中途关闭浏览器再重新登录
- ❌ 写评论时用新的浏览器实例

### 🔴 铁律：脚本优先，禁止手写临时 Playwright 脚本

**禅道交互只允许使用 `scripts/` 目录下的 5 个固定脚本**：

| 脚本 | 用途 | 关键参数 |
|------|------|----------|
| `zentao-login.js` | 登录 | `--port`（默认 9224）|
| `zentao-get-bug.js` | 获取 Bug 详情 | `--ws`、`--bug-id` |
| `zentao-download-files.js` | 下载附件 | `--ws`、`--bug-id`、`--dir` |
| `zentao-build-comment.js` | Markdown → HTML 评论 | `<report.md> [--out <output.html>]` |
| `zentao-post-comment.js` | 发布评论 | `--ws`、`--bug-id`、`--comment-file=<path>`（推荐）或 `--comment`（原始 HTML）|

**禁止行为**：
- ❌ 手写临时 `post_comment.js`、`check_bug.js`、`debug_login.js` 等任何 Playwright 脚本
- ❌ 在 `bugs/{bug_id}/` 目录下创建任何 `.js` 文件
- ❌ 用 `page.evaluate`、`page.fill`、`page.click` 等 Playwright API 绕过已有脚本

**遇到脚本报错时的正确处理方式**：
1. 先读脚本源码，理解它依赖的输入（WS endpoint、参数格式等）
2. 修复输入条件（如重新登录获取有效 WS endpoint），而不是绕过脚本
3. 如果脚本本身有 bug，修复脚本源码（`scripts/` 目录下），让修复对所有后续分析生效

---

## 边界情况处理

| 场景 | 处理 |
|------|------|
| 不含禅道链接 | 「未识别到有效的禅道缺陷链接，请确认消息内容」 |
| 链接解析失败 | 「无法解析该链接，请确认是否正确转发」 |
| 禅道 API 请求失败（登录失效/会话过期） | 「无法访问禅道，请检查连接和登录状态」 |
| 模块分类置信度低 | 飞书通知：Bug 链接+关键信息，请手动确认 |
| 模块不在负责范围 | 飞书通知：Bug 归属 + 提醒手动流转 |
| commit id 提取失败 | 飞书通知：日志片段，请手动确认分支 |
| commit id 不在任何分支 | 飞书通知：commit id，请手动确认 |
| 附件/日志下载失败 | 降级：仅基于 Bug 描述+历史评论+代码分析，评论注明「未能获取附件」，飞书通知 |
| 本地代码目录不存在 | 降级：跳过代码分析，仅日志+附件+评论，飞书通知检查配置 |
| 分析过程中断或超时 | 飞书通知进度和失败原因，不留半截评论 |
| 用户 5 分钟内未回复重新分析确认 | 默认不重新分析，流程终止 |
| 分析过程中 git worktree 冲突 | 清理残留 worktree 后重试；仍失败则飞书通知 |

---

## 范围约束

- 不自动填写指派人或流转状态
- 不自动生成修复代码
- 不做缺陷趋势统计或报表
- 当前只服务单一用户
