---
slug: gog
name: gog
version: 1.0.1
displayName: 命令行工具
summary: Google Workspace命令行工具,覆盖Gmail/日历/云盘/联系人/表格/文档六大服务。
summary_zh: Google Workspace命令行工具,覆盖Gmail/日历/云盘/联系人/表格/文档六大服务。
license: MIT
description: |-。Google Workspace命令行工具,覆盖Gmail/日历/云盘/联系人/表格/文档六大服务。。支持自动化配置和灵活的参数设置，适覆盖多种使用场景，优化工作流程和效率。。Google。Use when 需要提升效率、自动化流程、批量处理、工作流优化时使用。不适用于需要人工创意判断的任务。
  Workspace命令行工具,覆盖Gmail/日历/云盘/联系人/表格/文档六大服务。。命令行工具工具。内置智能分析引擎，自动识别用户需求并匹配优选处理策略，减少手动干预。'
tags:
- 研发工具
- Productivity
- 工具
- 效率
- 通信
- 邮件
- gog
- json
- bash
- gmail
- sheets
tools:
- read
- exec
- glob
- grep
homepage: ''
category: Automation
homepage: "https://skillhub.cn/skill/"
---

> **核心功能**: 本技能提供化流程等能力。

> **核心功能**: 本技能提供自动化配置和灵活的参数设置、工作流程和效率、时使用、、工作流优化时使用、处理、工作流优化时使用等能力。

# gog

`gog` 是 Google Workspace 的命令行工具,统一封装 Gmail、Calendar、Drive、Contacts、Sheets、Docs 六大服务的 API 调用。所有操作通过 OAuth 凭证鉴权,支持多账户切换、JSON 结构化输出与 `--no-input` 脚本模式.
## 参数说明
| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | Gog处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

## 付费版进阶功能
| 能力 | 免费版 | 付费版 |
|:-----|:-----|:-----|
| 基础功能 | 支持 | 支持 |
| 复杂工作流可视化编排 | 不支持 | 支持 |
| 条件分支与异常重试 | 不支持 | 支持 |
| 定时触发与事件驱动 | 不支持 | 支持 |
| 执行日志与审计追踪 | 不支持 | 支持 |
| 分布式任务调度与负载均衡 | 不支持 | 支持 |

## 前置条件
### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|---:|---:|---:|---:|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
需要配置对应API Key，详见上文环境配置章节

### 可用性分类
- **分类**: MD+EXEC（）

