---
slug: "longmemo-elite"
name: "longmemo-elite"
version: 2.0.1
displayName: "精英长记忆"
summary: "Agent精英级长记忆：WAL防丢失+三路混合检索+六层存储+成本预算控制。"
license: "Proprietary"
description: |-
  面向AI Agent的精英级长期记忆系统，解决跨会话遗忘、检索不准、成本失控三大核心痛点.
  WAL写前日志协议采用"先写状态，再回复用户"模式，在压缩/崩溃/重启场景下保证上下文不丢失.
  向量+关键词+图谱三路混合检索，通过RRF融合排序解决单一向量检索"相似但不相关"的召回质量问题.
  六层存储架构（L1热内存→L2温向量→L3冷图谱→L4精选归档→L5云备份→L6自动抽取）按需分层加载，降低token消耗.
  成本预算控制通过embedding缓存、分层存储、小模型抽取、图谱增量更新四项策略，配置日/月预算上限与自动降级.
  记忆卫生自动化执行去重、衰减、晋升、降级、归档、删除六项维护，避免记忆膨胀拖慢召回.
  适用于跨会话项目开发、多代理协作、长期偏好维护等生产级Agent记忆管理场景.
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
tags:
  - 通用办公
# 定价元数据
suggested_price: "29.9 CNY/per_use"
pricing_tier: "L3-专业级"
pricing_model: "per_use"

---
# 精英长记忆

解决AI Agent三大记忆顽疾：跨会话遗忘、检索不准、成本失控。本系统将六种成熟记忆策略整合为一套防弹架构，配合WAL写前日志协议，确保永不丢失上下文、永不遗忘决策、永不重复犯错.
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | 精英长记忆处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-----|:-----|
| 基础功能 | 支持 | 支持 |
| 精英长记忆三路混合检索 | 不支持 | 支持 |
| 复杂工作流可视化编排 | 不支持 | 支持 |
| 条件分支与异常重试 | 不支持 | 支持 |
| 定时触发与事件驱动 | 不支持 | 支持 |
| 执行日志与审计追踪 | 不支持 | 支持 |

## 核心能力

- **WAL写前日志防丢失**：采用"先写状态，再回复用户"协议，在压缩、崩溃、重启场景下保证上下文不丢失。触发时机：用户表达偏好时先写入SESSION-STATE.md与对应存储层再回复；用户做出决策时先写入SESSION-STATE.md与Git-Notes再回复；用户给出期限时先写入SESSION-STATE.md再回复；用户纠正错误时先写入SESSION-STATE.md与lessons.md再回复。写入本地文件是毫秒级操作，对用户感知无影响.
- **向量+关键词+图谱三路混合检索**：向量检索负责语义相似召回（基于LanceDB），关键词倒排负责精确实体匹配（本地零API成本），图谱遍历负责因果关联推理（基于Git-Notes）。三路结果通过RRF（Reciprocal Rank Fusion）融合排序，配置 `minScore=0.35`、`maxResults=10`。解决单一向量检索"相似但不相关"的召回质量问题，综合成本反而低于纯向量方案.
- **六层存储架构分层加载**：L1热内存（SESSION-STATE.md，抗压缩，会话开始立即加载）→ L2温向量（LanceDB本地向量库，按需检索）→ L3冷图谱（Git-Notes结构化决策，Git永久持久化）→ L4精选归档（MEMORY.md+daily/目录，人类可读，周期性回顾）→ L5云备份（SuperMemory API跨设备同步，可选）→ L6自动抽取（Mem0对话事实提取，推荐）。按需分层加载降低token消耗.
- **成本预算控制**：通过四项策略控制成本——embedding缓存（相同文本不重复计算，节省60-80%）、分层存储（热内存只放当前任务，节省40-60%）、小模型抽取（用小模型提取事实而非大模型，节省70-90%）、图谱增量更新（只更新变更部分，节省50-70%）。配置 `dailyLimitUsd=2.0`、`monthlyLimitUsd=50.0`，达到80%告警，100%自动降级为只读模式.
- **记忆卫生自动化**：自动执行六项维护——去重（memory_dedup合并相似条目）、衰减（低重要性记忆权重随时间降低）、晋升（7天内出现3次的记忆提升到MEMORY.md）、降级（30天未访问移出热内存）、归档（90天未访问移入archive/）、删除（180天未访问且importance<0.3询问后删除）。避免记忆膨胀拖慢召回速度.
### 六层存储架构速查
| 层级 | 存储 | 用途 | 持久化 | 加载时机 |
|---:|---:|---:|---:|---:|
| L1热内存 | SESSION-STATE.md | 当前任务、关键上下文、待办 | 抗压缩/重启 | 会话开始立即加载 |
| L2温向量 | LanceDB | 语义相似召回 | 本地向量库 | 按需检索 |
| L3冷图谱 | Git-Notes | 结构化决策、分支关联 | Git永久 | 决策/查询时 |
| L4精选归档 | MEMORY.md + daily/ | 蒸馏后的长期智慧 | 文件 | 周期性回顾 |
| L5云备份 | SuperMemory API | 跨设备同步 | 云端 | 可选 |
| L6自动抽取 | Mem0 | 对话自动提取事实 | 外部服务 | 推荐 |

