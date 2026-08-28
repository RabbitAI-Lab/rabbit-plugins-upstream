---
slug: tech-content-review-panel
displayName: Tech Content Review Panel
name: tech-content-review-panel
description: Reviews a tech/AI/industry research or in-depth analysis long-form article before publishing, via a fixed eight-role expert panel (target-reader reps, quality gatekeepers incl. fact+originality check, distribution gatekeeper) in an evaluate-then-optimize loop. Applies to tech/AI/data deep-dives, sector judgment and research pieces — not news, marketing, docs, tutorials, or short opinion posts. Trigger when the user asks to 会审/评审/review a finished deep-analysis draft or wants tech content 接近完美/可发布.
description_zh: "技术内容评审委员会：发布前用固定八角色专家小组（目标读者代表、质量门禁含事实与原创检查、分发门禁）以先评估后优化循环，评审技术/AI/行业研究深度长文。"
version: 1.1.2
agent_created: true
not_for:
  - Fact-checking a single claim in isolation (use a claim-audit skill instead)
  - Rewriting or restructuring the article itself (review only; revision guidance is advisory)
  - News, marketing copy, documentation, tutorials, or short opinion posts
  - Reviewing content that has no finished draft yet
read_when:
  - "会审 / 评审 / review this article"
  - "多视角挑刺 / 让内容接近完美 / 可发布质量"
  - "tech/AI/行业深度稿成稿后的质量把关"
---

# Tech Content Review Panel

A tech/AI/industry deep-analysis piece aimed at an industry readership and built to establish a professional personal brand is easy to miss with a single perspective. This skill provides a fixed **eight-role expert panel** that reviews a finished draft from multiple angles, giving blunt per-role feedback to push it toward publish-ready quality.

**Design pattern: Evaluator-Optimizer** — the panel evaluates, you revise per the feedback, then re-check to confirm no new problems before finalizing. It is a generate → evaluate → revise loop.

## When to use

**Applies to**: tech / AI / industry research or in-depth analysis **long-form** articles aimed at an industry readership (industry deep-dives, sector judgments, research pieces).
**Does not apply to**: news, marketing copy, product docs, tutorials, or short opinion posts — different goals and criteria mean this panel would mismatch. When such content triggers, tell the user this skill does not apply.

## Review workflow

### Step 1 [Deterministic] Confirm input and applicability
- Confirm there is a finished deep-analysis draft (file path or full text). If none, stop and ask the user to finish a first draft first.
- Judge whether the content type applies (see above). If not, stop and explain.

### Step 2 [LLM] G1 Fact & originality check (gate first — reject if it fails)
- **Facts**: verify every number / company name / date / policy / event. Foundational facts must be verified online with traceable sources. Distinguish confirmed / to-verify / possibly-stale (watch timeliness — do not present old news as new).
- **Originality**: search (WebSearch) the core argument, framework, and signature phrasing to judge whether it is "independently derived / deepened from public views" (keep, add a clarifying line if needed) or "verbatim-similar and needs rewrite" (plagiarism risk). Every "original / first / exclusive" claim must be verified — never assert originality from memory.

