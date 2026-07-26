---
slug: "automation-recipe-book"
name: "automation-recipe-book"
version: 1.0.1
displayName: "自动化配方手册(专业版)"
summary: "25+自动化配方库+配方生成器+高级模式+企业模板+调试工具包，支撑从个人到企业的全场景自动化。"
license: "Proprietary"
edition: "pro"
description: |-
  自动化配方手册专业版是面向从个人到企业的全场景自动化配方系统。在免费版8个配方基础上扩展至25+配方（6大类别），新增配方生成器框架、高级模式（条件分支/并行执行/错误处理/重试）、企业自动化模板、调试与监控工具包、配方分享与导入、版本管理与回滚七大高级能力。Use when 需要提升效率、自动化流程、批量处理、工作流优化时使用。不适用于需要人工创意判断的任务.
tags:
  - 自动化配方
  - 工作流编排
  - 企业自动化
  - 配方生成器
  - 流程数字化
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "19.9 CNY/per_use"
pricing_tier: "L2-标准级"
pricing_model: "per_use"

---
# 自动化配方手册(专业版)

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| 自动化配方手册(专业版)配方生成 | 不支持 | 支持 |
| 复杂工作流可视化编排 | 不支持 | 支持 |
| 条件分支与异常重试 | 不支持 | 支持 |
| 定时触发与事件驱动 | 不支持 | 支持 |
| 执行日志与审计追踪 | 不支持 | 支持 |

## 核心能力

> 详细内容已移至 `references/detail.md` - ### 功能一：25+配方库（6大类别）
### 功能二：配方生成器框架
> 详细代码示例已移至 `references/detail.md`

**生成器能力**：
- 自然语言描述需求，自动生成YAML配方
- 自动选择合适的trigger与action类型
- 自动推断参数（如cron频率、通知渠道）
- 生成后自动验证语法与逻辑
- 支持迭代修改（"把通知改成飞书"）

**处理**: 解析功能二：配方生成器框架的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
### 功能三：高级模式
> 详细代码示例已移至 `references/detail.md`

**输入**: 用户提供功能三：高级模式所需的指令和必要参数.
**处理**: 解析功能三：高级模式的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回功能三：高级模式的处理结果,包含执行状态码、结果数据和执行日志。### 功能四：企业自动化模板
> 详细代码示例已移至 `references/detail.md`

**输入**: 用户提供功能四：企业自动化模板所需的指令和必要参数.
**处理**: 解析功能四：企业自动化模板的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回功能四：企业自动化模板的处理结果,包含执行状态码、结果数据和执行日志。### 功能五：调试与监控工具包
```bash
agent recipe visualize --name daily-news --output flowchart.png
# ...
agent recipe trace --name daily-news --last-run
# ...
agent recipe analyze --name daily-news --period 7d
# ...
agent recipe validate --name daily-news
# ...
agent recipe dry-run --name daily-news --mock-input '{"title":"test"}'
```

**调试能力**：
- **可视化**：自动生成配方可视化流程图（Mermaid格式）
- **执行追踪**：逐步显示每个action的输入、输出、耗时
- **性能分析**：识别耗时最长的步骤、失败率最高的步骤
- **试运行**：用mock数据模拟执行，不产生副作用
- **断点调试**：在指定步骤暂停，检查中间状态

### 功能六：配方版本管理与回滚
```bash
agent recipe versions --name daily-news
# ...
agent recipe rollback --name daily-news --to previous
# ...
agent recipe rollback --name daily-news --to v1.2.0
# ...
agent recipe diff --name daily-news --v1 v1.0.0 --v2 v1.1.0
# ...
```

**处理**: 解析功能六：配方版本管理与回滚的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回功能六：配方版本管理与回滚的处理结果,包含执行状态码、结果数据和执行日志。### 功能七：配方分享与导入
```bash
agent recipe export --name daily-news --output daily-news.zip
# ...
agent recipe import --file daily-news.zip
# ...
agent recipe install --from community --name trending-news-monitor
```

**输入**: 用户提供功能七：配方分享与导入所需的指令和必要参数.
**处理**: 解析功能七：配方分享与导入的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
#
## 适用场景

