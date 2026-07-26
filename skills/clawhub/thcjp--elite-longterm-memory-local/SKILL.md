---
slug: "elite-longterm-memory-local"
name: "elite-longterm-memory-local"
version: 1.1.1
displayName: "本地向量记忆系统"
summary: "基于 LanceDB 与本地 Embedding 的纯本地向量记忆，零外部 API 依赖。"
license: "Proprietary"
description: |-
  基于 LanceDB 与纯 JavaScript Embedding 的本地向量记忆系统，无需外部 API 或原生模块.
  通过 Ollama 本地运行 nomic-embed-text 模型生成向量，所有数据完全留在本地，隐私至上.
  提供五层记忆架构：热内存（SESSION-STATE.md）、温存储（LanceDB 向量）、冷存储（Git-Notes）、
  精选归档（MEMORY.md + daily/）、本地 Embedding（Ollama）.
  支持 WAL 协议写前日志、自动召回相关上下文、智能捕获重要信息.特别适合对数据隐私有高要求的环境.
  对比云端 API 方案，本地 Embedding 免费、低延迟、可离线、数据不出域.
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
tags:
  - 智能助手
# 定价元数据
suggested_price: "19.9 CNY/per_use"
pricing_tier: "L2-标准级"
pricing_model: "per_use"

---
# 本地向量记忆系统（Elite Longterm Memory Local）

**本地优先，隐私至上。** 基于 LanceDB 与 Ollama 本地 Embedding 的向量记忆系统，零外部 API 依赖，所有数据完全留在本地。通过五层记忆架构与 WAL 协议，让 Agent 具备高效的语义搜索与上下文召回能力，同时保障数据隐私.
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | 本地向量记忆系统处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-----|:-----|
| 基础功能 | 支持 | 支持 |
| 大数据集流式处理 | 不支持 | 支持 |
| 多数据源关联查询 | 不支持 | 支持 |
| 可视化图表自动生成 | 不支持 | 支持 |
| 定时数据同步与增量更新 | 不支持 | 支持 |
| 数据质量检测与清洗规则 | 不支持 | 支持 |

## 核心能力

- **纯本地向量搜索（LanceDB）**：基于 LanceDB 的语义召回，无需外部 API。参数：node （请参考skill目录中的脚本文件） store "用户喜欢深色模式" --importance 0.9 --category preference，node （请参考skill目录中的脚本文件） search "用户界面偏好"。输出：按语义相似度排序的记忆列表。配置项：ollamaUrl（默认 http://localhost:11434）、embeddingModel（默认 nomic-embed-text）、dbPath（默认 ./memory/vectors）、autoRecall（自动召回）、autoCapture（自动捕获）.
- **本地 Embedding（Ollama）**：通过 Ollama 运行 nomic-embed-text 模型生成向量，完全本地。参数：ollama pull nomic-embed-text，ollamaUrl="http://localhost:11434"。输出：768 维向量嵌入。对比 OpenAI API：免费（vs 按 token 收费）、本地毫秒级延迟（vs 网络依赖）、数据不出域（vs 数据出域）、可离线（vs 不可用）、质量 nomic-embed-text（vs text-embedding-3）.
- **热内存（SESSION-STATE.md）**：活跃工作记忆，抗压缩与重启。参数：当前任务、关键上下文、待办动作、近期决策。输出：会话级状态文件。遵循 WAL 协议：用户输入触发写入，先写状态再回复。会话开始时读取获取热上下文，对话中用户给出具体细节则先写入再回复.
- **精选归档（MEMORY.md + daily/）**：人类可读的长期记忆。参数：MEMORY.md（摘要文件）+ memory/YYYY-MM-DD.md（每日日志）+ memory/topics/（主题文件）。输出：精炼后的长期记忆与每日活动记录。会话结束时将重要内容从 SESSION-STATE.md 迁移至 MEMORY.md，创建或更新每日日志.
- **记忆管理工具**：完整的 CLI 记忆管理命令。参数：node （请参考skill目录中的脚本文件） stats（统计）、node （请参考skill目录中的脚本文件） search "*" --limit 50（全量检索）、node （请参考skill目录中的脚本文件） dedup（去重）、node （请参考skill目录中的脚本文件） export --format json（导出）、node （请参考skill目录中的脚本文件） backup ./backups/memory-20260130.zip（备份）、node （请参考skill目录中的脚本文件） compact（压缩向量）、node （请参考skill目录中的脚本文件） cleanup --before 30d（清理旧记忆）。输出：结构化的记忆管理结果.
- **自动召回与捕获**：智能注入相关上下文与自动存储重要信息。参数：autoRecall=true（会话开始自动搜索相关记忆）、autoCapture=false（默认关闭自动捕获，避免噪音）、captureCategories=["preference","decision","fact"]、minImportance=0.7。输出：会话开始时自动召回与当前任务相关的历史记忆，对话中按类别与重要性自动存储.
### 纯本地向量搜索（LanceDB）