### Step 3 [Deterministic] G2 Style red-line scan (reject if not cleared)
- Grep the full text for red-line phrasing (aligned with the user's long-term writing profile `negative_rules`):
  - "not A but B" and all contrast variants (is X not Y / not…but / not…is / rather than)
  - marketing jargon (empower / closed-loop / end-to-end / powerful / significant / substantial / build)
  - self-aggrandizing / inspirational-influencer tone
  - preacher / instructing tone (you should… / I suggest you… / here's what to do)
  - putting down others' arguments (most analyses… / many articles… / everyone assumes…)
  - writing-process meta-info (one-line wrap-up / follow-up question / this piece will… / conclusion first)
  - explicit commercial intent (researcher posture, no pitching)
- Then read through to confirm no AI tone, no judgment-first, no written deflection.

### Step 4 [LLM] R1–R4 Target-reader representatives
- **R1 Technical decision-maker**: decision layer with a tech background in the industry. Picks on: vague generalities, phenomenon without depth, correct conclusions with no information gain.
- **R2 Cross-domain senior expert**: understands both the local and the reader's market. Picks on: assumed simplifications, inaccurate technical details, arrogant perspective.
- **R3 Investor / strategy analyst**: understands business logic but not details. Picks on: hanging judgments without data, logic jumps, absolute conclusions without boundaries.
- **R4 Blunt veteran critic**: zero tolerance for marketing / AI / influencer tone. Picks on: empty clichés, grandstanding, preacher posture, correct-but-useless platitudes.

### Step 5 [LLM] G3 Structure & professional depth assessment
- Against the six depth moves (see `references/depth-playbook.md`), hit at least 3: ① expose assumed causality ② decompose an overused concept with a layered framework ③ find contradictions within the argued object itself ④ place it in historical context ⑤ give a horizontal reference frame ⑥ expose the boundary of the judgment.
- Check structure: judgment-first, no isomorphic template, has a collectable comparison table / framework.

### Step 6 [LLM] T1 Distribution assessment
- **T1 Tech media editor**: understands platform distribution. Rates title hook (has a hook without losing professionalism), opening retention and search-crawlability, screenshot-shareable memorable points, multi-platform fit (WeChat / LinkedIn / Substack each have their own logic).
- Surface the tension with G2 / R4 (hook vs restraint) explicitly; do not force unification.

### Step 7 [LLM] Consolidate and revise
- Grade feedback: must-fix / suggested / optional / for-author-decision (tension items).
- Handle all must-fix and suggested; list options for tension items for the author to decide.

### Step 8 [Deterministic] Re-check
- After revision, re-run Step 2 and Step 3 (facts and red-lines must not introduce new problems from the changes; re-grep red-lines to confirm cleared).

### Step 9 Finalize

## Hard Rules

> Cannot be violated.

1. **Panelists critique hard, never self-praise** — finding problems is more valuable than confirming none.
2. **G1 has highest priority** — foundational facts and originality must be verified online; do not rely on existing material or memory alone.
3. **Red-line clearance is a hard gate** — both Step 3 and Step 8 must grep the full text to confirm; cannot finalize until cleared.
4. **Professional-vs-distribution tension is not forced into agreement** — list options for the author to decide. Principle: a hook must not sacrifice professional credibility, but must not be so professional that no one clicks.

## Failure Handling

| Scenario | Handling |
|----------|----------|
| No finished draft (only topic/outline) | Stop, ask to finish first draft before review |
| Content type does not apply (news/marketing/docs etc.) | Stop, explain this skill only reviews deep research pieces |
| Foundational fact cannot be verified | Mark "to-verify", reject and ask for evidence or revised judgment; do not pass |
| Core argument collides (plagiarism risk) | Judge independent-derivation vs verbatim-similar; if similar, reject and ask to rewrite that part |
| Revision introduces new red-line phrasing | Step 8 re-check intercepts, revise again |

## Output Format

```
【G1 Fact & Originality】Facts: pass/reject + Originality: core-argument search result (original / independently derived / collision-needs-fix)
【G2 Style red-line】pass/reject: specific sentence + line number
【R1】value judgment + what it picked on + pass or not
【R2】【R3】【R4】same as above
【G3 Depth】how many moves hit + what's missing
【T1 Distribution】title hook + opening retention + memorable point + platform fit + tension with G2/R4
【Summary】must-fix N / suggested N / optional N / for-decision N
```

## Notes

Role profiles can be fine-tuned per the specific project's reader composition and writing norms (e.g., align with the user's long-term writing profile). Detailed role definitions and depth moves are in `references/depth-playbook.md`.

## 中文摘要

本 Skill 提供固定的**八角色专家评审团**，在科技/AI/产业深度长文成稿后做多视角会审，逼近可发布质量。设计模式为 Evaluator-Optimizer（评估→修订→复审）。

- **适用**：面向行业读者、建专业 IP 的科技/AI/产业研究型或深度分析型长文；不适用新闻、营销、文档、教程、短评。
- **九步流程**：①确认输入与适用性 ②G1 事实与原创核查（立论基石须联网核实，原创性须检索验证，不过关打回）③G2 风格红线 grep 扫描（不清零打回）④R1–R4 目标读者代表会审 ⑤G3 结构与纵深评估（六套路至少命中 3）⑥T1 传播评估（钩子 vs 克制张力显性列出）⑦汇总分级修订 ⑧复审重跑 G1/G2 ⑨定稿。
- **硬规则**：评审挑得狠不自我表扬；G1 优先级最高；红线清零是硬门槛（Step3/Step8 双 grep）；专业 vs 传播张力不强行统一，列选项由作者拍板。
- 角色画像可按项目读者构成与写作规范微调；详细定义见 `references/depth-playbook.md`。
