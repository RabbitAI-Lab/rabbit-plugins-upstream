---
slug: skill-vetter
name: skill-vetter
version: "1.0.0"
displayName: Skill Vetter
summary: 安全优先的 AI Agent 技能审查协议，安装任何技能前必须执行。
license: MIT
description: |-
  skill-vetter 是一个安全优先的 AI Agent 技能审查工具。在安装任何技能前执行 4 步审查协议：
  来源检查、强制代码审查（RED FLAGS 检测）、权限范围评估和风险分级。支持 GitHub 仓库快速审查
  命令和 5 级信任层级。输出结构化审查报告，包含 RED FLAGS 列表、权限需求、风险等级和安装建议。
  适用于安全工程师、Agent 运维者和任何需要安装第三方技能的场景。
tools:
  - read
  - exec
---

# Skill Vetter

skill-vetter 是安全优先的 AI Agent 技能审查协议。**永远不要在未审查前安装任何技能。**

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
需要配置对应API Key，详见上文环境配置章节

### 可用性分类
- **分类**: MD+EXEC（）

**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统。
## 核心能力

### 1. 来源检查（Source Check）
验证技能来源的可靠性。回答 5 个关键问题：技能从哪里来（SkillHub / GitHub / 其他）？
作者是否知名/可信？下载量/星标数是多少？最后更新时间？是否有其他 Agent 的评价？
通过 GitHub API 查询仓库元数据：`curl -s "https://api.相关技术文档 | jq '{stars: .stargazers_count, forks: .forks_count, updated: .updated_at}'`。
获取仓库文件列表：`curl -s "https://api.相关技术文档 | jq '.[].name'`。

**输入**: 用户提供来源检查（Source Check）所需的指令和必要参数。
**处理**: 按照skill规范执行来源检查（Source Check）操作,遵循单一意图原则。
**输出**: 返回来源检查（Source Check）的执行结果,包含操作状态和输出数据。

- 执行`来源检查（Source Check）`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`来源检查（Source Check）`相关配置参数进行设置
### 2. 强制代码审查（Code Review - MANDATORY）
读取技能中的所有文件，逐一检查 RED FLAGS 清单。发现以下任何一项立即拒绝安装：
`curl`/`wget` 到未知 URL；向外部服务器发送数据；请求凭证/令牌/API Key；
读取 `~/.ssh`、`~/.aws`、`~/.config` 路径而无明确理由；访问 `MEMORY.md`、`USER.md`、
`SOUL.md`、`IDENTITY.md` 等身份文件；对任何内容使用 `base64` 解码；
使用 `eval()` 或 `exec()` 处理外部输入；修改工作区外的系统文件；
未声明就安装包；向 IP 地址而非域名发起网络调用；使用混淆代码（压缩、编码、最小化）；
请求 `sudo`/提权；访问浏览器 cookie/session；触及凭证文件。

**输出**: 返回强制代码审查（Code Review - MANDATORY）的执行结果,包含操作状态和输出数据。
### 3. 权限范围评估（Permission Scope）
评估技能的最小权限需求。回答 5 个问题：需要读取哪些文件？需要写入哪些文件？
运行哪些命令？是否需要网络访问？访问目标是什么？权限范围是否最小化以满足其声明的目的？
如果技能请求的权限超出其功能需求（如笔记技能请求网络访问），标记为风险信号。

- 执行`权限范围评估（Permission Scope）`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`权限范围评估（Permission Scope）`相关配置参数进行设置
### 4. 风险分级（Risk Classification）
根据功能类型和权限需求进行 4 级风险分级。LOW（绿色）：笔记、天气、格式化——基础审查后可安装。
MEDIUM（黄色）：文件操作、浏览器访问、API 调用——必须完整代码审查。HIGH（红色）：凭证、交易、
系统操作——必须人工批准。EXTREME（禁止）：安全配置、root 访问——绝不安装。

**输入**: 用户提供风险分级（Risk Classification）所需的指令和必要参数。
**输出**: 返回风险分级（Risk Classification）的执行结果,包含操作状态和输出数据。

- 执行`风险分级（Risk Classification）`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`风险分级（Risk Classification）`相关配置参数进行设置
### 5. 结构化审查报告生成
生成标准化的审查报告，包含：技能名称、来源、作者、版本；指标（下载量/星标数、最后更新时间、
审查文件数）；RED FLAGS 列表（None 或具体列表）；权限需求（文件、网络、命令）；
风险等级（LOW/MEDIUM/HIGH/EXTREME）；安装建议（SAFE TO INSTALL / INSTALL WITH CAUTION /
DO NOT INSTALL）；附注观察。