针对纯本地向量搜索（LanceDB）,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供纯本地向量搜索（LanceDB）相关的配置参数、输入数据和处理选项.
**输出**: 返回纯本地向量搜索（LanceDB）的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`纯本地向量搜索（LanceDB）`的配置文档进行参数调优
### 本地 Embedding（Ollama）

针对本地 Embedding（Ollama）,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供本地 Embedding（Ollama）相关的配置参数、输入数据和处理选项.
**输出**: 返回本地 Embedding（Ollama）的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`本地 Embedding（Ollama）`的配置文档进行参数调优
### 热内存（SESSION-STATE.md）

针对热内存（SESSION-STATE.md）,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供热内存（SESSION-STATE.md）相关的配置参数、输入数据和处理选项.
**输出**: 返回热内存（SESSION-STATE.md）的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`热内存（SESSION-STATE.md）`的配置文档进行参数调优
#
## 使用流程

第一步：安装依赖。执行 `ollama --version` 检查 Ollama 是否安装，执行 `ollama pull nomic-embed-text` 下载本地 Embedding 模型。进入 skills/elite-longterm-memory 目录执行 `npm install` 安装 Node.js 依赖.
第二步：初始化记忆系统。执行 `node （请参考skill目录中的脚本文件）` 创建记忆系统结构：SESSION-STATE.md（热内存）、MEMORY.md（长期记忆）、memory/（每日日志目录）、memory/vectors/（LanceDB 向量数据库）.
第三步：配置插件。在配置文件中添加 elite-longterm-memory 插件配置：enabled=true、ollamaUrl="http://localhost:11434"、embeddingModel="nomic-embed-text"、dbPath="./memory/vectors"、autoRecall=true、autoCapture=false。启用后系统自动提供 memory_recall、memory_store、memory_forget 三个工具.
第四步：配置 Agent 记忆协议。在 AGENTS.md 或 SOUL.md 中添加记忆协议：会话开始时读取 SESSION-STATE.md 获取热上下文，使用 memory_recall 搜索相关历史，检查 memory/YYYY-MM-DD.md 了解近期活动。对话中用户给出具体细节则先写入 SESSION-STATE.md 再回复；重要决策使用 memory_store 存储；偏好表达则 memory_store --importance 0.9 --category preference.
第五步：定期维护。执行 `node （请参考skill目录中的脚本文件） stats` 检查记忆统计，`node （请参考skill目录中的脚本文件） search "*" --limit 50` 全量检索检查质量，`node （请参考skill目录中的脚本文件） dedup` 去重，`node （请参考skill目录中的脚本文件） compact` 压缩向量数据库，`node （请参考skill目录中的脚本文件） cleanup --before 30d` 清理 30 天前旧记忆，`node （请参考skill目录中的脚本文件） backup ./backups/memory-$(date +%Y%m%d).zip` 定期备份.
#
## 错误处理

