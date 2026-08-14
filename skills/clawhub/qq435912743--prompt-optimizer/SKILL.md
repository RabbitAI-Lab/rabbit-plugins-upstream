---
name: prompt-optimizer
description: |
  提示词迭代优化器。把一段粗糙/平淡的 prompt 系统化升级为结构化、强约束、带输出格式的高质量 prompt，并做版本管理（v1/v2...）+ 双 prompt 基准对比选优。覆盖角色设定、上下文、分步指令、输出格式、约束、示例占位、链式思考、自检步骤等增强。当用户需要"优化这段提示词""让 prompt 更强""对比两个 prompt""prompt versioning""improve my prompt"时调用。
agent_created: true
visibility: "public"
---

# 提示词优化器（Prompt Optimizer）

把"凭感觉写的 prompt"升级为"工程化的 prompt"：结构化、强约束、可复现。配合 self-eval 形成闭环——优化后用 rubric 评分，分数低的维度再针对性增强。

## 适用场景
- 新任务起步时，从一句话需求生成可用 prompt
- 已有 prompt 效果不好，做系统化增强
- A/B 两个 prompt 哪个更好（bench 对比选优）
- 把验证过的 prompt 沉淀为团队模板（版本管理）

## 增强项（apply 时可按场景取舍）
1. **角色设定** — 注入领域专家身份（从任务推断领域）
2. **上下文块** — 明确背景/已知信息/约束
3. **分步指令** — 把要求拆成编号步骤
4. **输出格式** — 强制 JSON / Markdown / 表格等机器可读结构
5. **约束** — 显式"必须/不要"清单
6. **示例占位** — 预留 few-shot 位置
7. **链式思考** — 先推理再作答
8. **自检步骤** — 交付前按清单自检

## 标准工作流
```bash
# 优化一个弱 prompt（输出到 prompt.optimized.md，并写入版本日志）
python scripts/optimize.py --task "把中文论文摘要翻译成英文并保持学术风格" \
    --prompt weak.txt --out prompt.optimized.md
# 对比两个 prompt 哪个更强
python scripts/bench.py --a p1.md --b p2.md --task "..." --out bench.json
```

## 质量门禁
- 优化后建议用 self-eval 评分；overall < 0.6 的维度回到对应增强项补强
- 版本日志 `optimize_log.json` 记录每次变更，便于回滚

## 自进化学习系统
```bash
python scripts/learner.py record . --capability "提示词优化" [--fail --error <类型> --note <说明>]
python scripts/learner.py insight .
python scripts/learner.py reflect .
```
- 某增强项对某类任务特别有效 → 记录，reflect 建议设为默认开启
- 用户常用输出格式 → `prefer` 记录，未来默认套用
