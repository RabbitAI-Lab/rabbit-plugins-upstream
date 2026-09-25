---

slug: github-manager
name: "github-manager"
version: 1.0.1
displayName: "GitHub管理器(专业版)"
summary: "全功能GitHub管理工具,含批量操作、GraphQL高级查询、自动化工作流、团队仪表盘与Webhook管理,适合团队企业级协作。"
summary_zh: "全功能GitHub管理工具,含批量操作、GraphQL高级查询、自动化工作流、团队仪表盘与Webhook管理,适合团队企业级协作。"
license: "MIT"
edition: "pro"
description: |-
  GitHub管理器(专业版)是企业级GitHub协作管理工具,在免费版基础查询能力上,扩展批量操作、GraphQL高级查询、自动化工作流、团队仪表盘与Webhook管理等高级能力。核心能力:
  - 批量Issue/PR操作: 批量关闭、打标签、分配负责人、迁移
  - GraphQL高级查询: 复杂关联查询、跨仓库聚合、深度分页
  - 自动化工作流: 定时检查、自动分配、状态流转、通知告警
  - 团队仪表盘: 多仓库汇总、成员贡献统计、燃尽图
  - Webhook管理: 事件订阅、自动触发、回调配置
  - 安全审计: 权限审查、敏感信息扫...
tags:
  - GitHub
  - 团队协作
  - 自动化
  - 企业版
  - 版本控制
  - Git
  - 开发工具
  - gh-manager
  - repo
  - issue
  - owner
  - webhook
tools:
  - read
  - exec
  - write
homepage: ""
category: "Development"

---

