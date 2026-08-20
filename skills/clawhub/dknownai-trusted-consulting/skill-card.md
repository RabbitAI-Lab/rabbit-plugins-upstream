## Description:

深知可信咨询 answers policy, regulation, government-service, tax, social-security, housing-fund, enterprise-subsidy, licensing, industry-standard, compliance, and public-service questions through DKnownAI's trusted unified chat API, returning cited answers plus local provenance HTML and clean Markdown outputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dknownai](https://clawhub.ai/user/dknownai)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, and developers use this skill to obtain source-cited consultation answers for Chinese policy, government-service, tax, social-security, housing-fund, enterprise-subsidy, licensing, industry-standard, compliance, and public-service questions. It is intended for workflows that need cited answers, a clickable local provenance report, and a citation-stripped Markdown copy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Policy and compliance questions are sent to dknowc's API.

Mitigation: Use the skill only when that external service is intended for the task, and avoid submitting unnecessary sensitive details.

Risk: The skill may create local HTML and Markdown citation reports.

Mitigation: Review generated reports before sharing them and remove local outputs when they are no longer needed.

Risk: Phone, SMS-code, and API-key details are only appropriate when the user intends to use the DKnownAI service.

Mitigation: Provide those details only for intentional service setup, keep DKNOWC_API_KEY in the environment, and persist it only when future reuse is desired.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dknownai/skills/dknownai-trusted-consulting)
- [DKnownAI Publisher Profile](https://clawhub.ai/user/dknownai)
- [MaaS Management Platform](https://platform.dknowc.cn/)
- [Trusted Unified Chat API Endpoint](https://open.dknowc.cn/chat/trusted/unification)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, API Calls, Shell commands, Guidance]

**Output Format:** [Cited consultation answer, local HTML provenance report, clean Markdown file, and setup or execution guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires DKNOWC_API_KEY from the environment; writes consultation JSON and answer files under official-docs/search-results/ and HTML/Markdown deliverables under official-docs/output/.]

## Skill Version(s):

1.0.4 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
