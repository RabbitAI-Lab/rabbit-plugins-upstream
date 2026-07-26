---
slug: "elite-longterm-memory"
name: "elite-longterm-memory"
version: 1.2.4
displayName: "长期记忆系统"
summary: "六层记忆架构,从会话状态到云端备份,结合WAL协议与向量检索。"
license: "Proprietary"
description: |-
  融合六种成熟方法的AI代理记忆架构:会话状态热内存、向量数据库
  温存储、Git笔记冷存储、策展归档、云端备份与自动事实提取。通过
  WAL协议保证持久性,覆盖记忆卫生、故障诊断与即时修复。适用于
  独立开发者、企业团队和自动化工作流场景.
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
tags:
  - 智能助手
# 定价元数据
suggested_price: "99.9 CNY/monthly"
pricing_tier: "L4-企业级"
pricing_model: "monthly"

---
# 长期记忆系统

融合六种成熟方法的AI代理记忆架构,从会话状态到云端备份,通过WAL协议保证持久性,永不丢失上下文、决策与教训.
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | 长期记忆系统处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-----|:-----|
| 基础功能 | 支持 | 支持 |
| 长期记忆系统WAL协议与向量检索 | 不支持 | 支持 |
| 多租户管理与权限分配 | 不支持 | 支持 |
| 操作审计与合规日志 | 不支持 | 支持 |
| 自定义仪表盘与报表 | 不支持 | 支持 |
| API开放与第三方集成 | 不支持 | 支持 |

## 依赖说明

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
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统.
## 核心能力

### 1. HOT RAM 会话状态
- `SESSION-STATE.md` 作为代理的"内存",在压缩、重启、分心中存活
- 包含当前任务、关键上下文、待办动作、近期决策四个区块
- 规则:在响应用户之前先写入,由用户输入触发而非代理记忆

**处理**: 解析HOT RAM 会话状态的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回HOT RAM 会话状态的处理结果,包含执行状态码、结果数据和执行日志.
### 2. WARM STORE 向量检索
- 基于向量数据库的语义搜索,跨所有记忆自动召回相关上下文
- `memory_recall query="project status" limit=5` 召回相关记忆
- `memory_store text="User prefers dark mode" category="preference" importance=0.9` 存储记忆
- 配置 `minScore: 0.3`、`maxResults: 10` 控制召回质量与数量

### 3. COLD STORE 知识图谱
- 结构化决策、教训与上下文,分支感知
- `python3 memory.py -p $DIR remember '{"type":"decision","content":"Use React for frontend"}' -t tech -i h` 存储决策
- `python3 memory.py -p $DIR get "frontend"` 检索主题记忆
- 永久性决策记录,跨会话稳定

**输入**: 用户提供COLD STORE 知识图谱所需的指令和必要参数.
**处理**: 解析COLD STORE 知识图谱的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回COLD STORE 知识图谱的处理结果,包含执行状态码、结果数据和执行日志.
### 4. CURATED ARCHIVE 策展归档
- 人类可读长期记忆,日志+提炼智慧
- 结构:`MEMORY.md`(策展长期,小于5KB)+ `memory/YYYY-MM-DD.md`(每日日志)+ `memory/topics/`(主题文件)
- 每日日志记录当天活动,定期合并到 `MEMORY.md`

**处理**: 解析CURATED ARCHIVE 策展归档的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回CURATED ARCHIVE 策展归档的处理结果,包含执行状态码、结果数据和执行日志.
### 5. CLOUD BACKUP 云端同步
- 跨设备同步,与知识库对话
- `supermemory add "Important context"` 添加上下文
- `supermemory search "what did we decide about..."` 搜索决策
- 可选层,依赖 API Key

**输入**: 用户提供CLOUD BACKUP 云端同步所需的指令和必要参数.
**输出**: 返回CLOUD BACKUP 云端同步的处理结果,包含执行状态码、结果数据和执行日志.
### 6. AUTO-EXTRACTION 事实提取
- 自动从对话中提取偏好、决策、事实
- 去重并更新已有记忆
- 相比原始历史减少80% token消耗
- 跨会话自动工作

