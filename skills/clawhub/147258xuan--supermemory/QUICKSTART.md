# SuperMemory V1.2 — 5分钟快速上手

## 一分钟理解权重

```
用户红线  → 🔒 Pinned（永不遗忘）← V1.2 新增
你妈生日  → W=95 (永久，不衰减)
宸总不吃辣 → W=65 (偏好，慢衰减)
项目计划  → W=75 (重要，较慢)
想法笔记  → W=55 (普通，中速)
昨天午饭  → W=35 (日常，快速衰减) → 一周后自动忘
```

**核心原则：重要的记住，不该忘的锁定，不重要的自然淡出。**

## 三分钟上手

```python
from supermemory import SuperMemory

m = SuperMemory()

# 1. 写入记忆（自动赋权 + 锁定关键信息）
m.remember("宇宸总爱吃香菜，不吃辣", weight=80)
m.remember("今天午饭宫保鸡丁")  # 自动 W=35
m.remember("V8.5核心架构：插嘴系统+嵌入基座")  # 自动 W=95

# 🆕 V1.2: 锁定关键信息——永不遗忘
node_id = m.remember("用户红线：永不授权给大厂", weight=95, pinned=True)

# 2. 查询记忆（自动触发窄门复活）
results = m.recall("宸总吃什么")
for r in results:
    pin_tag = "🔒" if r.get("pinned") else ""
    print(f"{pin_tag}[W{r['weight']}] {r['digest']}")
# → 🔒[W101] 用户红线：永不授权给大厂（永远排最前面）
# → [W80] 宇宸总爱吃香菜，不吃辣

# 3. 执行衰减（锁定记忆自动跳过）
forgotten = m.decay()
print(f"本轮遗忘: {len(forgotten)} 条")
# 锁定记忆安然无恙

# 4. 管理锁定
m.list_pinned()      # 查看所有锁定
m.unpin(node_id)     # 解锁某条
m.pin(node_id)       # 重新锁定

# 5. 查看统计
print(m.stats())
# → {'total_nodes': 5, 'pinned': 2, ...}
```

## 常见场景

| 我想…… | 代码 |
|--------|------|
| 记住重要的事 | `m.remember("内容", weight=90)` |
| 自动判断重要性 | `m.remember("内容")` |
| 🆕 锁定永不遗忘 | `m.remember("...", pinned=True)` |
| 🆕 事后锁定 | `m.pin(node_id)` |
| 🆕 解锁恢复衰减 | `m.unpin(node_id)` |
| 查记忆 | `m.recall("查询词")` |
| 定期衰减 | `m.decay()` |
| 导出备份 | `m.export_json("backup.json")` |
| 看统计 | `m.stats()` |

## 窄门复活参数调节

```python
m = SuperMemory()

# 默认值（推荐）
m.REVIVE_THRESHOLD = 8      # W≥8 才进窄门
m.REVIVE_WINDOW = 7*86400   # 7天内被访问可复活
m.REVIVE_WEIGHT = 30        # 复活后恢复到 W=30

# 激进遗忘（记忆池 >500 条）
m.REVIVE_THRESHOLD = 10     # 缩小窄门范围
m.REVIVE_WINDOW = 3*86400   # 3天过期

# 保守保留
m.REVIVE_WEIGHT = 40        # 复活后更高权重
```

## 锁定 vs 高权重：如何选择

| 场景 | 用 pin() | 用 weight=95+ |
|------|----------|---------------|
| API Key / 密码 / 安全规则 | ✅ pin | — |
| 用户红线 / 铁律 | ✅ pin | — |
| 核心身份定义 | ✅ pin | — |
| "删它就是删我"级别信息 | ✅ pin | — |
| 重要但可更新的偏好 | — | ✅ W=85 |
| 项目架构信息 | — | ✅ W=75 |
| 长期有效的参考信息 | — | ✅ W=65 |

> **原则**：pin 给"永远不能忘"的，weight 给"很重要但可以被更高优先级覆盖"的。

## 安装

```bash
# 零依赖即可运行
python supermemory.py

# 推荐安装 jieba 获得更好的中文分词
pip install jieba
```

## 文件说明

| 文件 | 作用 |
|------|------|
| `supermemory.py` | 主引擎 (~250行) |
| `SKILL.md` | 完整文档 |
| `QUICKSTART.md` | 本文件 |
| `dashboard.html` | 可视化面板 |
| `LICENSE` | MIT 许可证 |

---

*SuperMemory V1.2 — 记住重要的，锁定不能忘的。*