> **核心功能**: 本技能提供等高级能力等能力。
# GitHub管理器(专业版)
## 专业版增值服务
| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| GitHub管理器(专业版)功能GitHub管理 | 不支持 | 支持 |
| GitHub管理器(专业版)raphQL高级查询 | 不支持 | 支持 |
| GitHub管理器(专业版)与Webhook管理 | 不支持 | 支持 |
| 代码静态分析与质量评分 | 不支持 | 支持 |
| 依赖漏洞检测与升级建议 | 不支持 | 支持 |
## 能力总览
### 批量Issue/PR操作
```bash
gh-manager issue batch-close --repo owner/repo --label stale --reason "not_planned"
gh-manager issue batch-label --repo owner/repo --issues 1,3,5,7 --labels "bug,priority:high"
gh-manager issue batch-assign --repo owner/repo --issues 10-20 --assignee "alice"
gh-manager issue migrate --from owner/repo-a --to owner/repo-b --issues 1-50
gh-manager issue batch-reopen --repo owner/repo --issues 30,32,35
```
批量操作安全机制:
- **预演模式**: `--dry-run`先预览变更,不实际执行
- **确认机制**: 影响超过10条记录时需二次确认
- **回滚支持**: 每次批量操作生成回滚脚本
- **速率控制**: 自动遵守API限速,避免触发429
### GraphQL高级查询
```bash
gh-manager graphql query --file queries/cross_repo_prs.graphql --vars '{"author":"alice"}'
gh-manager graphql query --file queries/dependency_graph.graphql --vars '{"repo":"owner/repo"}'
gh-manager graphql paginate --file queries/all_issues.graphql --limit 1000
```
GraphQL查询示例:
```graphql
query teamContributions($logins: [String!]!, $since: DateTime!) {
  users(filter: {logins: $logins}) {
    login
    contributionsCollection(from: $since) {
      pullRequestContributions(first: 100) {
        totalCount
        nodes {
          pullRequest {
            repository { nameWithOwner }
            state
            additions
            deletions
          }
        }
      }
    }
  }
}
```
- 异常时参考错误处理章节进行恢复
- 关键参数: `graphql高级查询` 选项
### 自动化工作流
```bash
gh-manager automation create --name "stale-issue-triage" \
  --trigger "schedule:0 9 * * 1" \
  --condition "label:none AND updated:<7d" \
  --action "add-label:stale AND comment:'此Issue已7天未更新,7天后将自动关闭'"
gh-manager automation list
gh-manager automation run --name "stale-issue-triage" --repo owner/repo
gh-manager automation history --name "stale-issue-triage" --last 10
```
自动化场景模板:
| 模板 | 触发条件 | 动作 |
|:-----|:-----|:-----|
| Stale Issue | 7天无更新 | 加stale标签,14天后关闭 |
| Auto Assign | 新Issue创建 | 按轮询分配给团队成员 |
| PR Review Reminder | PR 24h未review | 通知指定reviewer |
| CI Failure Alert | 工作流失败 | 发送通知到IM |
| Branch Cleanup | PR合并后 | 删除已合并分支 |
| Release Notes | 发布Release | 自动生成变更日志 |
### 团队仪表盘
```bash
gh-manager dashboard weekly --repos "owner/repo1,owner/repo2" --team "alice,bob,carol" --format pdf
gh-manager dashboard contributions --repos "owner/repo1" --period 30d
gh-manager dashboard burndown --repo owner/repo --milestone "v2.0"
gh-manager dashboard summary --org my-org --period week
```
仪表盘维度:
- Issue/PR数量与状态分布
- 成员贡献排名(提交、PR、review)
- 平均响应时间与关闭周期
- CI/CD成功率与平均时长
- 标签分布与趋势
### Webhook管理
```bash
gh-manager webhook list --repo owner/repo
gh-manager webhook add --repo owner/repo \
  --url "https://hooks.example.com/github" \
  --events "issues,pull_request,push" \
  --secret "$WEBHOOK_SECRET"
gh-manager webhook test --repo owner/repo --id 123 --event "issues"
gh-manager webhook delete --repo owner/repo --id 123
```
### 安全审计
```bash
gh-manager audit permissions --repo owner/repo --format csv
gh-manager audit secrets --repo owner/repo --depth 100
gh-manager audit compliance --org my-org --standard SOC2 --format pdf
gh-manager audit tokens --org my-org --period 90d
```
## 部署指引
1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理
> 详细的输入输出格式请参考下方章节说明。
## 适用范围
### 场景1 -开源项目Issue triage自动化
用户意图: "开源项目Issue太多,需要自动化triage流程。"
实施方案:
1. 创建"stale-issue-triage"自动化规则(7天无更新加标签,14天关闭)
2. 创建"auto-assign"规则(新Issue按标签分配给maintainer)
3. 创建"bug-report-template"规则(缺少复现步骤的Issue自动回复模板)
4. 每周生成triage报告,review未处理Issue
### 场景2 -多仓库团队管理
用户意图: "团队管理5个仓库,需要统一视图。"
实施方案:
1. 使用`gh-manager dashboard summary --org my-org`汇总多仓库状态
2. 配置跨仓库Webhook,统一接收事件
3. 设置CI失败自动告警(通知到IM)
4. 每月生成团队贡献报告
### 场景3 -安全合规审计
用户意图: "准备SOC2审计,需要GitHub权限与操作记录。"
实施方案:
1. 运行`gh-manager audit permissions`导出权限矩阵
2. 运行`gh-manager audit secrets`扫描敏感信息
3. 运行`gh-manager audit compliance --standard SOC2`生成合规报告
4. 导出90天操作日志作为审计证据
### 场景4 -大规模Issue迁移
用户意图: "要把旧仓库的200个Issue迁移到新仓库。"
实施方案:
1. 使用`--dry-run`预演迁移,确认映射关系
2. 执行`gh-manager issue migrate --from old --to new --issues 1-200`
3. 自动保留原始标签、assignee、评论
4. 生成迁移报告,核对数量
## 操作流程
### 第1步:安装与认证
```bash
pip install gh-manager[pro]
gh auth login
gh-manager version
gh-manager status
```
### 第2步:配置团队
```bash
gh-manager team init --org my-org
gh-manager team add --members "alice,bob,carol"
gh-manager repo add --repos "owner/repo1,owner/repo2,owner/repo3"
```
### 第3步:启用自动化
```bash
gh-manager automation enable --template stale-issue-triage
gh-manager automation enable --template ci-failure-alert --notify "im:#devops"
gh-manager automation list --enabled
```
### 第4步:生成仪表盘
```bash
gh-manager dashboard weekly --format pdf --output weekly-report.pdf
gh-manager dashboard live --port 8080
```
## 输入规范
| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| content | string | 否 | github-manager处理的内容输入 |, 默认: 全部维度 |
| strict_level | string | 否 | 审查严格度, 可选: strict/normal/loose, 默认: normal |
## 返回格式
```json
{
  "success": true,
  "data": {
    "overall_grade": "A",
    "total_score": 92,
    "max_score": 100,
    "summary": "处理完成",
    "details": [
      {
        "item": "代码风格",
        "status": "pass",
        "score": 95,
        "comment": "符合规范"
      },
      {
        "item": "安全合规",
        "status": "warn",
        "score": 80,
        "comment": "符合规范"
      }
    ],
    "improvements": [
      {
        "priority": "high",
        "suggestion": "建议优化",
        "expected_gain": "+5分"
      },
      {
        "priority": "medium",
        "suggestion": "建议优化",
        "expected_gain": "+3分"
      }
    ]
  },
  "error": null
}
```
## 异常处置
| 错误场景 | 原因 | 处理方式 |
|:---:|:---:|:---:|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 |
## 环境要求
### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux
- **gh CLI**: 2.0+(GitHub官方命令行工具,作为底层依赖)
- **Python**: 3.8+(运行gh-manager CLI)
- **Node.js**: 16+(可选,用于实时仪表盘)
### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:------|------:|:------|:------|
| gh-manager[pro] | CLI工具 | 必需 | `pip install gh-manager[pro]` |
| gh | CLI工具 | 必需 | `brew install gh` |
| jq | 命令行工具 | 可选 | `brew install jq` |
| GraphQL client | Python库 | 必需 | 随gh-manager安装 |
| GitHub账号 | 在线服务 | 必需 | 注册GitHub账号 |
| LLM API | API | 必需 | 由Agent平台内置LLM提供 |
### API Key 配置
- **GitHub认证**: 通过`gh auth login`完成OAuth,token存储于`~/.config/gh/hosts.yml`
- **Webhook Secret**: 通过环境变量`WEBHOOK_SECRET`配置,加密存储
- **IM通知Token**: 通过环境变量配置(如Slack/钉钉的webhook URL)
- **Token权限**: 建议包含`repo`、`workflow`、`read:org`、`admin:org_hook`
- **禁止**: 在SKILL.md或脚本中硬编码任何Token或Secret
### 可用性分类
- **分类**: MD+EXEC+CLI+DAEMON(Markdown指令+命令行工具+自动化守护)
- **说明**: 基于Markdown的AI Skill，高级功能需要gh-manager CLI与自动化守护进程
## 案例展示
### 完整专业版配置
```json
{
  "edition": "pro",
  "github": {
    "auth_mode": "oauth",
    "default_scope": ["repo", "workflow", "read:org", "admin:org_hook"]
  },
  "team": {
    "org": "my-org",
    "members": ["alice", "bob", "carol"],
    "repos": ["owner/repo1", "owner/repo2", "owner/repo3"]
  },
  "automation": {
    "enabled": true,
    "rules": [
      {
        "name": "stale-issue-triage",
        "trigger": "schedule:0 9 * * 1",
        "condition": "label:none AND updated:<7d",
        "action": "add-label:stale"
      },
      {
        "name": "ci-failure-alert",
        "trigger": "workflow_run:completed:failure",
        "action": "notify:im:#devops"
      }
    ]
  },
  "dashboard": {
    "enabled": true,
    "port": 8080,
    "refresh_interval": 300
  },
  "audit": {
    "enabled": true,
    "log_retention": 365,
    "alert_on_secret": true
  }
}
```
### 自动化规则示例
```yaml
- name: auto-assign-by-label
  description: 按Issue标签自动分配负责人
  trigger:
    type: event
    event: issues
    action: opened
  condition:
    label: bug
  action:
    type: assign
    strategy: round_robin
    team: [alice, bob, carol]
- name: pr-review-sla
  description: PR review SLA监控
  trigger:
    type: schedule
    cron: "0 10 * * *"
  condition:
    pr_state: open
    review_age: ">24h"
  action:
    type: notify
    channel: im
    target: "#pr-reviews"
    message: "PR #"manager_result" 待review已超过24小时"
```
## 疑问解答
### Q1: 批量操作会不会触发GitHub限速?
A: 专业版自动遵守API限速(5000请求/小时),超限时自动排队等待。大批量操作(>100条)建议在低峰期执行,并启用`--rate-limit wait`模式.
### 错误恢复步骤
| 错误场景(续)| 原因 | 处理方式 |
|----:|:----|----:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 请求重试；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |
## 使用约束
A: GitHub GraphQL API有复杂度评分限制(单次查询≤500000点)。专业版会自动计算复杂度,超限时建议拆分查询或使用分页.
### Q3: 自动化规则失败会通知吗?
A: 会。自动化规则执行失败时,自动发送通知到配置的channel(邮件/IM)。同时记录到`automation_history`表,可通过`gh-manager automation history --failed`查看.
### Q4: 团队仪表盘数据多久更新一次?
A: 实时仪表盘默认5分钟刷新一次(可配置)。周报/月报在生成时全量拉取。建议启用数据缓存,降低API消耗.
### Q5: Webhook secret如何管理?
A: 通过环境变量`WEBHOOK_SECRET`配置,加密存储于`~/.gh-manager/secrets.enc`。禁止在配置文件中明文存储。支持按仓库配置不同secret.
### Q6: 安全审计会扫描哪些敏感信息?
A: 扫描内容包括: API Key、密码、私钥、token等(基于正则与熵值检测)。支持自定义扫描规则。发现敏感信息会自动告警并生成Issue.
### Q7: 如何导出审计报告给合规团队?
A: 运行`gh-manager audit compliance --standard SOC2 --format pdf --output audit.pdf`,支持SOC2、ISO27001、GDPR等标准。报告包含权限矩阵、操作日志、敏感信息扫描结果.
### Q8: 多组织场景如何管理?
A: 通过`gh-manager org add`添加多个组织,切换时用`--org`参数指定。仪表盘支持跨组织汇总视图.
### Q9: 自动化规则支持哪些触发条件?
A: 支持: (1)定时(cron表达式); (2)事件(Issue/PR/Push/Release等); (3)状态变化(标签添加、状态流转); (4)外部webhook。可组合多条件.
### Q10: 专业版支持GitHub Enterprise吗?
A: 支持。配置`GITHUB_ENTERPRISE_HOST`环境变量即可连接Enterprise Server。所有功能在Enterprise环境下均可用.
## 补充限制说明
- 需要LLM支持
- API调用依赖第三方服务的可用性与稳定性
- 免费版有调用次数限制与并发限制
## 问题排查手册
| 错误现象 | 可能原因 | 诊断步骤 | 解决方案 |
| --- | --- | --- | --- |
| 批量操作失败 | GitHub API 限制触发 | 检查操作数量是否超过限制，使用`--rate-limit wait`模式等待或分批执行 | 降低操作频率，分批执行或调整API限速策略 |
| GraphQL查询无响应 | 网络问题或查询复杂度过高 | 检查网络连接，简化查询或分页查询 | 确保网络连接正常，简化查询或分页查询 |
| 自动化规则未按预期触发 | 触发条件配置错误 | 检查触发条件配置是否正确，确认事件类型和状态 | 重新配置触发条件，确保正确设置事件类型和状态 |
| 团队仪表盘数据缺失 | 仓库配置错误 | 检查仓库是否正确添加到团队配置中 | 确保仓库已添加到团队配置，重新配置或添加仓库 |
| Webhook未收到通知 | Webhook配置错误 | 检查Webhook URL和事件配置是否正确 | 重新配置Webhook，确保URL和事件正确设置 |
## 安全规范
| 风险项 | 等级 | 防护措施 | 验证方法 |
| --- | --- | --- | --- |
| 敏感信息泄露 | 高 | 使用环境变量存储敏感信息，加密存储 | 定期审计环境变量，确保敏感信息未明文存储 |
| 权限滥用 | 中 | 定期审查用户权限，限制不必要的权限 | 定期运行`gh-manager audit permissions`，审查权限分配 |
| API密钥泄露 | 高 | 使用OAuth令牌代替API密钥，限制令牌权限 | 确保使用OAuth令牌，并限制令牌权限 |
| 自动化规则误触发 | 中 | 严格配置触发条件和动作，测试自动化规则 | 测试自动化规则，确保触发条件和动作正确 |
| Webhook安全 | 高 | 使用HTTPS，配置Webhook Secret，验证请求来源 | 确保Webhook使用HTTPS，配置Secret，并验证请求来源 |
## 创新特色
| 效率提升量化分析 |
| --- |
| 批量操作 | 减少手动操作时间，提升效率50%以上 |
| GraphQL高级查询 | 减少查询时间，提升效率30%以上 |
| 自动化工作流 | 减少人工干预，提升效率40%以上 |
| 团队仪表盘 | 提供实时数据，提升决策效率20%以上 |
| 差异化对比表格 |
| --- |
| 功能 | GitHub管理器(专业版) | 其他工具 |
| --- | --- | --- |
| 批量操作 | 支持批量关闭、标签、分配、迁移Issue/PR | 有限支持或无 |
| GraphQL高级查询 | 支持复杂关联查询、跨仓库聚合、深度分页 | 有限支持或无 |
| 自动化工作流 | 支持定时检查、自动分配、状态流转、通知告警 | 有限支持或无 |
| 团队仪表盘 | 支持多仓库汇总、成员贡献统计、燃尽图 | 有限支持或无 |
| Webhook管理 | 支持事件订阅、自动触发、回调配置 | 有限支持或无 |
| 安全审计 | 支持权限审查、敏感信息扫描、合规报告 | 有限支持或无 |
## 主要功能
- **自动化执行**: 全功能GitHub管理工具,含批量操作、GraphQL高级查询、自动化工作流、团队仪表盘与Webhook管理,适合团队企
- **文件处理**: 支持多种文件格式的读取、解析和写入操作
- **API集成**: 通过标准化接口调用外部服务并处理响应
- **命令执行**: 在安全沙箱中执行系统命令并收集结果
- **信息检索**: 快速搜索和过滤目标数据
## 常见咨询
### Q1: GitHub管理器(专业版)支持哪些输入格式？
A1: 全功能GitHub管理工具,含批量操作、GraphQL高级查询、自动化工作流、团队仪表盘与Webhook管理,适合团队企业级协作。。支持文本指令和结构化参数输入，具体格式参考使用流程章节。
### Q2: 需要配置API Key吗？
A2: 是的，部分功能需要配置对应平台的API Key。请在依赖说明章节查看具体要求，并通过环境变量安全配置。
### Q3: 命令行执行失败怎么办？
A3: 检查命令参数是否正确，确认运行环境支持exec能力。如遇权限问题，请参照错误处理章节排查。
## 异常应对措施
针对GitHub管理器(专业版)使用中可能遇到的常见问题,提供以下排查方案:
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
### GitHub管理器(专业版)通用排查步骤
1. **检查输入参数**: 确认所有必填参数已提供且格式正确
2. **查看日志输出**: 定位具体错误行和异常类型
3. **验证环境配置**: 确认依赖库版本和运行环境满足要求
4. **逐步调试**: 缩小问题范围,隔离故障模块
## 快速入门指南
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
## 协助指南
## 常见咨询
### Q1: GitHub管理器(专业版)支持哪些输入格式？

A1: 全功能GitHub管理工具,含批量操作、GraphQL高级查询、自动化工作流、团队仪表盘与Webhook管理,适合团队企业级协作。。支持文本指令和结构化参数输入，具体格式参考使用流程章节。

### Q2: 需要配置API Key吗？

A2: 是的，部分功能需要配置对应平台的API Key。请在依赖说明章节查看具体要求，并通过环境变量安全配置。

### Q3: 命令行执行失败怎么办？

A3: 检查命令参数是否正确，确认运行环境支持exec能力。如遇权限问题，请参照错误处理章节排查。