**处理**: 解析六层存储架构速查的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回六层存储架构速查的处理结果,包含执行状态码、结果数据和执行日志.
### L1热内存

针对L1热内存,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供L1热内存相关的配置参数、输入数据和处理选项.
**输出**: 返回L1热内存的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`L1热内存`的配置文档进行参数调优
### L2温向量

针对L2温向量,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供L2温向量相关的配置参数、输入数据和处理选项.
**输出**: 返回L2温向量的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`L2温向量`的配置文档进行参数调优
#
## 使用流程

### 第一步：创建热内存文件

在工作区根目录创建 `SESSION-STATE.md`，包含当前任务、关键上下文（用户偏好/已做决策/当前阻塞）、待办动作、近期决策四个区块，作为抗压缩的热内存.
### 第二步：配置混合检索与成本预算

在 `memory-config.json` 中启用三路混合检索与成本预算控制：

```json
{
  "memorySearch": {
    "enabled": true,
    "provider": "openai",
    "minScore": 0.35,
    "maxResults": 10,
    "hybrid": { "vector": true, "keyword": true, "graph": true, "fusion": "rrf" }
  },
  "costBudget": {
    "dailyLimitUsd": 2.0,
    "monthlyLimitUsd": 50.0,
    "alertThreshold": 0.8,
    "strategies": { "embeddingCache": true, "tieredStorage": true, "smallModelExtraction": true }
  }
}
```

### 第三步：初始化冷存储与验证

执行 `git init` 初始化Git仓库（用于Git-Notes知识图谱），运行 `python3 memory.py -p . sync --start` 启动同步，创建 `memory/` 目录结构。执行 `memory_recall query="测试查询" limit=3` 验证检索功能正常，确认向量库非空、embedding provider可用.
### 第四步：执行WAL协议（对话进行中）

遵循"先写后回复"原则：用户表达偏好→写入SESSION-STATE.md + memory_store；做出决策→写入SESSION-STATE.md + Git-Notes；给出期限→写入SESSION-STATE.md；纠正错误→写入SESSION-STATE.md + lessons.md；出现代码错误→记录到lessons.md + memory_store.
### 第五步：会话管理与记忆卫生

会话开始时：读取SESSION-STATE.md（热内存）→ 执行memory_recall检索相关历史 → 检查memory/YYYY-MM-DD.md近期活动 → 扫描lessons.md相关教训.
会话结束时：更新SESSION-STATE.md最终状态 → 重要内容迁移到MEMORY.md → 创建/更新memory/YYYY-MM-DD.md日志.
每周执行：memory_dedup去重 → memory_forget清理低重要性向量（importance<0.3且超过30天）→ memory_compact压缩旧日志 → memory_export导出备份.
#
## 错误处理