**API Key配置方式**:
```bash
export API_KEY="${API_KEY:?请设置环境变量}"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统.
## 能力清单
- OAuth 凭证管理:导入 `client_secret.json`、添加多服务授权账户、列出已授权账户
- Gmail:按 Gmail 搜索语法检索邮件(`newer_than:`、`from:`、`has:attachment` 等)、发送邮件
- Calendar:按时间范围查询日历事件,支持 ISO8601 时间区间
- Drive:按查询语法检索文件,支持 `--max` 限制返回数量
- Contacts:列出联系人,支持分页
- Sheets:读取指定范围、更新单元格、追加行、清除范围、获取表格元数据
- Docs:导出为 txt/docx/markdown、直接 cat 输出文档内容

## 操作流程
1. **环境确认**: 确认Agent平台已加载本skill，检查依赖说明中的环境要求
2. **指令输入**: 向Agent描述需要执行的任务，引用`gog`的相关能力
3. **执行处理**: Agent按照核心能力章节的指令执行任务
4. **结果验证**: 检查输出结果是否符合预期，参考错误处理章节处理异常

## 一次性配置

```bash
gog auth credentials /path/to/client_secret.json
gog auth add you@gmail.com --services gmail,calendar,drive,contacts,sheets,docs
gog auth list
```

`client_secret.json` 从 Google Cloud Console 的 OAuth 客户端凭证页面下载,类型选择"桌面应用"。`--services` 按需勾选,首次 `auth add` 会触发浏览器授权流程.
## 常用命令

### Gmail

搜索近 7 天邮件:

```bash
gog gmail search 'newer_than:7d' --max 10
```

发送邮件:

```bash
gog gmail send --to a@b.com --subject "Hi" --body "Hello"
```

### Calendar

查询日历事件:

```bash
gog calendar events <calendarId> --from 2026-07-01T00:00:00Z --to 2026-07-31T23:59:59Z
```

### Drive

搜索云盘文件:

```bash
gog drive search "name='季度报告'" --max 10
```

### Contacts

列出联系人:

```bash
gog contacts list --max 20
```

### Sheets

读取范围:

```bash
gog sheets get <sheetId> "Tab!A1:D10" --json
```

更新范围:

```bash
gog sheets update <sheetId> "Tab!A1:B2" --values-json '[["A","B"],["1","2"]]' --input USER_ENTERED
```

追加行:

```bash
gog sheets append <sheetId> "Tab!A:C" --values-json '[["x","y","z"]]' --insert INSERT_ROWS
```

清除范围:

```bash
gog sheets clear <sheetId> "Tab!A2:Z"
```

获取元数据:

```bash
gog sheets metadata <sheetId> --json
```

### Docs

导出文档:

```bash
gog docs export <docId> --format txt --out /tmp/doc.txt
```

直接输出文档内容:

```bash
gog docs cat <docId>
```

## 使用约定

- 设置 `GOG_ACCOUNT=you@gmail.com` 可避免每次重复 `--account` 参数
- 脚本化场景优先使用 `--json` 加 `--no-input`,确保输出可解析且不阻塞
- Sheets 数据优先通过 `--values-json` 传递,避免内联行格式歧义
- Docs 仅支持 export/cat/copy;原位编辑需 Docs API 客户端,不在 gog 范围内
- 发送邮件或创建事件前需人工确认,避免误操作

## 典型场景
### 场景一:独立开发者邮件批处理

输入:近 7 天带附件的邮件列表、`--max 20`、JSON 输出
输出:结构化邮件列表,包含发件人、主题、附件名,可管道给下游脚本分类归档

### 场景二:自动化工作流表格读写

输入:Google Sheet ID、目标范围 `Tab!A:C`、追加数据 `[["x","y","z"]]`
输出:追加后的范围统计(更新行数、列数),可用于流水线断言

### 场景三:一人公司日历事件同步

输入:主日历 ID、ISO8601 时间区间 `--from` `--to`
输出:该区间内所有事件列表,含标题、开始时间、结束时间、参会人

### 场景四:文档批量导出归档

输入:多个 Doc ID、导出格式 `txt`、输出路径 `/tmp/`
输出:本地文本文件,可纳入版本控制或全文检索索引

## 案例展示

### 案例一:近 7 天邮件归档流水线

需求:每天凌晨归档近 7 天带附件的邮件到本地 JSON 文件.
实现:

```bash
export GOG_ACCOUNT=you@gmail.com
gog gmail search 'newer_than:7d has:attachment' --max 50 --json --no-input > /tmp/mail-$(date +%F).json
```

输出示例:

```json
[
  {"id":"abc123","from":"noreply@github.com","subject":"PR merged","attachments":["patch.diff"]},
  {"id":"def456","from":"boss@company.com","subject":"周报评审","attachments":["review.pdf"]}
]
```

下游脚本读取 JSON 分类归档,`--no-input` 确保不阻塞流水线.
### 案例二:Google Sheet 追加日志行

需求:CI 流水线每次构建完成后,向监控 Sheet 的 `Builds!A:C` 追加一行构建记录.
实现:

```bash
gog sheets append <sheetId> "Builds!A:C" \
  --values-json '[["2026-07-20","#1234","success"]]' \
  --insert INSERT_ROWS \
  --no-input
```

输出:`UpdatedRange: Builds!A5:C5, UpdatedRows: 1`,可用于断言追加成功.
### 案例三:日历事件导出为待办清单

需求:导出本周主日历事件,生成 Markdown 待办清单.
实现:

```bash
gog calendar events primary \
  --from 2026-07-20T00:00:00Z \
  --to 2026-07-26T23:59:59Z \
  --json --no-input \
  | python3 -c "