**痛点**：企业内部有大量审批、通知、报表流程，依赖人工流转，效率低且易出错.
**配置**：
```text
1. 启用approval-flow配方，实现多级审批自动流转
2. 启用sla-monitor配方，监控关键流程SLA
3. 启用compliance-check配方，每周合规检查
4. 启用weekly-report配方，自动生成周报
```

**效果**：审批流转从平均2天缩短至4小时，SLA违规率下降70%，合规检查自动化，周报无需手动整理.
## 使用流程

### 60秒上手（升级激活）
专业版完全兼容免费版的目录结构与配方格式：

```bash
ls ~/workspace/automations/recipes/
# ...
cat ~/workspace/automations/config.json | grep edition
```

### 120秒上手（配方生成器）
```text
用户："帮我生成一个配方：每天晚上11点检查我的待办清单，如果有高优先级未完成项，发钉钉提醒我"
# ...
Agent："已生成配方：
  name: todo-urgent-reminder
  trigger: schedule (每天 23:00)
  actions:
    1. 读取待办清单
    2. 筛选高优先级未完成项
    3. 条件判断：是否有未完成项
    4. 发送钉钉通知
  已保存至 ~/workspace/automations/recipes/todo-urgent-reminder.yaml
  是否立即启用？"
```

### 300秒上手（完整企业配置）

