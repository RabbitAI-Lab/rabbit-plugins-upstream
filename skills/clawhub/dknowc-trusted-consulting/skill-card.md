## Description:

深知可信咨询 helps agents answer Chinese policy, government-service, tax, social-security, subsidy, licensing, standards, compliance, and public-service questions through dknowc credibleChat, returning cited answers and local provenance HTML.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dylanzhangzx](https://clawhub.ai/user/dylanzhangzx)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, and developers use this skill to obtain cited consultation answers for Chinese policy, regulation, government-service, tax, social-security, housing-fund, subsidy, licensing, standards, compliance, and public-service questions. It is also used to create a local HTML provenance report for each supported consultation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Consultation questions and setup phone/SMS details may be sent to dknowc services.

Mitigation: Avoid submitting highly sensitive information unless external processing by dknowc is acceptable for the use case.

Risk: Generated consultation reports and intermediate files may remain under the skill directory.

Mitigation: Request no HTML or files when local persistence is not desired, and review or remove generated artifacts according to workspace retention needs.

Risk: The skill uses DKNOWC_API_KEY for API access.

Mitigation: Provide the key through the environment, do not expose the full key in conversation or files, and persist it only when future reuse is intended.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dylanzhangzx/skills/dknowc-trusted-consulting)
- [dknowc MaaS platform](https://platform.dknowc.cn/)
- [dknowc trusted unified chat endpoint](https://open.dknowc.cn/chat/trusted/unification)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Shell commands, Configuration guidance]

**Output Format:** [Markdown answers with citation markers plus generated HTML provenance files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires DKNOWC_API_KEY and may write consultation JSON, answer text, and HTML provenance artifacts under the skill workspace.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