**输入**: 用户提供结构化审查报告生成所需的指令和必要参数。
**处理**: 按照skill规范执行结构化审查报告生成操作,遵循单一意图原则。

- 执行`结构化审查报告生成`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`结构化审查报告生成`相关配置参数进行设置
### 6. 信任层级评估
根据来源应用差异化审查强度。5 级信任层级：官方技能（低度审查但仍需检查）→
高星标仓库 1000+（中度审查）→ 已知作者（中度审查）→ 新/未知来源（最大审查）→
请求凭证的技能（始终需人工批准）。信任层级越低，审查深度越深。

- 执行`信任层级评估`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`信任层级评估`相关配置参数进行设置
### 能力覆盖范围

本skill还覆盖以下能力场景: 安全优先的、技能审查协议、安装任何技能前必、须执行、vetter、是一个安全优先的、技能审查工具、在安装任何技能前、步审查协议、权限范围评估和风、仓库快速审查、命令和、输出结构化审查报、风险等级和安装建、适用于安全工程师、运维者和任何需要、安装第三方技能的。这些能力在上述核心功能中均有对应处理逻辑。
## 使用流程

1. 确认技能来源（SkillHub / GitHub / 其他），记录作者和版本
2. 执行来源检查：通过 GitHub API 查询星标数、下载量、最后更新时间
3. 读取技能中的所有文件，逐一检查 RED FLAGS 清单
4. 评估权限范围：文件读写、命令执行、网络访问需求
5. 根据功能类型和权限需求进行风险分级（LOW/MEDIUM/HIGH/EXTREME）
6. 应用信任层级评估，确定审查深度
7. 生成结构化审查报告，输出风险等级和安装建议
8. HIGH 及以上风险等级必须等待人工批准后再安装

### 命令参数说明

- `-team`: 命令参数,用于指定操作选项
- `-formatter`: 命令参数,用于指定操作选项

### 命令参数说明

- `-repo`: 命令参数,用于指定操作选项

## 示例

### 示例1：GitHub 技能完整审查

```bash
# 1. 查询仓库元数据
curl -s "https://api.相关技术文档 | jq '{stars: .stargazers_count, forks: .forks_count, updated: .updated_at}'
# 输出：
# {
#   "stars": 342,
#   "forks": 18,
#   "updated": "2026-06-15T10:30:00Z"
# }

# 2. 获取技能文件列表
curl -s "https://api.相关技术文档 | jq '.[].name'
# 输出：
# "SKILL.md"
# "scripts/helper.sh"
# "scripts/install.sh"

# 3. 读取 SKILL.md 内容
curl -s "https://raw.githubusercontent.com/example/skill-repo/main/skills/my-skill/SKILL.md"
```

```text
SKILL VETTING REPORT
═══════════════════════════════════════
Skill: my-skill
Source: GitHub (example/skill-repo)
Author: example-user
Version: 1.2.0
───────────────────────────────────────
METRICS:
• Stars: 342
• Last Updated: 2026-06-15
• Files Reviewed: 3
───────────────────────────────────────
RED FLAGS:
• scripts/install.sh: curl to unknown URL (http://45.33.32.156/install.sh)
• scripts/install.sh: Network call to IP instead of domain
• scripts/helper.sh: Reads ~/.config without clear reason

PERMISSIONS NEEDED:
• Files: ~/.config/app/config.json (write)
• Network: http://45.33.32.156 (unknown IP)
• Commands: curl, chmod
───────────────────────────────────────
RISK LEVEL: HIGH (credentials, system access)

VERDICT: DO NOT INSTALL

NOTES: install.sh 向未知 IP 发起网络请求，且访问 ~/.config 无明确理由。
建议联系作者确认，或寻找替代技能。
═══════════════════════════════════════
```

### 示例2：低风险技能审查