> 详细代码示例已移至 `references/detail.md`

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|:-----|:-----|:-----|:-----|
| content | string | 否 | automation-recipe-book处理的内容输入 |,  |
| content | string | 否 | automation-recipe-book处理的内容输入 |, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "book 相关配置参数",
    result: "book 相关配置参数",
    result: "book 相关配置参数",
    "metadata": {
      "template_used": "reviewer",
      "word_count": 0,
      "style": "专业"
    }
  },
  "error": null
}
```

输出模板参考: `assets/output.json`

## 异常处理

| 问题 | 可能原因 | 解决方案 | 优先级 |
|---:|---:|---:|---:|
| 配方不触发 | trigger配置错误 | 验证cron表达式；检查trigger类型 | 高 |
| action执行失败 | 依赖技能未安装或未配置 | 检查requires字段；安装依赖技能 | 高 |
| 生成器配方质量差 | 需求描述不清晰 | 补充细节；迭代修改；手动调整 | 中 |
| 条件分支不生效 | 条件表达式语法错误 | 检查if/elif/else语法；用dry-run验证 | 高 |
| 并行执行结果丢失 | wait策略配置错误 | 检查wait参数（all/any/first_n） | 中 |
| 无效 | on_failure未配置或retry次数为0 | 配置on_failure段；设置合理retry次数 | 高 |
| 配方性能差 | action过多或串行执行 | 优化action数量；启用并行执行 | 中 |
| 版本回滚失败 | 版本文件损坏或不存在 | 检查版本目录；从git恢复 | 高 |
| 可视化生成失败 | Mermaid语法错误或action类型不支持 | 检查action类型；更新可视化工具 | 低 |
| 导入配方失败 | 格式不兼容或依赖缺失 | 检查配方格式；安装依赖技能 | 中 |
| 企业模板对接失败 | 企业系统API变更 | 检查API可用性；更新模板配置 | 高 |

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Python**: 3.8+（用于配方验证与可视化脚本）

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:---:|:---:|:---:|:---:|
| LLM API | API | 必需 | 由Agent平台内置LLM提供 |
| 调度器 | 内置 | 必需 | Agent平台调度能力 |
| PyYAML | Python库 | 配方解析必需 | `pip install pyyaml` |
| Mermaid CLI | 工具 | 可视化必需 | `npm install -g @mermaid-js/mermaid-cli` |

### API Key 配置
- 本技能核心功能无需额外API Key
- 配方生成器使用Agent平台内置LLM
- 配方中引用的外部服务由对应技能管理API Key
- 告警webhook通过环境变量配置

### 可用性分类
- **分类**: MD+EXEC（）
- **说明**: 基于Markdown的AI Skill，

## 案例展示

### 场景二：团队协作编排（项目经理角色）
**痛点**：团队成员任务分配不透明，进度追踪困难，会议纪要无人整理.
**配置**：
```text
1. 用配方生成器创建"任务自动分配"配方（按技能匹配任务）
2. 启用meeting-reminder配方，会议前提醒
3. 启用meeting-notes配方，会议后自动生成纪要并分发
4. 启用weekly-report配方，每周五自动汇总进度
```

**效果**：任务分配自动化且更合理，会议纪要5分钟内生成分发，周报自动汇总无需催收.
### 场景三：数据处理流水线（数据工程师角色）
**痛点**：数据ETL流程复杂，步骤间有依赖，需要断点恢复与错误处理.
**配置**：

**效果**：并行抽取缩短40%耗时，校验步骤保障数据质量，失败自动重试，无需夜间值守.
### 场景四：内容运营自动化（内容运营角色）
**痛点**：需要每日在多个平台发布内容，手动操作耗时且容易遗漏.
**配置**：
```text
1. 启用content-generate配方，每日生成3篇候选文章
2. 启用multi-publish配方，工作日9点自动发布到3个平台
3. 启用seo-optimize配方，自动优化标题与关键词
4. 启用social-schedule配方，社媒内容排期发布
```

**效果**：内容生产与发布全自动化，运营人员从执行者变为审核者，产能提升3倍.
## 常见问题

### Q1：免费版与专业版有什么区别？
免费版提供8个基础配方与结构解析。专业版新增7大功能：25+配方库（6大类）、配方生成器、高级模式（条件分支/并行/错误处理）、企业模板、调试工具包、版本管理、配方分享。此外提供多角色场景指南、性能优化策略和多平台集成示例.
### Q2：配方生成器如何工作？
用户用自然语言描述需求（如"每天检查待办，高优先级发钉钉"），生成器分析需求后自动选择trigger与action类型，推断参数，生成YAML配方，并自动验证语法与逻辑。支持迭代修改（"把钉钉改成飞书"）.
### Q3：高级模式支持哪些控制流？
支持：条件分支（if/elif/else）、并行执行（parallel+wait策略）、循环（loop+终止条件）、子配方调用（call_recipe）、错误处理（on_failure+retry+backoff）、异常捕获（try/catch）.
### Q4：企业模板包含哪些？
包含：多级审批流自动化、SLA监控与告警、合规检查（GDPR/SOC2/ISO27001）、数据治理流程、访问权限审计、报告自动生成。模板可按企业需求定制参数.
### Q5：调试工具包如何帮助排查问题？
提供5大工具：可视化（生成流程图）、执行追踪（逐步查看输入输出）、性能分析（识别瓶颈步骤）、试运行（mock数据模拟）、断点调试（指定步骤暂停检查）。新配方建议先试运行验证.
### Q6：版本管理支持回滚吗？
支持。每次配方变更自动保存版本，最多保留20个版本。可回滚到上一版本或指定版本，可对比两个版本差异。配置`auto_rollback_on_failure: true`后，配方执行连续失败3次自动回滚到上一稳定版本.
### Q7：能分享配方给团队吗？
可以。导出配方为zip包（含YAML与依赖说明），团队成员导入即可使用。也可通过社区配方市场分享与安装热门配方。导入的配方会自动验证兼容性.
### Q8：配方能调用其他技能吗？
可以。配方中的action可引用任何已安装的技能（如fetch、mail、browser）。在action的`requires`字段声明依赖技能，调度器会自动加载。未安装的技能会提示用户安装.
### Q9：25+配方都开箱即用吗？
大部分配方修改参数后即可使用（如改URL、通知渠道）。部分企业模板（如审批流）需要与企业现有系统对接，需额外配置。每个配方都有详细的参数说明与前置条件说明.
### Q10：配方执行失败会怎样？
根据`on_failure`配置处理：
- `retry`：自动重试N次（支持指数退避）
- `notify`：通知指定渠道
- `escalate`：升级通知上级
- `auto_rollback`：回滚到上一版本
未配置on_failure时，仅记录日志不重试.
### Q11：能同时运行多少个配方？
无硬性限制，但建议根据Agent资源合理安排。高频配方（每分钟级）不超过5个，中频（每小时级）不超过20个，低频（每日级）无限制。调度器会自动错峰执行，避免资源竞争.
## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:------|------:|:------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

