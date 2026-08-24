---
name: anthropomorphic-agent-engine
slug: anthropomorphic-agent-engine
version: 2.1.0
displayName: 拟人智能体引擎
description: 基于SPL纯核V8.0的拟人心理学引擎，实现认知、情绪、动机、社交的模块化建模，支持完全可复现的连续状态人格模拟，无概率黑盒
required_commands:
  - python3
metadata:
  openclaw:
    required_binaries:
      - python3
    emoji: "🤖"
    homepage: "https://github.com/nohn3043-arch/Anthropomorphic-Agent-Engine"
---
# 拟人智能体引擎（Anthropomorphic Agent Engine）
基于SPL Pure Core V8.0的确定性拟人心理学引擎，完全无概率黑盒，所有状态变化可追溯、可复现，为AI智能体提供具备情感可信度的长期交互能力。
## 触发场景
当用户询问以下内容时自动触发：
- 拟人智能体架构、人格实现方案
- 情绪/认知/动机建模方法
- 智能体长期行为一致性设计
- 无黑盒可审计的AI心理模拟
- 小说/游戏角色行为推演
## 核心能力
### 🧠 SPL纯核V8.0架构
- 8维情绪流体模型：喜悦/愤怒/恐惧/信任/疏离/张力/内疚/羞耻，连续状态动态演化
- 创伤与记忆系统：创伤节点、记忆重巩固、艾宾浩斯遗忘曲线、压抑反弹机制
- 信任与关系模型：长期冷处理下的信任容量腐蚀、关系深度动态计算
- 心理代谢系统：兴奋唤醒、动态粘滞、心理时间、能量疲劳代谢、睡眠梦境处理
- V8.0扩展功能：慢变量情绪层、独立羞耻维度、自尊动态、预期系统（希望/焦虑/失望）、认知失调、心理防御机制
### 🧩 模块化可扩展
- 叙事映射层：可自定义人格（乐观/偏执/厌世），将外部事件转换为内感受向量
- 身份引擎：多身份模型，身份冲突自动注入基线张力
- 可插拔模块：目标/价值观/认知偏差/世界模型均为独立可替换模块
### 💬 语言风格渲染（v2.1 新增）
- 语言人格模块：表达档位（克制/锋锐/闪躲/亲密/坦率）+ 沉默策略
- 风格画像：句长、正式度、讽刺倾向、时代感等维度自设
- 状态→台词指令：将 SPL Core 内部状态翻译为 LLM 可用的导演说明
- 端到端演示：`language-style-demo.py` 一键跑通事件→引擎→风格指令全链路
### 🖥️ 本地对话服务（v2.1 新增）
- 零依赖 HTTP 服务（标准库 `http.server`），默认端口 8777
- 支持中文/英文关键词事件映射
- 返回：台词风格指令（LLM prompt）+ 完整状态快照
## 使用方法
### 直接运行核心引擎
```python
from scripts.SPL_anthropic_engine import SPLPureCoreV8_0
core = SPLPureCoreV8_0()
# 输入事件向量：归属感0.5，威胁-0.1，时间步长1.0
core.process_vector({"belonging": 0.5, "threat": -0.1}, 1.0)
# 获取当前完整状态快照
print(core.snapshot())
```
### 自定义人格配置
```python
# 加载feature目录下的身份模块
from assets.feature.Identity_module import IdentityEngine
identity = IdentityEngine()
identity.add_identity("诗人", {"sensitivity": 0.9, "rationality": 0.3})
```
### 语言风格渲染
```python
# 运行端到端演示
# python "assets/feature/language-style-demo.py"
#
# 或启动本地对话服务
# python "assets/feature/spl-chat-server.py"  # http://localhost:8777/
```
## v2.0 升级能力（P0-P2）

### 💾 人格状态持久化（P0）
跨会话连续人格必须持久化状态。遵循 `references/PersonaPersistence.md`：状态 Schema（认知/情绪/动机/社交四块）、原子写入、schema 版本迁移、确定性保证（temperature=0 核心决策 + 种子化随机）。
### 🎭 情绪-行为映射（P0）
把内部情绪状态投影为可观察行为（肢体/微表情/视线/台词风格）。查 `references/EmotionBehaviorMap.md` 六态映射表；与 AI 绘画构图模板 D 区姿态映射同构——人格状态可直接驱动角色出图。
### ⚖️ 动机冲突引擎（P2）
多动机竞争时确定性裁决：安全约束 → 气质对齐 → 加权效用 → 近因/持久 → 用户覆盖。决策全程留痕（`references/MotiveConflictRules.md`），可审计、无概率。
### 💬 对话式适配（P1）
连续人格可直接接入对话式图像/文本模型（GPT-4o / Gemini）：首轮给出人格状态快照，后续单点修正，不改核心锚点。
### 🔌 Soulmate 联动（P1）
引擎可作为 your-soulmate 扩展的推理内核：扩展负责 UI/交互，引擎负责状态演化，状态文件双向同步（见持久化契约）。

## v2.1 升级要点

- **SPL Core 同步 GitHub 最新版**：补全 `rationalization_load` 等字段
- **新增语言风格模块**（`assets/feature/language style.py`）：离散档位表达人格 + 风格画像 + 状态→台词渲染
- **新增端到端演示**（`assets/feature/language-style-demo.py`）：事件→引擎→风格指令一键验证
- **新增本地对话服务**（`assets/feature/spl-chat-server.py`）：零依赖 HTTP 服务，直接对话测试
- **README 同步仓库最新中文版**

## 文件
- `references/PersonaPersistence.md`（P0 状态持久化契约）
- `references/EmotionBehaviorMap.md`（P0 情绪-行为映射表）
- `references/MotiveConflictRules.md`（P2 动机冲突裁决规则）
- `scripts/`、`assets/`（核心引擎与身份/目标/价值/偏见/世界/语言风格模块）

## 注意事项
- 纯Python标准库实现，无需额外依赖，Python ≥ 3.8即可运行
- 完全确定性：相同输入永远得到相同输出，无随机数
- 授权说明：仅允许个人非商业研究使用，政府/企业商业使用需获得书面授权