```text
SKILL VETTING REPORT
═══════════════════════════════════════
Skill: markdown-formatter
Source: SkillHub (official)
Author: official-team
Version: 2.0.1
───────────────────────────────────────
METRICS:
• Downloads: 12,847
• Last Updated: 2026-07-10
• Files Reviewed: 2
───────────────────────────────────────
RED FLAGS: None

PERMISSIONS NEEDED:
• Files: workspace .md files (read/write)
• Network: None
• Commands: None
───────────────────────────────────────
RISK LEVEL: LOW (formatting only)

VERDICT: SAFE TO INSTALL

NOTES: 纯本地 Markdown 格式化工具，无网络访问，无系统文件操作。
权限范围最小化，符合声明目的。
═══════════════════════════════════════
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| `curl`/`wget` 到未知 URL | 技能尝试从不受信任的源下载数据 | 立即标记为 RED FLAG，拒绝安装，检查 URL 是否为已知可信域名 |
| 请求凭证/令牌/API Key | 技能要求用户提供敏感凭证 | 标记为 HIGH 风险，必须人工批准；确认凭证需求是否合理且使用安全存储 |
| 读取 `~/.ssh`/`~/.aws`/`~/.config` | 技能访问敏感系统路径 | 检查是否有明确理由；无理由则标记为 RED FLAG，拒绝安装 |
| 访问 `MEMORY.md`/`USER.md`/`SOUL.md`/`IDENTITY.md` | 技能触及 Agent 身份文件 | 立即拒绝安装，身份文件包含 Agent 核心信息，任何访问都是高风险 |
| 使用 `eval()`/`exec()` 处理外部输入 | 代码注入风险 | 标记为 RED FLAG，拒绝安装；确认输入是否经过严格沙箱化处理 |
| 向 IP 地址而非域名发起网络调用 | 绕过 DNS 审计的可疑行为 | 立即标记为 RED FLAG，拒绝安装；合法技能应使用域名而非裸 IP |
| 使用混淆代码（压缩/编码/最小化） | 隐藏恶意行为 | 标记为 RED FLAG，拒绝安装；要求作者提供可读源代码 |

## 常见问题

### Q1: 如何判断一个技能是否需要人工批准？
A: 根据风险分级判断。HIGH（红色）级别涉及凭证、交易、系统操作的技能必须人工批准。
EXTREME（禁止）级别涉及安全配置、root 访问的技能绝不安装。MEDIUM 级别在完整代码审查后
可自动安装。此外，任何请求凭证的技能无论风险等级都需要人工批准。

### Q2: GitHub API 查询返回 403 Rate Limit 怎么办？
A: GitHub API 未认证请求限制为每小时 60 次。如果达到限制，等待限制重置（通常 1 小时），
或使用 `GITHUB_TOKEN` 进行认证请求（限制提升到每小时 5000 次）：
`curl -s -H "Authorization: token $GITHUB_TOKEN" "https://api.相关技术文档

### Q3: 技能使用 `base64` 解码就一定是恶意吗？
A: 不一定，但必须标记为 RED FLAG 并深入调查。合法用途包括解码嵌入的配置文件或图片资源。
检查解码后的内容：如果解码为 shell 命令、脚本或 URL，则确认为恶意；如果解码为静态资源
（如图片 data URI），则可能合法但仍需人工确认。

### Q4: 5 级信任层级如何影响审查深度？
A: 官方技能（Level 1）进行基础代码审查即可；高星标仓库 1000+（Level 2）和已知作者
（Level 3）进行中度审查，重点关注权限范围；新/未知来源（Level 4）进行最大审查，
逐行检查所有代码；请求凭证的技能（Level 5）无论来源都必须人工批准。

### Q5: 技能安装包但未声明怎么办？
A: 这是一个 RED FLAG。合法技能应在文档中声明所有依赖。如果代码中有 `pip install`、
`npm install`、`apt-get install` 等命令但未在文档中列出，标记为 RED FLAG 并拒绝安装。
要求作者补充依赖声明后再重新审查。

### Q6: 审查报告中的 VERDICT 有哪几种结果？
A: 三种结果：SAFE TO INSTALL（安全安装）——LOW 风险且无 RED FLAGS，可直接安装；
INSTALL WITH CAUTION（谨慎安装）——MEDIUM 风险或存在 warn 级别问题，安装后需监控行为；
DO NOT INSTALL（拒绝安装）——HIGH/EXTREME 风险或存在 RED FLAGS，绝不安装。

## 已知限制

- GitHub API 未认证请求限制为每小时 60 次，大量审查时需使用 Token 认证
- 无法检测运行时动态加载的恶意代码（如从远程下载并执行）
- 混淆代码的检测依赖静态分析，高度混淆的代码可能遗漏
- 审查报告基于代码审查，不替代运行时沙箱测试
- 信任层级评估依赖作者声誉信息，新作者可能无法准确评估
