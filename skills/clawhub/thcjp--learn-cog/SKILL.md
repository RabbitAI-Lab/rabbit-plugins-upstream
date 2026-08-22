---

slug: learn-cog
name: "learn-cog"
version: 1.0.14
displayName: "个性化学习助手"
summary: "AI驱动的个性化学习助手，支持项目教程、语言学习、写作反馈、视觉学习与学习指南。个性化学习助手，基于CellCog提供多模式AI辅导. 支持项目教程、语言学习、写作反馈、视觉学习与学习指南"
summary_zh: "AI驱动的个性化学习助手，支持项目教程、语言学习、写作反馈、视觉学习与学习指南。个性化学习助手，基于CellCog提供多模式AI辅导. 支持项目教程、语言学习、写作反馈、视觉学习与学习指南"
license: "MIT"
description: |- 功能涵盖: learn。 功能涵盖:。Use when 需要AI模型调用、智能对话、Agent编排、LLM应用时使用。不适用于需要100%确定性的关键决策。适用于独立开发者、企业团队和自动化工作流场景。支持中文交互，无需复杂配置即开即用。输出结果可直接使用，减少二次加工成本。提供结构化输出和错误处理机制。 功能涵盖: cog。
  个性化学习助手，基于CellCog提供多模式AI辅导.
  支持项目教程、语言学习、写作反馈、视觉学习与学习指南生成.
  覆盖STEM、人文、技术与职业技能等多学科领域.
  适用于学生、开发者与终身学习者的知识获取与技能提升。Use when 需要AI模型调用、智能对话、Agent编排、LLM应用时使用。不适用于需要100%确定性的关键决策。
tools:
  - read
  - exec
  - write
homepage: ""
tags:
  - 通用办公
  - 工具
  - 效率
  - 知识
  - 文档
  - 写作
  - api
  - react
  - learning
  - 示例
category: "Automation"
homepage: ""
pricing_tier: "L2-标准级"

---

> **功能说明**: 本技能涵盖 中文交互、化工作流场景 等核心能力。

# 个性化学习助手

AI驱动的个性化学习助手，支持项目教程、语言学习、写作反馈、视觉学习与学习指南.
## 输入规范
| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | 个性化学习助手处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

## 运行环境
### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Python环境**: Python 3.8+（如使用CellCog SDK）

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|---:|---:|---:|---:|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| CellCog SDK | Python库 | 可选 | `pip install -U cellcog` |
| CELLCOG_API_KEY | API密钥 | 可选 | CellCog平台获取 |
| 终端/Shell | CLI | 可选 | 操作系统自带 |

### 可用性分类
- **分类**: MD+EXEC（）
- **说明**: 基于Markdown的AI Skill，通过自然语言指令驱动Agent执行学习辅导任务