| 错误类型 | 原因 | 处理方式 |
|---:|---:|---:|
| Ollama 连接失败 | ollama serve 未运行或 OLLAMA_HOST 环境变量配置错误 | 检查 `ollama serve` 是否运行；检查 OLLAMA_HOST 环境变量；确认 ollamaUrl 配置为 http://localhost:11434 |
| 向量搜索无结果 | LanceDB 路径错误或记忆库为空 | 检查 dbPath 配置是否指向 ./memory/vectors；执行 `node （请参考skill目录中的脚本文件） stats` 确认已存储记忆；若为空先执行 memory_store 存入初始记忆 |
| nomic-embed-text 模型未下载 | 未执行 ollama pull nomic-embed-text | 执行 `ollama pull nomic-embed-text` 下载模型；确认 `ollama list` 中包含该模型 |
| 内存占用过高 | 向量数据库膨胀，长期使用未清理 | 运行 `node （请参考skill目录中的脚本文件） compact` 压缩向量；执行 `node （请参考skill目录中的脚本文件） cleanup --before 30d` 清理旧记忆；检查 stats 输出的记忆总量 |
| 自动召回注入无关上下文 | autoRecall 开启但 minImportance 阈值过低 | 提高 minImportance 阈值至 0.8；关闭 autoCapture 改手动存储；执行 dedup 去重清理低质量记忆 |
| 记忆重复存储 | autoCapture 与手动 memory_store 同时执行 | 禁用 autoCapture（设为 false）；仅保留手动 memory_store；执行 `node （请参考skill目录中的脚本文件） dedup` 清理已产生的重复记忆 |
| 备份文件损坏 | 备份过程中进程中断或磁盘空间不足 | 检查磁盘空间 `df -h`；重新执行 backup 命令；验证备份完整性 `node （请参考skill目录中的脚本文件） export --format json` 对比 |
| 初始化失败 | npm install 未完成或 Node.js 版本不兼容 | 确认 Node.js 版本≥18；重新执行 `npm install`；检查 package.json 依赖完整性 |

## 示例

### 示例 1：存储与搜索用户偏好

输入：
```bash
# 存储用户偏好
node （请参考skill目录中的脚本文件） store "用户喜欢深色模式" --importance 0.9 --category preference
# ...
# 存储项目决策
node （请参考skill目录中的脚本文件） store "项目前端框架选用 React" --importance 0.8 --category decision
# ...
# 存储技术事实
node （请参考skill目录中的脚本文件） store "API 网关使用 Kong" --importance 0.7 --category fact
```

执行与输出：
```
[记忆存储成功]
  ID: mem_001 | 内容: 用户喜欢深色模式 | 类别: preference | 重要性: 0.9
  ID: mem_002 | 内容: 项目前端框架选用 React | 类别: decision | 重要性: 0.8
  ID: mem_003 | 内容: API 网关使用 Kong | 类别: fact | 重要性: 0.7
# ...
# 语义搜索（无需精确关键词匹配）
node （请参考skill目录中的脚本文件） search "用户界面偏好"
→ 返回 mem_001（相似度: 0.92）"用户喜欢深色模式"
  （语义匹配："界面偏好" 与 "深色模式" 语义相关）
# ...
node （请参考skill目录中的脚本文件） search "前端技术选型"
→ 返回 mem_002（相似度: 0.89）"项目前端框架选用 React"
```

### 示例 2：完整会话记忆流程

输入：
```
会话开始：
  Agent 读取 SESSION-STATE.md → 获取上次任务上下文
  Agent 执行 memory_recall "当前项目状态" → 召回相关历史记忆
# ...
用户对话：
  "数据库从 MongoDB 迁移到 PostgreSQL 数据库，事务支持更好"
  → WAL 协议：先写入 SESSION-STATE.md
  → memory_store "数据库迁移到 PostgreSQL 数据库，因事务支持更好" --importance 0.9 --category decision
# ...
会话结束：
  Agent 更新 SESSION-STATE.md 最终状态
  Agent 迁移重要内容到 MEMORY.md：
    ## 决策
    - 数据库迁移到 PostgreSQL 数据库（事务支持更好）
  Agent 创建 memory/2026-07-21.md 每日日志
# ...
后续会话：
  memory_recall "数据库选型" → 召回 PostgreSQL 决策记录
  → Agent 自动遵循该决策，不再建议 MongoDB
```

## FAQ

