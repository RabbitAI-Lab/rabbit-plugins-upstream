## Description:

用 Cue 跑「法律合规」场景的深度研究：快速检索国内法律法规与行政令原文，梳理立法背景与合规要点，覆盖企业合规风险体检、监管问询答复案例库、疑难法律实操案例库、国内法规调研、法律实务问题研判、监管处罚雷达、诉讼文书起草等核心搭子，并产出带法条与类案依据、可逐条回查的合规体检与法律实务底稿。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wangxiaoxu](https://clawhub.ai/user/wangxiaoxu)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external legal and compliance practitioners, and developers can use this skill to run Cue-backed public legal and compliance research for disclosure, regulatory, diligence, case-law, enforcement, and drafting workflows. Outputs should be treated as sourced research drafts that require professional legal review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can clone or update the Cue runner under ~/.cue before executing research.

Mitigation: Review the runner source and confirm the local installation or update path before running setup commands.

Risk: Legal research subjects or questions are sent to Cue and may consume Cue credits.

Mitigation: Obtain explicit user confirmation before each credit-consuming run and avoid sending confidential information unless the user has approved that disclosure.

Risk: Generated legal and compliance reports may be incomplete or unsuitable as final advice.

Mitigation: Treat outputs as sourced drafts, preserve source links, and require professional legal review before relying on them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wangxiaoxu/skills/cue-legal-research)
- [Cue playbook API](https://cuecue.cn/api/playbook)
- [Cue skills runner repository](https://github.com/sensedeal/cue-skills)
- [Cue skills runner Gitee mirror](https://gitee.com/sensedeal/cue-skills)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with sourced legal and compliance research plus inline shell commands for runner setup and execution]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Cue account API key, user confirmation before credit-consuming runs, and preservation of source links in returned reports.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
