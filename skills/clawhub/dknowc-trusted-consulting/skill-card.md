## Description:

深知可信咨询 helps agents answer China policy, regulation, government-service, tax, social-security, subsidy, licensing, standards, public-service, compliance, and business-policy questions by calling DKnowC's credibleChat service and returning source-cited answers with a local verification report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dylanzhangzx](https://clawhub.ai/user/dylanzhangzx)

### License/Terms of Use:

MIT-0

## Use Case:

External users, employees, and agents use this skill when they need source-backed Chinese policy or public-service guidance with citation markers, a cited source list, and generated verification artifacts. It is suited for questions about procedures, eligibility, materials, timelines, subsidies, tax and social-security rules, licensing, standards, and compliance obligations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Questions and pasted materials may be sent to DKnowC's remote service despite user-facing language that says conversations or materials will not be uploaded.

Mitigation: Review the provider and privacy terms before installation, correct the data-flow language, and avoid submitting confidential HR, tax, legal, or business documents until that review is complete.

Risk: The SMS/key bootstrap can return an access key for the agent to handle during the current task.

Mitigation: Use the bootstrap only when comfortable with agent-handled credentials, keep the key out of user-visible output, and persist it only after explicit user consent.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dylanzhangzx/skills/dknowc-trusted-consulting)
- [Publisher profile](https://clawhub.ai/user/dylanzhangzx)
- [Consult introduction](reference/consult_intro.md)
- [Sample consult answer](reference/sample_consult_answer.md)
- [Sample trace report](reference/sample_trace_report.html)
- [DKnowC platform](https://platform.dknowc.cn/)
- [DKnowC API host](https://open.dknowc.cn/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Source-cited Markdown answer, HTML verification report, clean Markdown file, JSON intermediate result, and shell commands for initialization, API calls, key bootstrap, and delivery.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires DKNOWC_API_KEY from the environment for full trusted consultation; without it, the skill falls back to non-verified guidance.]

## Skill Version(s):

1.1.0 (source: release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