**输入**: 用户提供AUTO-EXTRACTION 事实提取所需的指令和必要参数.
**处理**: 解析AUTO-EXTRACTION 事实提取的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回AUTO-EXTRACTION 事实提取的处理结果,包含执行状态码、结果数据和执行日志.
### 7. WAL协议
写前日志:在响应之前写入状态,而非之后.
- 用户陈述偏好 → 写入 `SESSION-STATE.md` → 再响应
- 用户做决策 → 写入 → 再响应
- 用户给截止日期 → 写入 → 再响应
- 用户纠正你 → 写入 → 再响应
- 原因:若先响应再崩溃/压缩,上下文丢失;WAL保证持久性

**处理**: 解析WAL协议的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回WAL协议的处理结果,包含执行状态码、结果数据和执行日志.
### 8. 记忆卫生
每周维护:
- 审查 `SESSION-STATE.md`,归档已完成任务
- 检查向量库垃圾:`memory_recall query="*" limit=50`
- 清除无关向量:`memory_forget id=<id>`
- 合并每日日志到 `MEMORY.md`

**输入**: 用户提供记忆卫生所需的指令和必要参数.
**输出**: 返回记忆卫生的处理结果,包含执行状态码、结果数据和执行日志.
### 9. 故障模式诊断
| 失败模式 | 原因 | 修复 |
|:---:|:---:|:---:|
| 忘记一切 | `memory_search` 禁用 | 启用并添加 API key |
| 文件未加载 | 代理跳过读取记忆 | 加入 AGENTS.md 规则 |
| 事实未捕获 | 无自动提取 | 使用事实提取工具或手动记录 |
| 子代理隔离 | 不继承上下文 | 在任务提示中传递上下文 |
| 重复错误 | 教训未记录 | 写入 `memory/lessons.md` |

**输入**: 用户提供故障模式诊断所需的指令和必要参数.
**处理**: 解析故障模式诊断的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回故障模式诊断的处理结果,包含执行状态码、结果数据和执行日志.
### 10. 即时修复检查表
- 忘记偏好 → 在 `MEMORY.md` 添加 `## Preferences` 段
- 重复错误 → 每个错误记录到 `memory/lessons.md`
- 子代理缺上下文 → 在 spawn 任务提示中包含关键上下文
- 忘记近期工作 → 严格的每日文件纪律
- 记忆搜索不工作 → 检查 `OPENAI_API_KEY` 是否设置

**输入**: 用户提供即时修复检查表所需的指令和必要参数.
**输出**: 返回即时修复检查表的处理结果,包含执行状态码、结果数据和执行日志.
#
## 适用场景

| 场景 | 输入 | 输出 |
|:------|------:|:------|
| 会话开始 | 无 | 读取 SESSION-STATE.md + 召回相关记忆 + 检查当日日志 |
| 对话中捕获 | 用户陈述偏好/决策 | 写入 SESSION-STATE.md → 存入知识图谱 → 存入向量库 → 再响应 |
| 会话结束 | 无 | 更新 SESSION-STATE.md + 迁移重要项到 MEMORY.md + 创建当日日志 |
| 每周维护 | 无 | 审查会话状态、清理向量垃圾、合并日志 |
| 故障诊断 | 记忆失效症状 | 对应失败模式与修复步骤 |

不适用于:需要100%确定性的关键决策、无LLM环境的纯规则系统.
## 使用流程

1. 创建 `SESSION-STATE.md` 热内存文件
2. 在配置中启用向量检索(`minScore: 0.3`、`maxResults: 10`、`autoRecall: true`、`minImportance: 0.7`)
3. 初始化 Git 笔记冷存储
4. 验证 `MEMORY.md` 与 `memory/` 目录结构
5. (可选)配置云端同步 API Key
6. 会话开始读取热内存,对话中遵循WAL协议,会话结束更新状态
7. 每周执行记忆卫生

#
## 示例

### 示例1:WAL协议执行
```
用户: "这个项目用 Tailwind,不用原生 CSS"
# ...
代理(内部):
1. 写入 SESSION-STATE.md: "Decision: Use Tailwind, not vanilla CSS"
2. 存入知识图谱: 关于CSS框架的决策
3. memory_store: "User prefers Tailwind over vanilla CSS" importance=0.9
4. 然后响应: "明白,用 Tailwind..."
```

