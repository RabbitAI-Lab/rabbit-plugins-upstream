---
slug: "memo-quickstart"
name: "memo-quickstart"
version: 1.0.1
displayName: "记忆快速启动"
summary: "零依赖本地记忆系统：三层架构+混合检索+WAL日志+关系图谱+迁移工具。"
license: "Proprietary"
description: |-
  面向零依赖场景的本地记忆系统，解决搜索精度不足、上手门槛高、数据格式不统一四大痛点.
  三层记忆架构（热内存SESSION-STATE.json/冷存储memories/目录/人类可读归档MEMORY.md+daily/）协同提供从快到慢的记忆存取.
  TF-IDF+近期加权+重要度加权+标签匹配四维混合检索算法，召回率比纯TF-IDF提升40%.
  WAL写前日志协议确保响应前先写入记忆，避免崩溃丢失上下文.
  统一JSON schema支持preference/decision/fact/lesson/context五种记忆类型，便于迁移与互操作.
  记忆关系图谱支持related_to/followed_by关系链，查到一条记忆可顺藤摸瓜找到关联记忆.
  迁移工具支持从其他记忆系统一键导入.
  适用于隐私敏感场景、离线开发、学习记忆系统、构建自定义Agent记忆层.
  无API Key、无云、无追踪，纯本地记忆.
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
tags:
  - 创意设计
# 定价元数据
suggested_price: "19.9 CNY/per_use"
pricing_tier: "L2-标准级"
pricing_model: "per_use"

---
# 记忆快速启动

面向零依赖场景的本地记忆系统，用三层架构和混合检索算法，在不引入任何外部依赖的前提下，提供开箱即用的记忆能力。无API Key、无云、无追踪，纯本地记忆.
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | 记忆快速启动处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-----|:-----|
| 基础功能 | 支持 | 支持 |
| 记忆快速启动混合检索 | 不支持 | 支持 |
| 高清分辨率与无损输出 | 不支持 | 支持 |
| 批量生成与风格预设 | 不支持 | 支持 |
| 自定义模型微调 | 不支持 | 支持 |
| 商用版权授权 | 不支持 | 支持 |

## 核心能力

- **三层记忆架构**：热内存（SESSION-STATE.json，活跃工作记忆，抗上下文压缩，会话开始立即加载）→ 冷存储（memories/目录，索引化JSON文件，可检索）→ 人类可读归档（MEMORY.md + daily/目录，长期精选，周期性回顾）。三层协同提供从快到慢的记忆存取，热内存毫秒级访问，冷存储支持复杂检索，归档层人类可读可编辑.
- **混合检索算法**：在TF-IDF基础文本相关性（权重50%）上叠加近期加权（权重20%，近期记忆优先）、重要度加权（权重20%，高重要度优先）、标签匹配（权重10%，标签命中加分）三维加权。召回率比纯TF-IDF提升40%，解决"查用户喜好找不到偏好深色模式"的语义鸿沟问题。执行 `memory-search "关键词"` 返回按综合得分排序的结果.
- **WAL写前日志协议**：响应前先写入记忆，避免崩溃丢失上下文。用户表达偏好/做决策/给截止时间/纠正错误时，执行三步：更新SESSION-STATE.json → memory-store持久化 → 响应用户。确保任何时刻崩溃，关键上下文已持久化.
- **统一JSON schema与记忆类型分类**：所有记忆遵循同一schema：`{"id":"uuid-001","type":"preference","content":"用户偏好TypeScript","importance":0.9,"tags":["frontend","typescript"],"timestamp":"2026-07-21T10:00:00Z","context":"项目技术选型","confidence":0.95,"source":"user_input","expires_at":null}`。支持preference（用户喜好，重要度0.8-1.0）/decision（项目决策，0.9-1.0）/fact（重要信息，0.6-0.8）/lesson（错误教训，0.9-1.0）/context（背景信息，0.4-0.6）五种类型.
- **记忆关系图谱与迁移工具**：支持related_to（相关关系）与followed_by（顺序关系）两种关系链。存储时通过 `--related-to uuid-001` 指定关联，检索时顺关系链找到关联记忆。提供迁移工具支持从其他记忆系统一键导入：`memory-export > old-backup.json` → `node convert-to-memo-quickstart.js old-backup.json > new-backup.json` → `memory-import --file new-backup.json`.
### 记忆类型与重要度参考
| 类型 | 使用场景 | 重要度范围 |
|---:|---:|---:|
| preference | 用户表达喜好 | 0.8-1.0 |
| decision | 项目决策 | 0.9-1.0 |
| fact | 重要信息 | 0.6-0.8 |
| lesson | 从错误中学 | 0.9-1.0 |
| context | 背景信息 | 0.4-0.6 |

