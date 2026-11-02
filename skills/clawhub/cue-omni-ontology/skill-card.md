## Description:

从用户指定的公开资料建立可追溯业务知识包，支持跨期变化审阅、原文查证和可选的数字出处核对；需人工核验证据，且不判定事实真伪或自动预警。

This skill is ready for commercial/non-commercial use.

## Publisher:

[huhoo](https://clawhub.ai/user/huhoo)

### License/Terms of Use:

MIT

## Use Case:

面向研究分析师、业务团队和开发者，用于跟踪公开报告、公司披露、供应商或产品变化，整理可回查证据并生成变化简报。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Numeric checks and page citations may provide less assurance than they appear to; financial-strength and causal-link assessments are heuristics.

Mitigation: Verify numbers and page references against the original documents, treat heuristic assessments as provisional, and review the offline demo before relying on results.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/huhoo/skills/cue-omni-ontology)
- [Publisher profile](https://clawhub.ai/user/huhoo)
- [cue-omni-reader setup documentation](https://github.com/sensedeal/cue-skills/blob/main/cue-omni-reader/references/setup.md)
- [Evidence verification guidance](references/verification.md)

## Skill Output:

**Output Type(s):** [Markdown, JSON, Text]

**Output Format:** [Markdown briefs, JSON knowledge packs, and evidence-grounded text answers]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs include source-linked excerpts and change summaries; numeric checks require human review against original documents.]

## Skill Version(s):

0.3.11 (source: SKILL.md frontmatter, CHANGELOG.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
