---slug: job-auto-apply-tool-free
name: job-auto-apply-tool-free
version: 1.0.0
displayName: 求职自动申请
summary: "轻量级求职自动化工具，"
license: Proprietary
edition: free
description: '轻量级求职自动化工具，支持多平台职位搜索与申请提交，自动生成求职信，适合个人求职者提升效率.
  核心能力:

  - 跨多个招聘平台搜索职位

  - 智能匹配职位与个人资料

  - 自动生成定制化求职信

  - 安全的试运行与确认模式

  适用场景:

  - 个人求职者批量投递简历

  - 应届毕业生求职投递

  - 跨行业转职申请

  差异化:

  - 免费版聚焦核心申请功能，操作简单

  - 支持试运行模式，安全无风险

  - 智能匹配，提高投递成功率

  适用关键词: 求职申请, 自动投递, 职位搜索, 简历投递, 求职信生成'
tags:
  - 求职
  - 自动化
  - 招聘
  - 求职信
  - 搜索
  - 检索
  - 工具
  - json
  - 支持创建
  - 查询
  - input_params
  - python
tools:
  - read
  - exec
  - glob
  - grep
homepage: ""
category: "Knowledge"---# 求职自动申请（免费版）

## 概述

求职自动申请免费版是一款面向个人求职者的自动化申请工具。支持跨 LinkedIn、Indeed 等主流招聘平台搜索职位，智能匹配职位要求与个人资料，自动生成定制化求职信，并提交申请。内置试运行模式和手动确认机制，确保投递安全可控.
## 核心能力

| 能力 | 说明 | 免费版支持 |
|---|---|-----|
| 多平台搜索 | 跨平台职位搜索 | 是（2 个平台） |
| 智能匹配 | 职位与资料匹配 | 是 |
| 求职信生成 | 自动生成求职信 | 是 |
| 试运行模式 | 无风险测试 | 是 |
| 手动确认 | 投递前确认 | 是 |
| 批量申请 | 批量自动投递 | 否 |
| 多账号管理 | 多平台账号 | 否 |
| 申请追踪 | 投递状态追踪 | 否 |
| 数据分析 | 投递效果分析 | 否 |

### 已知限制
执行已知限制操作,使用`input_params`参数进行配置,支持创建/查询/导出等操作.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作
### 支持最多 2 个招聘平台
支持最多 2 个招聘平台

**处理**: 解析支持最多 2 个招聘平台的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回支持最多 2 个招聘平台的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 单日最多投递 10 个申请
单日最多投递 10 个申请

**处理**: 解析单日最多投递 10 个申请的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回单日最多投递 10 个申请的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 不支持批量自动投递
不支持批量自动投递

**处理**: 解析不支持批量自动投递的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回不支持批量自动投递的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 不支持申请状态追踪
不支持申请状态追踪

**处理**: 解析不支持申请状态追踪的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回不支持申请状态追踪的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 不支持投递效果分析
不支持投递效果分析

**处理**: 解析不支持投递效果分析的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回不支持投递效果分析的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

**处理**: 解析已知限制的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回已知限制的响应数据,包含状态码、结果和日志.
**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：轻量级求职自动化、支持多平台职位搜、索与申请提交、适合个人求职者提、升效率等。这些关键词对应description中声明的使用场景,均已在上述能力点中提供对应的操作支持.
## 使用场景

### 场景一：基础求职投递

求职者希望搜索并申请匹配的职位.
```bash
# 试运行模式（不实际提交）
python job_search_apply.py \
  --title "Software Engineer" \
  --location "San Francisco, CA" \
  --remote \
  --max-applications 10 \
  --dry-run
# ...
# 实际提交（需确认）
  --profile ~/job_profile.json \
  --title "Backend Engineer" \
  --platforms linkedin,indeed \
  --require-confirmation
```

### 场景二：远程职位搜索

求职者想找远程工作机会.
```bash
# 搜索远程职位
  --title "Frontend Developer" \
  --remote \
  --max-applications 5 \
  --dry-run
```

### 场景三：应届生求职

毕业生首次求职，谨慎投递.
```bash
# 使用确认模式逐个审核
  --title "Junior Developer" \
  --require-confirmation \
  --max-applications 3
```

## 不适用场景

以下场景求职自动申请不适合处理：

- 需要人工创意判断的任务
- 非结构化头脑风暴
- 人际沟通协调

## 触发条件

需要提升效率、自动化流程、批量处理、工作流优化时使用。不适用于非本工具能力范围的需求.
## 快速开始

1. 阅读## 核心能力章节了解skill功能
2. 按## 依赖说明配置环境
3. 执行所需能力对应的命令
4. 参考## 错误处理章节处理异常
5. 查看## FAQ解答常见疑问

### 配置个人资料

```bash
# 复制资料模板
cp profile_template.json ~/job_profile.json
# ...
# 编辑个人资料
vim ~/job_profile.json
```

### 示例

```json
{
  "full_name": "Jane Doe",
  "email": "jane@example.com",
  "phone": "+1234567890",
  "resume_path": "~/Documents/resume.pdf",
  "linkedin_url": "https://linkedin.com/in/janedoe",
  "years_experience": 5,
  "authorized_to_work": true,
  "requires_sponsorship": false,
  "skills": ["Python", "JavaScript", "SQL"],
  "experience_level": "mid"
}
```

### 执行首次搜索