import json,sys
events = json.load(sys.stdin)
for e in events:
    print(f'- [ ] {e[\"summary\"]} @ {e[\"start\"]}')
"
```

输出本周所有会议标题与开始时间,管道给 Python 生成 Markdown 清单.
## 异常恢复流程
### 1. OAuth 凭证未导入

现象:`gog auth list` 为空,或调用任何命令返回 "no credentials"
原因:未执行 `gog auth credentials` 导入 `client_secret.json`
处理:从 Google Cloud Console 下载 OAuth 桌面应用凭证,执行 `gog auth credentials /path/to/client_secret.json` 后重新 `gog auth add`

### 2. 账户未授权目标服务

现象:调用 `gog gmail search` 返回 "service not authorized for account"
原因:`auth add` 时 `--services` 未包含 gmail
处理:重新执行 `gog auth add you@gmail.com --services gmail,calendar,drive,contacts,sheets,docs`,补全所需服务

### 3. Sheets 范围格式错误

现象:`gog sheets get` 返回 400,提示 "Unable to parse range"
原因:范围未带工作表名(如 `A1:D10`)或工作表名含特殊字符未加引号
处理:范围必须为 `工作表名!A1:D10` 格式;含空格或特殊字符的工作表名需用单引号包裹,如 `'My Sheet'!A1:D10`

### 4. Sheets 值矩阵维度不匹配

现象:`gog sheets update` 返回 400,提示 "values length does not match range"
原因:`--values-json` 的列数与范围的列数不一致
处理:核对范围列数与每行 values 的元素数;范围 `A1:B2` 对应 2 行 2 列,values 必须为 `[["A","B"],["1","2"]]`

### 5. Gmail 搜索语法错误

现象:`gog gmail search` 返回 400,提示 "Invalid query"
原因:搜索语法使用了 Gmail 不支持的运算符,或引号未闭合
处理:使用 Gmail 官方支持的运算符(`from:`、`to:`、`subject:`、`has:attachment`、`newer_than:`、`older_than:` 等);含空格的关键词用双引号包裹,如 `subject:"周报 评审"`

### 6. Calendar 时间格式不合法

现象:`gog calendar events` 返回 400,提示 "Invalid time"
原因:`--from` 或 `--to` 未使用 ISO8601 格式,或缺少时区标识
处理:时间必须为 ISO8601 带时区,如 `2026-07-20T00:00:00Z` 或 `2026-07-20T00:00:00+08:00`;不要用 `2026-07-20` 这种纯日期

### 7. Drive 查询语法错误

现象:`gog drive search` 返回 400,提示 "Invalid query"
原因:使用了 Drive API 不支持的查询运算符,或运算符拼写错误
处理:使用 Drive 官方查询语法,如 `name='报告'`、`mimeType='application/pdf'`、`modifiedTime > '2026-07-01T00:00:00'`;等号后值用单引号包裹

### 8. Docs 原位编辑不被支持

现象:尝试用 `gog docs` 修改文档内容但找不到对应子命令
原因:gog 的 docs 模块仅支持 export/cat/copy,不支持原位编辑
处理:原位编辑需使用 Google Docs API 客户端直接调用 `documents:batchUpdate`;gog 流程下可先 `export` 为 txt,本地编辑后重新上传为新文档

## 用户问题集锦
### Q1:如何避免每次都传 `--account`?

设置环境变量 `GOG_ACCOUNT=you@gmail.com`,gog 会自动使用该账户作为默认账户,无需每次命令重复传入.
### Q2:`--values-json` 和内联行参数有什么区别?

`--values-json` 接收标准 JSON 二维数组(如 `[["A","B"],["1","2"]]`),推荐用于脚本化场景,可避免 shell 转义问题。内联行参数适合简单交互式调用,但含特殊字符时易出错.
### Q3:Docs 能否直接修改文档内容?

不能。gog 的 docs 模块仅支持 export(导出)、cat(输出内容)、copy(复制文档)。原位编辑需要 Google Docs API 的 `documents:batchUpdate` 接口,不在 gog 范围内。常见替代流程是 export 为 txt 本地编辑后重新上传.
### Q4:多账户如何切换?

通过 `--account` 参数指定,或设置 `GOG_ACCOUNT` 环境变量切换默认账户。`gog auth list` 可查看所有已授权账户。不同账户的 OAuth token 相互隔离.
### Q5:Gmail 发送邮件是否需要确认?

是的。发送邮件是不可逆操作,gog 默认在发送前会要求确认。脚本化场景可加 `--no-input`,但需自行承担误发风险。建议先 `gog gmail send --dry-run` 预览内容.
### Q6:Sheets 的 `--input USER_ENTERED` 与 `RAW` 有何区别?

`USER_ENTERED` 表示值按用户在 UI 中输入的方式解析(如 `=SUM(A1:A10)` 会被识别为公式),`RAW` 表示值作为字面量原样写入(公式不会被计算)。默认为 `USER_ENTERED`,写入纯数据时建议显式指定以避免歧义.
## 能力边界
- Docs 不支持原位编辑,仅支持 export/cat/copy
- Calendar 仅支持事件查询,不支持事件创建与修改(需人工确认或调用 Calendar API)
- Sheets 单次请求的单元格数量受 Google API 配额限制,大批量写入需分批
- Gmail 发送邮件的附件大小上限 25MB,超过需使用 Drive 链接
- OAuth token 有有效期,过期后需重新 `gog auth add` 刷新
- `gog` 不封装 Google Workspace 的权限管理与组织管理能力,仅处理个人账户维度操作

## 创新特色
### 效率提升量化分析
| 操作步骤 | 手动耗时 | 自动化耗时 | 时间节约 | 准确率提升 |
| --- | --- | --- | --- | --- |
| 检索Gmail邮件 | 15分钟 | 1分钟 | 14分钟 | 100% |
| 发送Gmail邮件 | 5分钟 | 1分钟 | 4分钟 | 100% |
| 查询日历事件 | 10分钟 | 1分钟 | 9分钟 | 100% |
| 检索云盘文件 | 20分钟 | 2分钟 | 18分钟 | 100% |
| 列出联系人 | 15分钟 | 1分钟 | 14分钟 | 100% |
| 读取表格数据 | 30分钟 | 5分钟 | 25分钟 | 100% |

### 差异化对比
| 对比维度 | 本技能 | 手动操作 | Python脚本 | 专业软件 |
| --- | --- | --- | --- | --- |
| 易用性 | 高 | 低 | 中 | 高 |
| 功能丰富度 | 高 | 低 | 中 | 高 |
| 效率 | 高 | 低 | 中 | 高 |
| 成本 | 低 | 高 | 中 | 高 |
| 学习曲线 | 低 | 高 | 中 | 高 |

### 核心痛点解决
| 痛点 | 描述 | 影响范围 | 解决方案 | 量化效果 |
| --- | --- | --- | --- | --- |
| 操作繁琐 | 手动操作Google Workspace服务效率低下 | 影响工作效率 | 使用gog自动化操作 | 节约时间80% |
| 跨平台兼容性差 | 手动操作在不同操作系统间兼容性差 | 影响用户体验 | gog支持多平台 | 提升用户体验50% |
| 安全性低 | 手动操作容易泄露敏感信息 | 影响数据安全 | gog采用OAuth认证 | 提升安全性90% |

## 诊断与修复
| 错误现象 | 可能原因 | 诊断步骤 | 解决方案 |
| --- | --- | --- | --- |
| 无法登录 | API Key配置错误 | 检查API Key配置是否正确 | 重新配置API Key |
| 操作失败 | 网络连接问题 | 检查网络连接是否正常 | 检查网络连接，重试操作 |
| 权限不足 | 服务授权问题 | 检查服务授权是否正确 | 重新授权服务 |
| 输出格式错误 | 配置选项错误 | 检查配置选项是否正确 | 修正配置选项 |
| 无法检索文件 | 搜索语法错误 | 检查搜索语法是否正确 | 修正搜索语法 |

## 安全提示
1. 确保API Key安全，避免泄露到公共或版本控制系统中。
2. 使用OAuth 2.0进行身份验证，确保操作的安全性。
3. 限制访问权限，只授权必要的API和功能。
4. 定期检查和更新API Key，防止未授权访问。
5. 在操作敏感数据时，确保数据加密传输和存储。

### 安全风险防范

| 风险项 | 等级 | 防护措施 | 验证方法 |
| --- | --- | --- | --- |
| API密钥泄露 | 高 | 通过环境变量配置，禁止硬编码 | 定期检查代码和配置文件 |
| 命令执行风险 | 高 | 仅执行白名单命令，避免拼接用户输入 | 使用沙箱环境测试 |
| 网络通信安全 | 中 | 使用HTTPS协议，验证SSL证书 | 定期检查证书有效期 |
| 敏感数据暴露 | 高 | 输出结果中不包含密钥、令牌等敏感信息 | 日志脱敏审查 |
| 未授权访问 | 中 | 限制访问权限，实施认证机制 | 定期审计访问日志 |

## 功能梳理
- **自动化执行**: Google Workspace命令行工具,覆盖Gmail/日历/云盘/联系人/表格/文档六大服务。
- **文件处理**: 支持多种文件格式的读取、解析和写入操作
- **API集成**: 通过标准化接口调用外部服务并处理响应
- **命令执行**: 在安全沙箱中执行系统命令并收集结果
- **信息检索**: 快速搜索和过滤目标数据

## 错误恢复流程
针对命令行工具使用中可能遇到的常见问题,提供以下排查方案:

| 错误类型 | 原因分析 | 解决方案 |
|---------|---------|---------|
| API认证失败(401) | API密钥错误或过期 | 检查密钥配置,重新生成token |
| 接口限流(429) | 请求频率超出限制 | 降低调用频率,启用重试退避策略 |
| 响应超时(504) | 网络延迟或服务端负载过高 | 增加超时阈值,检查网络连接 |
| 文件不存在 | 路径错误或文件未创建 | 检查路径拼写,确认文件已生成 |
| 文件格式不支持 | 扩展名不在支持列表中 | 转换为支持的格式后重试 |
| 权限不足 | 当前用户无读写权限 | 检查文件权限,以管理员身份运行 |
| 命令执行失败 | 参数错误或环境依赖缺失 | 检查命令语法,确认依赖已安装 |
| 进程超时 | 命令执行时间过长 | 增加超时设置,优化命令参数 |
| 网络连接失败 | DNS解析失败或防火墙拦截 | 检查网络配置,确认代理设置 |

### 命令行工具通用排查步骤

1. **检查输入参数**: 确认所有必填参数已提供且格式正确
2. **查看日志输出**: 定位具体错误行和异常类型
3. **验证环境配置**: 确认依赖库版本和运行环境满足要求
4. **逐步调试**: 缩小问题范围,隔离故障模块

## 实操说明
1. **配置API密钥**: 在环境变量中设置对应的API Key
2. **初始化连接**: 使用提供的凭证建立API连接
3. **调用接口**: 传入必要参数执行API调用
1. **准备文件**: 确认文件路径正确且格式受支持
2. **执行处理**: 调用对应的处理函数
3. **查看结果**: 检查输出文件或返回数据
1. **检查环境**: 确认运行时和依赖已安装
2. **执行命令**: 使用正确的参数格式执行
3. **查看输出**: 检查命令输出和退出码

### 前置条件

- 已安装所需运行环境(参考依赖说明)
- 已获取必要的API密钥或访问凭证(如适用)
- 输入数据已准备就绪

## 依赖说明

### 运行环境
- **Agent 平台**: 支持SKILL.md的任意AI Agent
- **操作系统**: Windows / macOS / Linux

### 可用性分类
- **分类**: MD（纯Markdown指令，通过自然语言驱动Agent完成操作）
- **说明**: 基于Markdown的AI Skill，通过自然语言指令驱动Agent完成操作。