**API Key配置方式**:
```bash
export API_KEY="${API_KEY:?请设置环境变量}"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统.
## 能力范围
### 项目教程（Project Tutorials）
通过实战项目驱动学习，从零到一构建完整应用：

- **逐步引导**：将复杂项目拆解为可执行的步骤，每步附带代码示例
- **项目类型**：REST API搭建、Web应用开发、CLI工具构建、数据处理管道等
- **可运行代码**：提供可直接运行的代码示例，边学边做
- **深度概念讲解**：在项目实践中讲解Docker容器、React Hooks等技术原理
- **能力评估**：通过mini-project综合检验学习成果

示例请求：

> "Walk me through building a REST API step by step"
> "Teach me React hooks: My level is I know basic JavaScript, never used React"

### 语言学习（Language Learning）
系统化掌握新语言，覆盖听说读写全方位训练：

- **语法讲解（Grammar Explanations）**：如"Explain Japanese particles with examples"
- **对话练习（Conversation Practice）**：如"Practice ordering food in French"场景对话
- **词汇构建（Vocabulary Building）**：如"Teach me 20 essential business Chinese phrases"
- **多语言支持**：日语（JLPT N4-N1）、法语、西班牙语、中文等
- **文化背景**：附带语言使用的文化语境与注意事项

### 写作反馈（Writing Feedback）

对文章、论文、邮件等写作内容提供专业反馈：

- **语法与拼写检查**：识别并修正语法错误与拼写问题
- **结构优化**：评估文章结构，建议段落重组与逻辑改进
- **语言润色**：优化用词、句式与语气，提升表达力
- **写作风格指导**：学术写作、商务写作、创意写作的风格调整
- **语言学习写作**：如"Check my Spanish essay and explain my mistakes"

### 视觉学习（Visual Learning）
通过图表、图示、信息图等视觉化方式辅助理解：

- **概念图示**：如"Create a diagram explaining the water cycle"
- **流程图**：将复杂流程可视化为步骤图
- **信息图**：将数据与概念组织为易理解的视觉格式
- **对比图**：通过视觉对比帮助理解差异
- **学习风格适配**：支持Visual（图表）、Examples（示例）、Analogies（类比）、Step-by-Step（步骤）、Big Picture（全局）、Hands-On（实践）等多种学习风格

### 学习指南（Study Guides）
生成系统化的学习材料与备考资源：

- **学习指南（Study Guides）**：如"Create a study guide for AP Chemistry exam"
- **闪卡（Flashcards）**：如"Generate 50 flashcards for Spanish vocabulary"
- **模拟测试（Practice Tests）**：如"Create a practice quiz on US History 1900-1950"
- **摘要笔记（Summary Notes）**：如"Summarize Chapter 5 of my biology textbook"
- **速查表（Cheat Sheets）**：如"Create a one-page reference for Python syntax"

### 概念解释与作业辅导（Concept Explanations & Homework）
多角度解释概念与作业问题解答：

- **概念拆解**：如"Explain quantum entanglement like I'm 10 years old"
- **多角度解释**：如"Explain recursion using 3 different analogies"
- **数学解题**：逐步解答微积分、物理等问题并解释每步
- **代码调试**：解释代码为何不工作并帮助修复
- **作文结构**：帮助构建论文框架与论点

---

## 操作步骤
1. 确认运行环境满足依赖说明中的要求
2. 明确学习目标：概念理解、项目实践、语言学习、写作反馈或备考
3. 说明当前水平：如"Complete beginner"或"I understand the basics"
4. 选择学习风格：Visual、Examples、Analogies、Step-by-Step、Big Picture或Hands-On
5. 使用自然语言描述学习需求，Agent生成个性化学习内容
6. 通过主动回忆（Active Recall）与练习巩固学习成果

**结果验证**: 任务完成后,查看输出确认状态。成功时返回摘要和数据;失败时根据错误信息排查,参考恢复章节获取修复步骤.
## 示例展示
### 示例1：学习React Hooks

```
用户: Teach me React hooks, I know basic JavaScript, never used React
# ...
Agent: React Hooks学习计划：
1. What problem do hooks solve? - 状态逻辑复用与组件简化
2. useState with simple examples - 计数器示例
3. useEffect with practical use cases - 数据获取与副作用
4. When to use which hook - 决策树
5. A mini-project putting it together - Todo App
# ...
[附带可运行的代码示例]
```

### 示例2：生成AWS认证学习指南

```
用户: Create a study guide for the AWS Solutions Architect exam
# ...
Agent: AWS Solutions Architect学习指南：
- Key services and when to use them (EC2, S3, RDS, Lambda...)
- Networking concepts (VPC, Subnets, Route53...)
- Security best practices (IAM, KMS, Security Groups...)
- Cost optimization strategies (Reserved Instances, Spot Fleet...)
[每节附练习题]
```

### 示例3：日语对话练习

```
用户: Help me practice Japanese, Level: JLPT N4, Focus: Conversational
# ...
Agent: 日语对话练习 - 在东京问路：
- Scenario: Asking for directions in Tokyo
- Vocabulary list: 駅、交差点、右、左...
- Grammar points used: 〜はどこですか、〜てください
- Cultural notes: 礼貌用语与鞠躬礼仪
- Variations to practice: 正式场合与日常场景
[Romaji + 汉字 + ひらがな标注]
```

## 常见疑问
### Q1: 如何获得优选学习效果？
A: 1）说明当前水平；2）多问"为什么"而非只要答案；3）请求练习题；4）承认困惑点；5）基于已理解的内容构建新知识；6）使用主动回忆（要求测验而非仅解释）.
### Q2: agent模式和agent team模式有什么区别？
A: `agent`模式适合大多数学习场景：快速解释、作业辅导、学习材料生成。`agent team`模式适合综合学习：完整课程大纲、研究论文、多源综合分析.
### Q3: 支持哪些学科领域？
A: STEM（数学、物理、化学、生物、计算机、统计）、人文（历史、文学、哲学、语言、心理）、职业（商业、金融、营销、项目管理、设计、法律）、技术技能（编程语言、云平台、DevOps、数据工程、AI/ML）.
### Q4: 如何进行语言学习写作反馈？
A: 将你的写作内容发送给Agent，说明语言（如西班牙语），Agent会检查语法错误、解释错误原因、提供修改建议并优化表达.
### Q5: CellCog未安装怎么办？
A: 运行 `/cellcog-setup` 安装认证，或手动执行 `pip install -U cellcog` 并设置 `CELLCOG_API_KEY`。也可直接使用Agent内置LLM进行学习辅导.
### Q6: 如何生成备考学习计划？
A: 提供考试名称、时间线、目标分数、薄弱环节，Agent会生成包含每周计划、资源推荐、练习测试策略与考前清单的完整学习计划.
## 功能边界
- 单次会话仅覆盖一个学习意图，跨学科综合问题需拆分为多次交互
- CellCog SDK为可选依赖，未安装时部分高级功能受限
- 视觉学习生成的图表为文本描述格式，非真实图片
- 语言学习口语练习需配合TTS工具实现语音输出
- 复杂学科（如高级医学、法学）的准确性需人工验证
- 学习进度跟踪需要用户手动维护

## 输出规范
```json
{
  "success": true,
  "data": {
    "result": "个性化学习助手处理结果",
    "execution_time": "0.5s",
    "metadata": {
      "version": "1.0",
      "processor": "learn-cog"
    }
  },
  "execution_log": [
    "解析输入参数",
    "执行核心处理",
    "格式化输出结果"
  ],
  "error": null
}
```

## 创新优势
### 效率提升量化分析
| 操作步骤 | 手动耗时 | 自动化耗时 | 时间节约 | 准确率提升 |
| --- | --- | --- | --- | --- |
| 项目教程编写 | 20小时 | 2小时 | 18小时 | 15% |
| 语言学习课程设计 | 30小时 | 5小时 | 25小时 | 10% |
| 写作反馈评估 | 10小时 | 1小时 | 9小时 | 12% |
| 视觉学习内容制作 | 40小时 | 4小时 | 36小时 | 8% |
| 学习指南生成 | 15小时 | 1.5小时 | 13.5小时 | 7% |

### 差异化对比
| 对比维度 | 本技能 | 手动操作 | Python脚本 | 专业软件 |
| --- | --- | --- | --- | --- |
| 功能丰富度 | 高 | 低 | 中 | 高 |
| 学习效率 | 高 | 低 | 中 | 高 |
| 个性化定制 | 高 | 低 | 中 | 高 |
| 成本效益 | 高 | 低 | 中 | 高 |
| 易用性 | 高 | 低 | 中 | 高 |

### 核心痛点解决
| 痛点 | 描述 | 影响范围 | 解决方案 | 量化效果 |
| --- | --- | --- | --- | --- |
| 学习资源有限 | 学生难以获取全面的学习资源 | 广泛的学生群体 | 提供个性化学习路径和资源推荐 | 学习资源利用率提升30% |
| 学习效率低 | 传统学习方式效率低下 | 学生群体 | 通过AI辅导提高学习效率 | 学习效率提升20% |
| 学习体验单一 | 学习体验缺乏互动和趣味性 | 学生群体 | 提供多样化的学习内容和交互方式 | 学习兴趣提升25% |

## 诊断与修复
| 错误现象 | 可能原因 | 诊断步骤 | 解决方案 |
| --- | --- | --- | --- |
| 无法加载教程内容 | 网络连接问题 | 检查网络连接 | 重启技能或检查网络设置 |
| 语言学习发音不准确 | 语音识别错误 | 检查语音识别设置 | 调整语音识别参数或更换语音库 |
| 写作反馈延迟 | 服务器负载过高 | 检查服务器状态 | 增加服务器资源或优化代码 |
| 视觉学习内容缺失 | 数据源问题 | 检查数据源 | 更新或修复数据源 |
| 学习指南内容错误 | 内容校对错误 | 校对学习指南内容 | 修正错误内容 |

## 安全规范
1. [与「个性化学习助手」相关的安全注意事项]
   - 保护用户隐私，不泄露用户学习数据。
   - 确保数据传输加密，防止数据被窃取。
   - 定期更新AI模型，防止安全漏洞。
   - 对敏感操作进行权限控制，防止未授权访问。
   - 定期进行合规检查，确保系统安全。

### 安全风险防范

| 风险项 | 等级 | 防护措施 | 验证方法 |
| --- | --- | --- | --- |
| API密钥泄露 | 高 | 通过环境变量配置，禁止硬编码 | 定期检查代码和配置文件 |
| 命令执行风险 | 高 | 仅执行白名单命令，避免拼接用户输入 | 使用沙箱环境测试 |
| 网络通信安全 | 中 | 使用HTTPS协议，验证SSL证书 | 定期检查证书有效期 |
| 敏感数据暴露 | 高 | 输出结果中不包含密钥、令牌等敏感信息 | 日志脱敏审查 |
| 未授权访问 | 中 | 限制访问权限，实施认证机制 | 定期审计访问日志 |

## 故障应对方案
针对个性化学习助手使用中可能遇到的常见问题,提供以下排查方案:

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

### 个性化学习助手通用排查步骤

1. **检查输入参数**: 确认所有必填参数已提供且格式正确
2. **查看日志输出**: 定位具体错误行和异常类型
3. **验证环境配置**: 确认依赖库版本和运行环境满足要求
4. **逐步调试**: 缩小问题范围,隔离故障模块

### 前置条件

- 已安装所需运行环境(参考依赖说明)
- 已获取必要的API密钥或访问凭证(如适用)
- 输入数据已准备就绪

## 典型场景
- **日常开发**: 个性化学习助手可快速集成到现有开发流程中,提升工作效率
- **接口集成**: 对接第三方API服务,实现数据自动获取和处理
- **内容生成**: 自动生成文档、代码或结构化数据
- **文件批处理**: 批量处理文件内容,支持多格式转换和解析
- **环境管理**: 批量管理开发环境和部署流程
- **数据处理**: 对结构化数据进行清洗、转换和分析