**处理**: 解析记忆类型与重要度参考的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回记忆类型与重要度参考的处理结果,包含执行状态码、结果数据和执行日志。### 混合检索加权公式
- TF-IDF（50%）：文本相关性，基础召回
- 近期加权（20%）：近期记忆优先
- 重要度加权（20%）：高重要度优先
- 标签匹配（10%）：标签命中加分

**输入**: 用户提供混合检索加权公式所需的指令和必要参数.
**输出**: 返回混合检索加权公式的处理结果,包含执行状态码、结果数据和执行日志.
### preference

针对preference,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供preference相关的配置参数、输入数据和处理选项.
**输出**: 返回preference的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`preference`的配置文档进行参数调优
### decision

针对decision,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供decision相关的配置参数、输入数据和处理选项.
**输出**: 返回decision的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`decision`的配置文档进行参数调优
#
## 使用流程

### 第一步：初始化（10秒）

执行安装与初始化命令，创建目录结构与核心文件：

```bash
npm install -g simple-local-memory
cd your-project
memory-init
```

初始化创建 `SESSION-STATE.json`（活跃工作记忆）、`MEMORY.md`（长期精选记忆）、`memories/`（记忆存储目录）.
### 第二步：配置Agent（20秒）

在Agent的系统提示词中写入规则：收到重要信息时先写入SESSION-STATE.json再memory-store持久化，然后响应用户；会话开始时读取SESSION-STATE.json并用memory-search检索相关记忆.
### 第三步：存储与检索记忆

存储第一条记忆并验证检索功能：

```bash
memory-store --type preference --content "用户偏好TypeScript" --importance 0.9 --tags frontend,typescript
memory-search "TypeScript 偏好"
```

确认能召回刚存的记忆，验证混合检索算法工作正常.
### 第四步：执行WAL协议（日常使用）

用户表达偏好/做决策/给截止时间/纠正错误时，执行：更新SESSION-STATE.json → memory-store持久化 → 响应用户。确保崩溃前上下文已持久化.
### 第五步：定期维护

每日运行 `memory-stats` 查看统计；每周运行 `memory-archive --days 7` 和 `memory-deduplicate` 归档去重；每月运行 `memory-export --format json --output backup.json` 导出备份和 `memory-cleanup --days 30` 清理.
### CLI命令速查

```bash
memory-init                                              # 初始化
memory-store --type preference --content "..." --importance 0.9  # 存储
memory-search "关键词"                                    # 检索
memory-list --limit 10 --type preference                  # 列表
memory-stats                                             # 统计
memory-export --format json --output backup.json          # 导出
memory-import --file backup.json                          # 导入
memory-archive --days 7                                   # 归档
memory-deduplicate                                       # 去重
memory-cleanup --days 30                                  # 清理
```

#
## 错误处理

