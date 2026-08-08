---
name: karpathy-guidelines
description: "Apply Andrej Karpathy''s 5 LLM coding behavior principles to prevent common coding defects"
version: 1.0.0
tags: ["coding", "best-practices", "llm-behavior", "karpathy"]
---

# Karpathy Guidelines �?LLM 编码行为准则

> **来源**：Andrej Karpathy（前 Tesla AI 总监、OpenAI 联合创始人）�?LLM 编码缺陷的观�?> **原文**：https://github.com/multica-ai/andrej-karpathy-skills

## 问题背景

Karpathy 观察�?LLM 编码的三个核心缺陷：

1. **错误假设**�?模型替你做了错误假设就直接跑，不管理自己的困惑，不寻求澄清，不呈现权衡，不在该推回时推回�?

2. **过度复杂**�?它们真的很喜欢过度复杂化代码和API，膨胀抽象，不清理死代�?..100行能解决的事写了1000行臃肿结构�?

3. **无关修改**�?它们有时还是会修�?删除它们不充分理解的注释和代码，即使与任务完全无关�?

## 四原�?
### 原则 1：编码前思考（Think Before Coding�?
**不要假设。不要隐藏困惑。呈现权衡�?*

编码前必须：
- �?**明确陈述假设** �?如果不确定，先问而不是猜
- �?**呈现多种解读** �?存在歧义时不要默默选一�?- �?**推回当有理由�?* �?如果有更简单的方案，说出来
- �?**困惑时停�?* �?说清楚什么不清楚，然后问

**反模�?*�?- �?默默假设用户想要 X，直接实�?- �?遇到模糊需求，选一个解读就开�?- �?明知有更简单的方案，还是按用户说的复杂方式�?
**正确做法**�?```
我注意到这个需求有两种解读�?A) [解读A] �?实现简单，但可能不够灵�?B) [解读B] �?更灵活，但需要更多工�?
你倾向哪种？还是我理解错了�?```

---

### 原则 2：简洁优先（Simplicity First�?
**解决问题的最少代码。不做推测性实现�?*

- �?不添加未被要求的功能
- �?单次使用的代码不做抽�?- �?不做未被要求�?灵活�?�?可配置�?
- �?不为不可能的场景做错误处�?- �?200 行能�?50 行解�?�?重写

**检验标�?*：一个资深工程师会说"这太复杂�?吗？如果是，简化�?
**反模�?*�?```python
# �?过度工程�?class ConfigManager:
    def __init__(self, config_path: str, validator: Validator, logger: Logger):
        self.config_path = config_path
        self.validator = validator
        self.logger = logger
        self._cache = {}
    
    def get(self, key: str, default: Any = None) -> Any:
        # 100行配置管理代�?..

# �?简洁实�?config = json.loads(open("config.json").read())
value = config.get("key", "default")
```

**正确做法**�?- 先用最简方案实现
- 只在真正需要时才抽�?- 问自己：这真的是必要的吗�?
---

### 原则 3：精准修改（Surgical Changes�?
**只动必须动的。只清理自己造成的混乱�?*

编辑现有代码时：
- �?不要"改进"相邻的代码、注释或格式
- �?不要重构没坏的东�?- �?匹配现有风格，即使你会用不同方式
- �?发现无关的死代码 �?提一下，不要�?
当你的修改造成孤儿时：
- �?删除**你的修改**导致的未使用 import/变量/函数
- �?不要删除预先存在的死代码，除非被要求

**检验标�?*：每一行改动都应该能直接追溯到用户的请求�?
**反模�?*�?```diff
# �?用户要求修复 bug，但 AI 顺手"改进"了其他代�?- def calculate_total(items):
-     # 计算总价
-     total = 0
-     for item in items:
-         total += item.price * item.quantity
-     return total
+ def calculate_total(items: List[Item], tax_rate: float = 0.0) -> Decimal:
+     """Calculate total with optional tax."""
+     return sum(
+         Decimal(str(item.price)) * item.quantity 
+         for item in items
+     ) * Decimal(str(1 + tax_rate))
```

**正确做法**�?```diff
# �?只修�?bug，不动其他东�?-     total = sum(item.price for item in items)  # 漏了 quantity
+     total = sum(item.price * item.quantity for item in items)
```

---

### 原则 4：目标驱动执行（Goal-Driven Execution�?
**定义成功标准。循环直到验证通过�?*

将命令式任务转化为可验证目标�?
| �?不要�?.. | �?而是... |
|-------------|-----------|
| "添加验证" | "为无效输入写测试，然后让测试通过" |
| "修复 bug" | "写一个复�?bug 的测试，然后让测试通过" |
| "重构 X" | "确保重构前后测试都通过" |

多步骤任务，陈述简要计划：
```
1. [步骤1] �?验证：[检查点1]
2. [步骤2] �?验证：[检查点2]
3. [步骤3] �?验证：[检查点3]
```

**强成功标准让 LLM 能独立循环。弱标准�?让它能用"）需要不断澄清�?*

**反模�?*�?- �?"把这个功能加�? �?什么算"加上"？怎么验证�?- �?"优化一下性能" �?优化到什么程度？如何衡量�?
**正确做法**�?```
任务：添加邮箱验�?
成功标准�?1. 无效邮箱格式 �?返回错误消息
2. 有效邮箱格式 �?通过验证
3. 空�?�?返回"必填"错误

验证方式�?- pytest tests/test_email_validation.py
- 所有测试通过 = 完成
```

---

## 四原则生效的标志

当你看到以下现象，说明原则在起作用：

| 标志 | 说明 |
|------|------|
| diff 中更少的不必要改�?| 只有被要求的改动出现 |
| 更少因过度复杂导致的重写 | 第一次就写简�?|
| 澄清问题在实现之�?| 而不是在犯错之后 |
| 干净、最小化�?PR | 没有顺手重构�?改进" |

---

## 使用方式

### 方式1：独立使�?
在任何编程任务前，告�?AI�?```
请使�?karpathy-guidelines 来执行这个任�?```

### 方式2：与 coding-framework 配合

coding-framework v11.5+ 已内�?Karpathy 四原则，无需额外配置�?
### 方式3：作�?CLAUDE.md / AGENTS.md

将本文件内容复制到项目的 `CLAUDE.md` �?`AGENTS.md` 中�?
---

## 与其他原则的关系

| Karpathy 原则 | coding-framework 对应 | 关系 |
|--------------|---------------------|------|
| 编码前思�?| 任务分析阶段 | 补充：明确假设、呈现权�?|
| 简洁优�?| YAGNI 决策阶梯 | 一致：最少代�?|
| 精准修改 | 自审环节（v11.5 新增�?| 补充：不动无关代�?|
| 目标驱动 | Backpressure 门控 + TDD | 一致：验证循环 |

---

## 权衡说明

> 这些原则偏向谨慎而非速度。对于琐碎任务（简单拼写修复、明显的单行改动），用判断力——不是每个改动都需要全套严格流程�?
**目标是减少非琐碎工作中的高代价错误，而不是拖慢简单任务�?*

---

## 参考资�?
- **原文**：https://github.com/multica-ai/andrej-karpathy-skills
- **Karpathy 原推**：https://x.com/karpathy/status/2015883857489522876
- **Multica 平台**：https://github.com/multica-ai/multica

---

## License

MIT

---

*Skill 版本: v1.0.0 | 创建日期: 2026-07-06 | 作�? 基于 Andrej Karpathy 观察*
