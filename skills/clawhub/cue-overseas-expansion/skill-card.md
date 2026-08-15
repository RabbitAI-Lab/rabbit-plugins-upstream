## Description:

用 Cue 跑「出海企业线索」场景的深度研究：锁定指定区域内有 ODI 备案、实际出海动作的跨境企业，按开户、结算、发债、并购等需求精准匹配商机，覆盖跨境制裁与海外执法筛查、跨境法规调研、出海企业资质尽调底稿、出海企业跨境业务线索、目的地国营商准入扫描等核心场景，产出可回查、可派单的出海商机清单与合规底稿。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wangxiaoxu](https://clawhub.ai/user/wangxiaoxu)

### License/Terms of Use:

MIT-0

## Use Case:

Business development, compliance, diligence, and cross-border operations teams use this skill to run Cue public-data research for overseas expansion lead discovery, sanctions and enforcement screening, regulatory research, qualification diligence, and market-entry checks. The expected result is a source-linked research report or lead list that can be reviewed and assigned for follow-up.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can clone or update an external Cue runner before executing research.

Mitigation: Review the Cue runner source and repository provenance before installation or execution in controlled environments.

Risk: The workflow can use local Cue account credentials, make network requests, and spend Cue credits.

Mitigation: Confirm account context and credit spend with the user before running research, and avoid executing it without explicit approval.

Risk: Research outputs are based on public data and may not be sufficient for legal, diligence, underwriting, or compliance decisions.

Mitigation: Preserve source links, review the report before use, and route high-impact decisions to qualified reviewers.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wangxiaoxu/skills/cue-overseas-expansion)
- [Cue playbook API](https://cuecue.cn/api/playbook)
- [Cue skills repository](https://github.com/sensedeal/cue-skills)
- [Cue skills mirror](https://gitee.com/sensedeal/cue-skills)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown report with source links and inline shell commands when setup or execution guidance is needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live Cue templates, requires user confirmation before spending credits, and should preserve source links in returned reports.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
