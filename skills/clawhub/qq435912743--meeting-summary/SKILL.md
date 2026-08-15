---
name: meeting-summary
description: |
  会议纪要助手。把会议录音转写/聊天记录/笔记整理成结构化纪要：结论、行动项（owner+时限）、待决问题、关键决策。当用户需要"整理会议纪要""把这段对话总结一下""提取行动项"时调用。
agent_created: true
visibility: "public"
---

# 会议纪要助手

把零散的会议记录（转写文本、聊天流、笔记）提炼成可执行的纪要。核心：**行动项必须带 owner 与时限，决策与待决分开**。

## 标准输出结构
1. **一句话结论**：这场会达成了什么
2. **关键决策**：拍板了哪些事（含理由摘要）
3. **行动项**：每条 `[动作] @owner 截止<时间>` —— 这是最有价值的部分
4. **待决/风险**：悬而未决、需要跟进的
5. **下次会议议题**（如有）

## 标准工作流
使用 `scripts/extract_actions.py` 从文本中抽取 `@某人/截止时间/动作` 模式，辅助生成行动项列表：
```bash
python scripts/extract_actions.py transcript.txt --json
```
输出：识别到的 owner、deadline、action 三元组（正则启发式，作为初稿，由 agent 校正）。

## 质量门禁
- [ ] 行动项是否都有 owner（无 owner = 不会被执行）
- [ ] 是否区分了"决策"与"待决"
- [ ] 是否去掉了寒暄/重复，只留信息密度高的内容

## 自进化学习系统
```bash
python scripts/learner.py record . --capability "会议纪要" [--fail --error <类型> --note <说明>]
python scripts/learner.py insight .
python scripts/learner.py reflect .
```
- owner 识别经常漏 → 记录，reflect 建议扩充称呼/昵称词典
- 用户常用模板 → `prefer` 记录

## 安全边界
- 会议内容涉敏时，纪要仅存用户指定位置，不外传
- 不臆造 owner/时限，缺失则标"（待确认）"