**Q1：本地 Embedding 与 OpenAI API 有什么区别？**
本地 Embedding 使用 Ollama 运行 nomic-embed-text 模型，付费版独享、本地毫秒级延迟、数据不出域、可离线使用。OpenAI API 按 token 收费、依赖网络、数据出域、不可离线，但质量略高（text-embedding-3）。对于个人使用，nomic-embed-text 的质量足够，且付费版独享.
**Q2：系统需要联网吗？**
初始化时需联网下载 Ollama 与 nomic-embed-text 模型（`ollama pull nomic-embed-text`）及 npm 依赖。运行时完全离线，所有向量计算与记忆存储在本地，不做任何网络请求。适合对网络隔离有要求的环境.
**Q3：记忆数据存储在哪里？**
所有记忆存储在本地文件系统：SESSION-STATE.md（热内存）、MEMORY.md（长期摘要）、memory/YYYY-MM-DD.md（每日日志）、memory/vectors/（LanceDB 向量数据库）。数据不离开本地机器，可通过 `node （请参考skill目录中的脚本文件） backup` 备份到指定路径.
**Q4：autoRecall 和 autoCapture 该怎么配置？**
推荐 autoRecall=true（会话开始自动召回相关记忆，提升上下文连续性）、autoCapture=false（关闭自动捕获，避免噪音记忆，改用手动 memory_store 精确控制）。若对话频繁且需自动记录，可开启 autoCapture 并设置 minImportance=0.8 与 captureCategories=["preference","decision"] 限制捕获范围.
**Q5：记忆膨胀了怎么办？**
执行三步维护：第一步 `node （请参考skill目录中的脚本文件） stats` 查看记忆总量与分布；第二步 `node （请参考skill目录中的脚本文件） dedup` 去除重复记忆；第三步 `node （请参考skill目录中的脚本文件） compact` 压缩向量数据库。若仍过大，执行 `node （请参考skill目录中的脚本文件） cleanup --before 30d` 清理 30 天前旧记忆。定期执行可保持系统性能.
**Q6：支持多用户隔离吗？**
当前版本面向单用户设计。多用户场景可通过为每个用户配置独立的 dbPath（如 ./memory/user-a/vectors、./memory/user-b/vectors）实现隔离，但需手动管理多套配置。跨用户记忆共享不支持.
## 依赖说明

**LLM 依赖**：由 Agent 内置 LLM 提供自然语言理解与推理能力，必需。向量 Embedding 由本地 Ollama 提供，无需外部 LLM API.
**API Key 配置**：本 Skill 无需任何外部 API Key。Ollama 本地运行，nomic-embed-text 模型本地生成向量，所有数据处理在本地完成，不做任何网络请求.
**运行环境**：
- Agent 平台：支持 SKILL.md 的任意 AI Agent（Claude Code / Cursor / Codex / Gemini CLI 等）
- 操作系统：Windows / macOS / Linux
- Node.js（≥18）：运行 memory.js CLI 工具与 LanceDB 相关脚本，必需
- Ollama：本地运行 nomic-embed-text Embedding 模型，必需
- npm 依赖：vectordb（LanceDB Node.js 绑定）等，通过 `npm install` 安装
- 文件系统：本地存储，必需

**可用性分类**：MD+EXEC（Markdown 指令驱动，向量搜索与记忆管理需 exec 命令行执行能力）。memory.js CLI 工具需 Node.js 运行环境.
## 已知限制

1. **本地 Embedding 质量略低于云端 API**：nomic-embed-text 的语义理解质量略低于 OpenAI text-embedding-3，在复杂语义匹配场景下召回精度可能略有下降。对大多数个人使用场景质量足够.
2. **不支持多设备同步**：所有记忆存储在本地文件系统，无云备份与跨设备同步能力。多设备使用需手动通过 backup 与 export 命令迁移数据.
3. **需安装 Ollama 与 Node.js**：依赖 Ollama 运行时与 Node.js 环境，初始化需下载 nomic-embed-text 模型（约 270MB），对运行环境有一定要求.
4. **单用户设计**：当前版本面向单用户，多用户场景需手动配置独立 dbPath 实现隔离，无内置多用户管理与权限控制.
5. **向量数据库需定期维护**：长期使用后向量数据库可能膨胀，需定期执行 compact、dedup、cleanup 命令维护性能，否则搜索延迟可能上升.