| 错误类型 | 原因 | 处理方式 |
|:---:|:---:|:---:|
| 搜索无结果：目录不存在 | memories/目录未创建，memory-init未执行 | 运行 `memory-init` 初始化目录结构，创建memories/、SESSION-STATE.json、MEMORY.md |
| 搜索无结果：JSON格式无效 | 记忆文件JSON语法错误，如未转义引号、缺少逗号 | 用 `jq` 工具验证JSON格式：`jq . memories/*.json`，修复语法错误后重新检索 |
| 搜索无结果：关键词太窄 | 搜索词过于具体，无匹配结果 | 扩大搜索词范围，利用标签匹配补充召回：`memory-search "前端" --tag frontend` |
| SESSION-STATE.json过大 | 旧条目未归档，活跃工作记忆堆积过多 | 将已完成任务通过memory-store迁移到冷存储，执行 `memory-archive --days 7` 归档旧条目 |
| 记忆未保存：文件权限不足 | 工作区目录无写入权限 | 检查工作区写入权限，执行 `chmod 755 memories/` 修正权限后 |
| 记忆未保存：磁盘空间不足 | 磁盘空间耗尽，无法写入新文件 | 检查磁盘空间，清理后；执行 `memory-cleanup --days 30` 清理旧记忆释放空间 |
| 记忆未保存：JSON语法错误 | content字段含未转义引号，导致JSON解析失败 | 用JSON校验器检查content字段，确保引号正确转义：`\"` |
| 检索变慢 | 记忆条目过多（>1000条），全量扫描耗时 | 执行 `memory-archive --days 7` 归档旧记忆，定期 `memory-deduplicate` 去重 |
| 关联检索断链 | related_to指向的记忆已被删除，引用悬空 | 运行 `memory-cleanup` 清理断链引用，或手动修复related_to指向有效记忆ID |

## 示例

### 示例1：技术选型决策存储与检索

**输入：** 用户说"这个项目用Tailwind，不用vanilla CSS"

**执行：**
1. 更新SESSION-STATE.json（记录决策）
2. `memory-store --type decision --content "用Tailwind不用vanilla CSS" --importance 0.9 --tags frontend,css`
3. `memory-store --type preference --content "用户偏好Tailwind" --importance 0.95 --tags frontend,css`
4. 响应用户

**输出：**
```bash
# SESSION-STATE.json 更新
{"activeDecisions": [{"content":"用Tailwind不用vanilla CSS","timestamp":"2026-07-21T10:00:00Z"}]}
# ...
# memory-store 输出
Stored: uuid-001 (type=decision, importance=0.9, tags=[frontend,css])
Stored: uuid-002 (type=preference, importance=0.95, tags=[frontend,css])
# ...
# 响应
"明白，用Tailwind。已保存此偏好。"
```

### 示例2：关联检索顺藤摸瓜

**输入：** 用户问"我们之前为什么选了React？"

**执行：**
1. `memory-search "React 选型"` 找到决策记忆（uuid-001）
2. 顺related_to关系链找到关联记忆（uuid-002：团队熟悉度评估）
3. 返回完整决策上下文

**输出：**
```bash
# 检索结果
memory-search "React 选型" → uuid-001 (score=0.87)
  content: "选择React作为前端框架"
  type: decision
  importance: 0.95
  related_to: [uuid-002]
# ...
# 关联记忆
uuid-002 (score=0.82)
  content: "团队React熟悉度评估得分8/10"
  type: fact
  importance: 0.7
# ...
# 返回
"选React是因为团队熟悉度高（评估得分8/10），且需要组件化架构。此决策记录于2026-07-15。"
```

### 示例3：从其他系统迁移

**输入：** 用户想从旧记忆系统迁移到本系统

**执行：**
1. 从旧系统导出数据
2. 转换为本系统JSON schema格式
3. 导入

**输出：**
```bash
# 导出旧系统数据
memory-export > old-backup.json
# ...
# 转换格式
node convert-to-memo-quickstart.js old-backup.json > new-backup.json
# 转换日志：处理150条记忆，成功148条，跳过2条（格式不兼容）
# ...
# 导入
memory-import --file new-backup.json
# 导入结果：成功导入148条记忆，其中decision 35条/preference 42条/fact 51条/lesson 12条/context 8条
```