| 错误类型 | 原因 | 处理方式 |
|:---:|:---:|:---:|
| 全部遗忘（新会话无历史） | memory_search未启用或embedding provider未配置OPENAI_API_KEY | 启用memory_search，配置OPENAI_API_KEY；无API Key时降级为本地embedding |
| 记忆文件未加载 | Agent跳过读取记忆步骤，会话开始未读取SESSION-STATE.md | 在AGENTS.md中写入强制规则：会话开始必须读取SESSION-STATE.md |
| 子代理上下文孤立 | 派生子代理时未注入上下文继承块，子代理无法获取主代理决策 | 使用上下文传递协议，在子代理任务提示词中注入项目/任务/决策/偏好/约束五项上下文 |
| 重复犯错 | 教训未记录到lessons.md，新会话无法召回之前踩过的坑 | 强制WAL协议：出现错误时先写lessons.md再修复；会话开始扫描lessons.md |
| 召回不准（相似但不相关） | 仅启用单路向量检索，语义相似但实际不相关的内容排名靠前 | 启用三路混合检索（vector+keyword+graph）+ RRF融合；关键词与图谱本地执行零API成本 |
| 召回太慢 | 向量库膨胀未清理，记忆条目过多导致检索延迟上升 | 执行memory_compact压缩 + memory_forget清理低重要性记忆；每周执行一次轻清理 |
| 账单暴涨 | 无预算控制或embedding未缓存，每次检索都重新计算向量 | 配置日/月预算上限（dailyLimitUsd/monthlyLimitUsd），启用embedding缓存与小模型抽取 |
| Git-Notes不持久 | 未执行git notes push，图谱决策仅存于本地 | 执行 `git notes push` 同步到远程仓库，确保结构化决策跨设备可用 |
| 召回为空 | 向量库为空或minScore设置过高（如0.8），过滤掉了所有结果 | 检查向量库非空，降低minScore到0.35；确认memory_store已写入数据 |
| 事实未自动捕获 | 未启用Mem0自动抽取，对话中的事实仅靠手动memory_store记录 | 启用Mem0自动抽取，或在WAL协议中增加手动memory_store记录步骤 |

## 示例

### 示例1：跨会话技术决策延续

**输入：**
- 会话A（周一）：用户说"数据库用MySQL，开发环境用SQLite"
- 会话B（周三，新会话）：用户说"部署脚本怎么写？"

**执行：**
1. 会话A执行WAL：写入SESSION-STATE.md"决策：MySQL生产/SQLite开发"；写入Git-Notes（带分支标记）；memory_store存储 `{"content":"用户偏好MySQL生产/SQLite开发","importance":0.9,"category":"decision"}`
2. 会话B会话开始：执行 `memory_recall query="部署 数据库"` → 召回MySQL决策 → 回复时主动考虑MySQL部署配置

**输出：**
```bash
# 会话A WAL写入
SESSION-STATE.md: "决策：MySQL生产环境/SQLite开发环境"
Git-Notes: "决策#001: 数据库选型 MySQL生产/SQLite开发 [branch:main]"
memory_store: {"id":"mem_001","content":"用户偏好MySQL生产/SQLite开发","importance":0.9,"category":"decision"}
# ...
# 会话B召回
memory_recall query="部署 数据库" → 召回mem_001（score=0.87）
→ 生成MySQL部署脚本（包含连接池配置、字符集utf8mb4、时区设置）
```

### 示例2：避免重复犯错

**输入：**
- 会话A：Agent生成的Dockerfile缺少.dockerignore，导致镜像2GB，用户纠正
- 会话B：用户说"帮我写个Dockerfile"

**执行：**
1. 会话A执行WAL：写入lessons.md"生成Dockerfile必须同时生成.dockerignore"
2. 会话B会话开始：检索lessons.md → 召回.dockerignore教训 → 主动同时生成两个文件

**输出：**
```bash
# 会话A WAL写入
lessons.md: "教训#003: 生成Dockerfile必须同时生成.dockerignore，否则镜像体积过大"
memory_store: {"id":"mem_007","content":"Dockerfile必须配.dockerignore","importance":0.95,"category":"lesson"}
# ...
# 会话B召回
memory_recall query="Dockerfile" → 召回mem_007（score=0.92）
→ 同时输出Dockerfile和.dockerignore两个文件
```

### 示例3：多代理协作上下文传递

**输入：** 主代理需派生代码审查子代理审查支付模块

**执行：** 主代理在子代理任务提示词中注入上下文继承块

**输出：**
```
上下文继承块（注入子代理提示词）：
- 项目: 电商平台
- 当前任务: 审查支付模块代码
- 关键决策: 支付用Stripe / 货币用USD / 支持订阅与一次性付款
- 已知约束: 必须PCI合规 / 信用卡数据不落本地
- 历史教训: 上次支付模块因未处理Webhook重试导致重复扣款
# ...
子代理基于继承上下文进行审查，无需重新询问，直接关注PCI合规与Webhook重试逻辑.
```

