## Description:

dknowc trusted consulting answers policy, regulation, government-service, tax, social-security, housing-fund, subsidy, licensing, standards, public-service, and compliance questions through the dknowc trusted unified chat API, returning cited answers and local provenance HTML.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dknownai](https://clawhub.ai/user/dknownai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to answer policy, regulation, government-service, tax, social-security, housing-fund, subsidy, licensing, standards, public-service, and compliance questions with cited source material and a local provenance report.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Consultation questions are sent to dknowc services and local trace artifacts are created.

Mitigation: Install only when this data flow is acceptable, and avoid entering unnecessary personal, confidential business, or regulated data.

Risk: The registration helper returns an API key to the running agent process for temporary use.

Mitigation: Treat the returned API key as a secret, do not display it, and persist it only after explicit user consent.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dknownai/skills/dknownai-trusted-consulting)
- [dknowc MaaS management platform](https://platform.dknowc.cn/)
- [dknowc trusted unified chat API endpoint](https://open.dknowc.cn/chat/trusted/unification)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, files, guidance]

**Output Format:** [Markdown answers with numeric citations plus local HTML provenance files and JSON/text intermediates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires DKNOWC_API_KEY and may create local trace artifacts under the skill workspace.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