### 示例2:配置片段
```json
{
  "memorySearch": {
    "enabled": true,
    "provider": "llm-provider",
    "sources": ["memory"],
    "minScore": 0.3,
    "maxResults": 10
  },
  "plugins": {
    "entries": {
      "memory-lancedb": {
        "enabled": true,
        "config": {
          "autoCapture": false,
          "autoRecall": true,
          "captureCategories": ["preference", "decision", "fact"],
          "minImportance": 0.7
        }
      }
    }
  }
}
```

### 示例3:SESSION-STATE.md 结构
```markdown
## Current Task
重构用户认证模块
# ...
## Key Context
- User preference: 优先函数式风格
- Decision made: 用 JWT 不用 session
- Blocker: 等待设计团队确认登录页
# ...
## Pending Actions
- [ ] 完成token刷新逻辑
- [ ] 编写认证中间件测试
# ...
## Recent Decisions
2026-07-21: 采用 JWT 无状态认证
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---:|:---|---:|
| 代理对话中频繁遗忘 | `SESSION-STATE.md` 未更新 | 检查WAL协议执行,确认在响应前写入 |
| 注入无关记忆 | autoCapture 开启或 minImportance 过低 | 关闭 autoCapture,提高 `minImportance` 阈值至 0.7+ |
| 记忆过大召回缓慢 | 向量库累积垃圾 | 运行卫生流程:`memory_recall query="*" limit=50` 清除旧向量 |
| Git笔记不持久 | 未同步到远程 | 执行 `git notes push` 同步到远程仓库 |
| `memory_search` 无返回 | API Key 未设置或配置错误 | `echo $OPENAI_API_KEY` 验证,确认 memorySearch 启用 |
| 子代理缺乏上下文 | spawn 时未传递记忆 | 在任务提示中包含关键上下文与决策摘要 |
| 事实提取工具报错 | API Key 无效或额度耗尽 | 验证 `MEM0_API_KEY`,检查额度,降级为手动记录 |

## 常见问题

### Q1: WAL协议为何要在响应前写入?
A: 若先响应再崩溃或压缩,上下文丢失。WAL(写前日志)保证持久性:用户陈述偏好/决策/截止日期/纠正时,先写入 `SESSION-STATE.md` 再响应,即使中途断电也能恢复.
### Q2: 向量检索的 `minScore: 0.3` 与 `maxResults: 10` 如何调优?
A: `minScore` 过低会注入无关记忆,过高会漏掉相关项;0.3 是平衡起点。`maxResults` 控制上下文窗口占用,10 条通常够用。若召回噪声多,提高 `minScore` 到 0.5;若漏召回,降到 0.2.
### Q3: `minImportance: 0.7` 意味着什么?
A: 重要性低于 0.7 的记忆不会被自动捕获。偏好与决策设为 0.9,普通事实设为 0.7,临时信息不存储。这避免向量库被低价值记忆污染.
### Q4: `MEMORY.md` 为何要小于 5KB?
A: `MEMORY.md` 是策展的长期摘要,每次会话开始都会读取。过大消耗上下文窗口且稀释关键信息。详细内容拆分到 `memory/topics/` 主题文件,`MEMORY.md` 只放索引与最重要的决策.
### Q5: 事实提取工具如何减少80% token?
A: 原始对话历史包含大量寒暄与重复,事实提取工具自动抽取偏好、决策、事实等结构化条目,去重并更新。后续会话只注入提取后的精炼记忆,而非完整历史,token 消耗大幅下降.
### Q6: 子代理如何继承记忆上下文?
A: 子代理默认不读取父代理的记忆文件。在 spawn 任务提示中显式包含关键上下文(当前任务、相关决策、用户偏好),或让子代理调用 `memory_recall` 自行检索.
## 已知限制

- 需要 LLM 支持语义检索,无 API Key 环境仅能用文件记忆
- 向量数据库需要磁盘空间存储向量索引
- 云端同步依赖外部服务可用性
- 记忆质量依赖写入纪律,WAL协议需严格执行
- 不适用于需要100%确定性的关键决策场景

## 输出格式

```json
{
  "success": true,
  "data": {
    "result": "长期记忆系统处理结果",
    "execution_time": "0.5s",
    "metadata": {
      "version": "1.0",
      "processor": "elite-longterm-memory"
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