## FAQ

**Q1：WAL协议会不会拖慢回复速度？**
A：写入本地文件是毫秒级操作，对用户感知无影响。相比崩溃后丢失上下文的代价，这点延迟完全值得。WAL协议的核心是"先写后回复"，确保任何时刻崩溃都不丢失关键信息.
**Q2：混合检索三路都开会不会很贵？**
A：关键词倒排和图谱遍历都是本地操作，零API成本。只有向量检索需要embedding（已缓存，相同文本不重复计算）。综合成本反而低于纯向量方案，因为召回更准，减少了重试与重复检索.
**Q3：Mem0自动抽取和手动memory_store冲突吗？**
A：不冲突。Mem0负责对话流自动提取事实（低价值高频），手动memory_store负责高价值显式记录（高价值低频）。两者互补，Mem0有去重逻辑避免重复存储相同事实.
**Q4：本地和云端如何选择？**
A：个人或小团队用本地（LanceDB + Git-Notes）足够；跨设备协作加SuperMemory云备份；生产级建议本地为主+云端备份。L1-L4纯本地即可工作，L5云备份与L6自动抽取为可选增强.
**Q5：记忆库多久清理一次？**
A：建议每周一次轻清理（memory_dedup去重 + 低重要性降级），每月一次深清理（归档 + 压缩 + 导出备份）。记忆卫生自动化可配置为定时执行，无需手动触发.
**Q6：成本预算达到100%后怎么办？**
A：达到100%预算后自动降级为只读模式，此时新记忆无法写入，但检索仍可用。需等待下一预算周期重置或提升预算上限。建议配置alertThreshold=0.8在80%时收到告警，提前调整策略.
## 依赖说明

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:------|------:|:------|:------|
| Agent平台 | 运行环境 | 必需 | 安装支持SKILL.md的AI Agent |
| Python 3.8+ | 运行时 | 推荐 | python.org安装（Git-Notes脚本） |
| Node.js 16+ | 运行时 | 推荐 | nodejs.org安装（LanceDB向量库） |
| LanceDB | 向量数据库 | 推荐 | `pip install lancedb` |
| OpenAI Embedding API | 向量化 | 推荐 | 配置OPENAI_API_KEY（无则降级为本地embedding） |
| Mem0 | 自动事实抽取 | 可选 | `npm install mem0ai` |
| SuperMemory | 跨设备云同步 | 可选 | 官网注册获取API Key |
| LLM API | API | 必需 | 由Agent平台内置LLM提供 |

**API Key配置：**
- OPENAI_API_KEY：向量embedding生成（推荐，无则降级为本地embedding）
- MEM0_API_KEY：对话自动事实抽取（可选）
- SUPERMEMORY_API_KEY：跨设备云同步（可选）

**可用性分类：** MD+EXEC（核心记忆协议纯Markdown即可工作；向量检索、自动抽取等高级功能需对应依赖）

**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统.
## 已知限制

1. **六层架构需逐步启用**：L1-L4纯本地Markdown即可工作，L2向量检索需安装LanceDB，L5云备份需SuperMemory API，L6自动抽取需Mem0，并非开箱即用全部功能.
2. **WAL协议依赖Agent配合**：协议本身是行为规范，需要Agent平台支持在AGENTS.md中写入强制规则才能保证执行，若Agent忽略指令则WAL失效.
3. **embedding缓存基于文本哈希**：相同文本不重复计算，但文本微小改动（如加空格）会触发重新计算，对高频更新场景缓存命中率会下降.
4. **图谱遍历深度受限**：为控制延迟，图谱遍历默认限制在2-3跳，超深关联（5跳以上）可能遗漏.
5. **成本预算只读降级后无法写入**：达到100%预算后自动降级为只读模式，此时新记忆无法写入，需等待下一预算周期或提升上限.
## 输出格式

```json
{
  "success": true,
  "data": {
    "result": "精英长记忆处理结果",
    "execution_time": "0.5s",
    "metadata": {
      "version": "1.0",
      "processor": "longmemo-elite"
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