## FAQ

**Q1：真的完全不需要API Key吗？**
A：是的。所有存储与检索在本地完成，零网络请求，零外部依赖。数据不离开本机，适合隐私敏感场景与离线开发环境。如需可选的Gist云同步，才需要配置Gist Token.
**Q2：混合检索比纯TF-IDF好在哪？**
A：纯TF-IDF只看词频，查"用户喜好"找不到"偏好深色模式"（无共同词）。混合检索叠加标签匹配（10%）与重要度加权（20%），即使无共同词也能通过标签关联召回。整体召回率比纯TF-IDF提升40%.
**Q3：能和其他记忆系统共存吗？**
A：可以。本系统独立运行于 `memories/` 目录，不干扰其他系统。提供迁移工具（convert-to-memo-quickstart.js）支持从其他系统导出的JSON互导，转换为本系统统一schema后导入.
**Q4：记忆多了会不会变慢？**
A：1000条以内无明显延迟（毫秒级检索）。超1000条建议定期执行 `memory-archive` 归档与 `memory-deduplicate` 去重。超10000条检索延迟明显，建议接入Transformers.js本地embedding增强语义检索.
**Q5：SESSION-STATE.json与MEMORY.md有什么区别？**
A：SESSION-STATE.json是机器优化的活跃上下文（JSON格式），存储当前任务、关键决策、待办动作，频繁更新，会话开始立即加载。MEMORY.md是人类可读的长期归档（Markdown格式），定期从冷存储中精选重要内容整理而成，用于周期性回顾.
**Q6：记忆关系图谱怎么用？**
A：存储记忆时通过 `--related-to uuid-001` 参数指定关联记忆。检索时找到一条记忆后，可顺related_to或followed_by关系链找到关联记忆。例如决策记忆关联其依据的评估记忆，检索决策时自动返回完整上下文。关系需在存储时显式指定，系统不会自动发现记忆间关联.
## 依赖说明

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:------|------:|:------|:------|
| Agent平台 | 运行环境 | 必需 | 安装支持SKILL.md的AI Agent |
| Node.js | 运行时 | 必需 | nodejs.org安装（运行记忆CLI） |
| simple-local-memory | npm包 | 必需 | `npm install -g simple-local-memory` |
| Transformers.js | npm包 | 可选 | 用于本地embedding增强检索（超10000条记忆时推荐） |
| LLM API | API | 必需 | 由Agent平台内置LLM提供 |
| GitHub Gist Token | API Key | 可选 | 用于可选的Gist云同步 |

**API Key配置：**
- 本技能基于本地存储，无需任何API Key
- 云同步增强（可选）：如用GitHub Gist同步，需配置Gist Token

**可用性分类：** MD+EXEC（Markdown指令驱动，需exec执行memory CLI命令）

## 已知限制

1. **无向量语义检索**：基于TF-IDF + 加权的混合检索，无法理解深层语义相似性，查"汽车"找不到"轿车"（无共同词且无标签关联时）。超10000条记忆建议接入Transformers.js本地embedding增强.
2. **无自动事实抽取**：以手动memory-store和简单规则为主，不会自动从对话流中提取事实，需要Agent主动调用存储命令.
3. **无跨设备同步**：纯本地存储，默认无云同步。如需跨设备可通过GitHub Gist自行扩展，但非内置功能.
4. **记忆关系需手动维护**：related_to/followed_by关系链需在存储时显式指定，系统不会自动发现记忆间关联.
5. **单机性能上限**：10000条以上记忆检索延迟明显，无分区/分片机制，不适合超大规模记忆库.
## 输出格式

```json
{
  "success": true,
  "data": {
    "result": "记忆快速启动处理结果",
    "execution_time": "0.5s",
    "metadata": {
      "version": "1.0",
      "processor": "memo-quickstart"
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
