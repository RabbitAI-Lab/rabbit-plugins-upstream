---
name: tech-content-review-panel
description: Reviews a tech, AI, or industry research/in-depth analysis long-form article before publishing, using a fixed eight-role expert panel in an evaluate-then-optimize loop. Applies to tech/AI/data deep-dives, sector judgment and research pieces, not news, marketing, docs, tutorials, or short opinion posts. Trigger when a user asks to review a finished deep-analysis draft or wants tech content to reach publish-ready quality.
version: 1.0.0
metadata:
  openclaw:
    tags:
      - content-review
      - editorial
      - tech-writing
      - quality-assurance
      - fact-checking
      - deep-analysis
      - thought-leadership
    requires:
      bins:
        - none
read_when:
  - review this article
  - multi-perspective critique
  - make content publish-ready
  - editorial review for deep-analysis draft
---

# Tech Content Review Panel

A single reviewer misses things. This skill runs a fixed **eight-role expert review panel** over a finished tech/AI/industry deep-analysis draft, gives blunt per-role feedback, and pushes the draft toward publish-ready quality — especially for content meant to build a professional personal brand for an industry audience.

**Design pattern: Evaluator-Optimizer.** The panel evaluates, the draft is revised, a re-check confirms no new issues, then it ships. A generate → evaluate → revise loop.

## When to use

**Applies to**: tech / AI / data industry deep-dives, sector judgment articles, and research pieces aimed at an industry readership.
**Does not apply to**: news, marketing copy, product docs, tutorials, or short opinion posts — their goals and criteria differ, and this panel would misfire. If triggered on such content, stop and tell the user the skill does not apply.

## Workflow

### Step 1 [Deterministic] Confirm input and applicability
- Confirm a finished draft exists (file path or full text). If only a topic or outline exists, stop and ask for a complete draft first.
- Confirm the content form is in scope (see above). If not, stop and explain.

### Step 2 [LLM] G1 fact and originality check (must pass first)
- **Facts**: verify every number, company name, date, policy, and event. Foundational claims must be verified against a reliable source (use web search). Mark items as confirmed / to-verify / possibly-stale (watch for stale news presented as current).
- **Originality**: search the core arguments, frameworks, and signature phrasings. Decide whether each is an independent take/deepening of a public idea (keep, add a distinguishing line if needed) or too close to an existing piece (rewrite). Every "original / first / exclusive" claim must be verified — never assert originality from impression.

### Step 3 [Deterministic] G2 style red-line scan (must be clean)
- Grep the full text for banned patterns (align to the author's writing profile):
  - "not A but B" and all paired-contrast variants
  - marketing jargon (empower, closed-loop, end-to-end, powerful, significant, substantial)
  - inflated/preachy/self-media tone
  - lecturing/advice tone (you should / it is recommended / here is what to do)
  - arguing by belittling others (most analyses / many articles / everyone assumes)
  - writing-process meta text (in one line / further questions / this piece will)
  - explicit commercial intent (keep a researcher stance, no selling)
- Then read through: no AI tone, judgment-first, written and tightened.

### Step 4 [LLM] R1-R4 target-reader representatives
- **R1 tech decision-maker**: technically-grounded exec. Flags: vague generalities, phenomena without depth, correct-but-no-new-info conclusions.
- **R2 cross-domain senior expert**: knows both the local and the subject's market. Flags: lazy simplifications, inaccurate technical detail, arrogant framing.
- **R3 investor / strategy analyst**: knows business logic, not the code. Flags: floating judgments without data, logic gaps, absolute conclusions without boundaries.
- **R4 blunt veteran**: zero tolerance for marketing/AI/self-media tone. Flags: filler, inflation, lecturing, correct-but-empty prose.

### Step 5 [LLM] G3 structure and depth
- Check against six depth moves (see references/depth-playbook.md); hit at least three: (1) puncture a taken-for-granted causal link; (2) give a layered framework that unpacks an overused concept; (3) surface a contradiction inside the subject; (4) place it in a historical lineage; (5) add a horizontal comparison; (6) name the boundary of the judgment.
- Check structure: judgment-first, no cookie-cutter sections, has a keepable comparison table or framework.

### Step 6 [LLM] T1 distribution check
- **T1 tech media editor**: knows platform distribution. Assesses title hook (hooked yet still credible), opening retention and searchability, screenshot-worthy memorable points, multi-platform fit.
- The tension with G2/R4 (hook vs restraint) is surfaced explicitly, not forced into agreement.

### Step 7 [LLM] Consolidate and revise
- Grade feedback: must-fix / suggested / optional / for-author-decision (tension items).
- Apply all must-fix and suggested; list tension items as options for the author to decide.

### Step 8 [Deterministic] Re-check
- Re-run Step 2 and Step 3 after edits (facts and red-lines must not regress; re-grep red-lines to confirm clean).

### Step 9 Finalize

## Hard Rules

> These cannot be violated.

1. **Reviewers critique hard, no self-congratulation** — finding problems beats confirming none.
2. **G1 has highest priority** — foundational facts and originality must be web-verified, not taken from existing material or impression.
3. **Red-line clearance is a hard gate** — both Step 3 and Step 8 must grep-confirm clean before finalizing.
4. **Do not force the professional-vs-distribution tension into agreement** — list options for the author. A hook must not cost credibility, but content too dry to open is also a failure.

## Failure Handling

| Scenario | Action |
|----------|--------|
| No draft (only topic/outline) | Stop, ask for a complete draft first |
| Content form out of scope (news/marketing/docs) | Stop, explain the panel only reviews deep-analysis pieces |
| Foundational fact cannot be verified | Mark as to-verify; send back for evidence or a softened claim; do not pass |
| Core argument collides with existing work | Judge independent-take vs verbatim overlap; rewrite the overlapping part |
| Revision introduces a new red-line pattern | Caught by Step 8 re-check; revise again |

## Output Format

```
[G1 fact & originality] facts: pass/reject + originality: search result (original / independent take / collision - rewrite)
[G2 style red-lines] pass/reject: specific sentence + line number
[R1] value judgment + what it flags + pass or not
[R2] [R3] [R4] same
[G3 depth] how many moves hit + what is missing
[T1 distribution] title hook + opening retention + memorable point + platform fit + tension with G2/R4
[Summary] must-fix N / suggested N / optional N / for-author-decision N
```

## Notes

Role profiles can be tuned to a project's specific readership and writing conventions (e.g. aligning to the author's long-term writing profile). Full role definitions and depth moves live in references/depth-playbook.md.

---

一份中文导读：本 skill 用固定的八角色评审团（4 位目标读者代表 + 3 位质量守门人，含事实与原创核查 + 1 位传播守门人），对科技/AI/产业深度稿做成稿后的多视角会审，逼近可发布质量。核心是"评估→修订→复审"循环，红线清零是硬门槛，专业与传播的张力交给作者拍板。