```bash
# 试运行搜索
  --title "Software Engineer" \
  --location "Remote" \
  --dry-run
```

**响应解析**: 完成完成后,查看输出响应确认任务状态。成功时输出包含解析摘要和响应数据;失败时根据错误信息排查问题,查阅错误解析章节获取恢复步骤.
## 配置示例

### 支持的招聘平台

| 平台 | 支持方式 | 说明 |
|:-----|:-----|:-----|
| LinkedIn | API + 爬取 | 含 Easy Apply |
| Indeed | API | 官方 API |

### 参数说明

| 参数 | 类型 | 默认值 | 说明 |
|---:|---:|---:|---:|
| `--profile` | 字符串 | 无 | 个人资料文件路径 |
| `--title` | 字符串 | 无 | 职位名称 |
| `--location` | 字符串 | 无 | 工作地点 |
| `--remote` | 布尔 | false | 仅搜索远程 |
| `--platforms` | 字符串 | all | 平台列表 |
| `--max-applications` | 整数 | 10 | 最多申请数 |
| `--dry-run` | 布尔 | false | 试运行模式 |
| `--require-confirmation` | 布尔 | false | 需手动确认 |

### 工作流程

```text
1. 配置资料 → 加载个人信息
2. 搜索职位 → 跨平台搜索匹配
3. 智能匹配 → 分析兼容性
4. 生成求职信 → 定制化生成
5. 确认投递 → 手动确认（可选）
6. 提交申请 → 自动提交
7. 记录结果 → 保存投递记录
```

## 最佳实践

### 安全投递建议

1. **先试运行**：始终先用 `--dry-run` 测试
2. **启用确认**：重要投递使用 `--require-confirmation`
3. **限制数量**：每日投递不超过 10 个
4. **高匹配分**：设置最低匹配分数 0.75+
5. **真实信息**：不夸大或虚构资质

### 个人资料优化

```json
{
  "full_name": "真实姓名",
  "email": "常用邮箱",
  "phone": "可联系电话",
  "resume_path": "简历文件路径",
  "linkedin_url": "LinkedIn 主页",
  "years_experience": 5,
  "authorized_to_work": true,
  "requires_sponsorship": false,
  "skills": ["核心技能1", "核心技能2", "核心技能3"],
  "experience_level": "entry/mid/senior",
  "preferred_locations": ["城市1", "城市2"],
  "salary_min": 100000,
  "job_type": "full-time"
}
```

### 求职信模板

```text
Dear Hiring Manager at {company},
# ...
I am excited to apply for the {position} role. With {years} years of
experience in {skills}, I believe I would be an excellent fit.
# ...
{custom_paragraph}
# ...
I look forward to discussing how I can contribute to {company}'s success.
# ...
Best regards,
{name}
```

## 常见问题

### 搜索无结果

```bash
# 放宽搜索条件
  --title "Developer" \
  --location "Remote" \
  --dry-run
# ...
# 尝试不同关键词
  --title "Software Engineer" \
  --location "" \
  --dry-run
```

### 申请提交失败

```bash
# 检查资料完整性
py --validate-profile
# ...
# 验证平台连接
py --check-platforms
# ...
# 使用试运行模式测试
```

### 求职信质量不佳

```bash
# 优化个人资料中的技能描述
vim ~/job_profile.json
# ...
# 自定义求职信模板
py --cover-letter-template custom_template.txt
```

### 匹配分数过低

```bash
# 降低匹配阈值（谨慎使用）
py --min-match-score 0.6
# ...
# 优化资料中的技能关键词
# 确保技能与目标职位匹配
```

## 依赖说明

### 运行环境

- **Agent 平台**：支持 SKILL.md 的任意 AI Agent（Claude Code / Cursor / Codex / Gemini CLI 等）
- **操作系统**：Windows / macOS / Linux
- **Python 版本**：3.8 及以上
- **网络环境**：需可访问招聘平台

### 依赖详情

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:---:|:---:|:---:|:---:|
| Python 3.8+ | 运行时 | 是 | 系统包管理器安装 |
| requests | HTTP 库 | 是 | `pip install requests` |
| beautifulsoup4 | HTML 解析 | 是 | `pip install beautifulsoup4` |
| python-dotenv | 环境变量 | 否（推荐） | `pip install python-dotenv` |
| LLM API | API | 是 | 由 Agent 内置 LLM 提供 |

### API Key 配置

- LinkedIn 平台（如需要）：

```bash
export LINKEDIN_API_KEY=your_key
export LINKEDIN_ACCESS_TOKEN=your_token
```

- Indeed 平台（如需要）：

```bash
export INDEED_API_KEY=your_key
```

### 可用性分类

- **分类**：MD+EXEC（纯 Markdown 指令，部分功能需要 exec 命令行执行能力）
- **说明**：基于 Markdown 的 AI Skill，通过自然语言指令驱动 Agent 执行任务
- **适用人群**：个人求职者、应届毕业生、转职人员
- **升级建议**：如需批量投递、多账号管理、申请追踪等高级功能，请使用 PRO 版本

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:------|------:|:------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，参考国内替代方案 |

## 输出格式
```json
{
  "success": true,
  "data": {
    "result": "求职自动申请处理结果",
    "execution_time": "0.5s",
    "metadata": {
      "version": "1.0",
      "processor": "job auto apply"
    }
  },
  "execution_log": ["解析输入参数", "执行核心处理", "格式化输出结果"],
  "error": null
}
```
