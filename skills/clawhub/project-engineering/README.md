# Project Engineering

> **让 Agent 先读懂项目，再动手改代码。**
>
> *Understand the repo. Change with evidence. Deliver with proof.*

[English](README.en.md) · [使用手册](docs/USAGE.md) · [更新记录](CHANGELOG.md)

多数编码 Agent 都会生成代码。真正困难的是判断：**应该修改什么、代码应该放在哪里、必须遵守哪些约束，以及需要多少验证证据。**

Project Engineering 是一个面向现有软件仓库的通用 Agent Skill。它先从项目规则、真实代码、构建配置、数据库迁移、测试和工作区状态中建立事实，再指导 Agent 完成架构定位、风险判断、最小实现、分层验证和可追溯交付。

它不是一段更长的“万能提示词”，而是一套面对真实工程时减少臆测、越界和无证据结论的工作方法。

## 为什么值得使用

- **先找证据，再做判断**：不根据目录名或类名猜测能力，追踪真实入口、调用链、状态和副作用。
- **尊重现有架构**：先识别模块职责和依赖方向，不机械套用 DDD、微服务或设计模式。
- **风险决定深度**：普通字段和设备控制不会走同一套检查强度；操作授权与目标风险分开判断。
- **最小但完整**：复用已有公开边界，不顺手重构，不虚构协议、接口或环境能力。
- **验证必须可追溯**：区分代码完成、自动测试、集成验证和真实环境验收，不用“应该没问题”替代证据。
- **保护真实工作区**：识别并保留用户已有修改，避免把本地配置、密钥和无关文件混入交付。
- **跨技术栈**：内置只读画像脚本可识别常见 Java/Maven/Gradle、Node.js、Python、Go、Rust 和 .NET 项目线索。

## 一条完整工作流

```text
仓库规则与真实代码
        ↓
工程画像与调用链还原
        ↓
模块归属、数据权威与风险分级
        ↓
最小且完整的实现
        ↓
按风险分层验证
        ↓
可审计的交付报告
```

## 30 秒开始使用

在 Codex 中显式调用：

```text
使用 $project-engineering。

任务：实现订单导出功能。
模式：直接开发。
要求：
1. 先读取项目规则并梳理现有调用链；
2. 保留工作区已有修改；
3. 遵循现有架构和编码风格；
4. 完成必要测试并报告结果；
5. 不提交、不推送。
```

只读理解陌生项目：

```text
使用 $project-engineering。

只读梳理当前仓库的技术栈、模块职责、运行进程、核心调用链、
数据库、外部依赖、权限边界、测试现状和主要工程风险。不要修改文件。
```

设计高影响变更：

```text
使用 $project-engineering。

为当前项目设计设备维护模式，仅输出方案，不编码。
重点分析状态权威源、权限、并发仲裁、协议兼容、数据库迁移、
失败关闭、回退和真实环境验收条件。
```

更多直接可复制的模板见 [完整使用手册](docs/USAGE.md)。

## 安装

### Codex / ChatGPT desktop / IDE

将仓库克隆到用户级 Skills 目录：

```bash
git clone https://github.com/liubai00/project-engineering.git ~/.agents/skills/project-engineering
```

也可以放入单个仓库的 `.agents/skills/project-engineering`，让它只对该仓库生效。若 Skill 没有立即出现，重启 Codex。

### OpenClaw / ClawHub

```bash
openclaw skills install @liubai00/project-engineering
```

安装后可让 OpenClaw 根据描述自动选择，也可以在请求中直接指定 `project-engineering`。

## 适用场景

适合：

- 接手陌生项目、遗留项目或他人开发的系统；
- 梳理技术栈、模块职责、部署形态和真实调用链；
- 设计新能力应该归属哪个包、模块、进程或服务；
- 完成跨入口、业务层、数据层、配置与测试的功能开发；
- 处理 API、消息、协议、数据库 Schema 和外部服务演进；
- 检查事务、并发、幂等、权限、兼容性和回退；
- 对开发结果进行审查、验收和工程交付；
- AI 执行动作、身份权限、资金和设备控制等高影响能力。

不适合：

- 一个错别字、单句文案或完全确定的机械替换；
- 与代码仓库无关的纯写作任务；
- 代替专业渗透测试、功能安全认证、法律或合规意见；
- 在缺少事实和授权时直接操作生产数据库、部署环境或真实设备。

## 风险不是看修改了多少行

| 等级 | 典型任务 | 主要增加的检查 |
|---|---|---|
| L1 | 文档、命名、局部纯逻辑 | 目标差异与最小验证 |
| L2 | CRUD、查询、单模块业务 | 输入、权限、事务、迁移 |
| L3 | 跨模块、数据库、异步、外部 API | 状态、幂等、兼容、超时、契约 |
| L4 | 身份、资金、隐私、AI 动作、设备控制 | 失败关闭、重新鉴权、仲裁、审计 |
| L5 | 可能伤人、破坏关键设施或受正式认证约束 | 领域安全负责人、危险分析与正式审批 |

只读审查一个高风险功能，仍然需要 L4/L5 的思考深度；但只读授权并不允许 Agent 修改代码或外部系统。

## 安全与授权边界

调用 Skill 只是在选择工程工作流，**不代表授权**：

- Git 提交、推送、创建 PR 或合并；
- 数据库迁移、部署、发版或生产写入；
- 密钥轮换、权限变更或外部服务配置；
- 真实设备控制和其他不可逆副作用。

Project Engineering 不上传仓库内容，不读取或输出密钥值。自带的 `project_inventory.py` 需要 Python 3.10+，是标准库只读扫描器：它只发现工程线索，不执行项目构建、包管理脚本或仓库代码。扫描报告会包含仓库根路径、分支、提交号和结构路径，公开分享前仍应检查。

## 能力包结构

```text
project-engineering/
├── SKILL.md
├── agents/openai.yaml
├── references/
│   ├── discovery.md
│   ├── architecture.md
│   ├── implementation.md
│   ├── risk-and-archetypes.md
│   └── delivery.md
└── scripts/
    ├── project_inventory.py
    ├── test_project_inventory.py
    └── test_skill_package.py
```

`SKILL.md` 只保留通用流程和参考路由；细节按任务需要逐步加载，避免每次占用大量上下文。

## 验证

```bash
python -m unittest discover -s scripts -p "test_*.py"
python scripts/project_inventory.py --repo . --format json
```

测试覆盖多生态识别、敏感信息不回显、异常清单安全处理和 Skill 包链接完整性。CI 同时在 Windows 与 Linux 上运行。

## 开源协议

[MIT-0](LICENSE)：可以自由使用、修改、商业使用和再分发，不要求署名。ClawHub 发布版本同样按 MIT-0 分发。

如果你认同“先理解，再修改；以证据决策，以验证交付”，欢迎提交 Issue 或 Pull Request。
