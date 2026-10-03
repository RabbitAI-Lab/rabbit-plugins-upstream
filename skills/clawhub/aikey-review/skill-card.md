## Description:

Reviews talking-head scripts before publication for audience retention, information density, factual support, and content red flags; diagnoses issues without rewriting by default.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

Independent creators use this skill to assess finished spoken-video scripts before publishing, with sentence-level scoring, audience-reaction predictions, red-line checks, and suggested fixes where needed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may persist user feedback or recurring review issues in local vault and memory files, including details from confidential drafts.

Mitigation: Review and control vault writeback and 08-技能记忆/aikey-review/ memory behavior before using confidential scripts.

Risk: Review results may depend on AI KEY or vault rule files that the skill reads locally.

Mitigation: Check which rule files are available and appropriate; keep confidential materials out of any files shared beyond the intended review environment.

## Reference(s):

- [Review rules](references/规则卡.md)
- [Scoring anchors](references/评分锚点.md)
- [Audience-reaction predictions](references/反应预测.md)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown review report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Chinese-language, diagnosis-first report with sentence scores, red-line findings, and alternative edits for flagged text.]

## Skill Version(s):

0.4.6 (source: server-resolved ClawHub release; supplied SKILL.md says 0.6.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
