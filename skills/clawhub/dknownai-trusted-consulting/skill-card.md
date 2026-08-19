## Description:

深知可信咨询 answers policy, regulation, government-service, tax, social-security, subsidy, licensing, standards, compliance, and public-service questions through DKNOWC's trusted consultation API, returning cited answers with local provenance HTML and clean Markdown outputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dknownai](https://clawhub.ai/user/dknownai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, employees, and developers use this skill to obtain cited consulting answers for Chinese policy, government-service, tax, social-security, housing-fund, subsidy, licensing, industry-standard, public-service, and compliance questions. It is intended for workflows that need source-backed answers, a source list, and locally generated provenance files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Consultation questions are sent to DKNOWC's API.

Mitigation: Inform users before use and avoid submitting sensitive information unless the deployment has approved that data flow.

Risk: The skill may ask for a phone number and verification code to obtain an API key, and persistent key storage could affect future sessions.

Mitigation: Use API keys only through DKNOWC_API_KEY, never display complete keys, and persist keys only after explicit user consent.

Risk: Policy or compliance answers could be misleading if claims are not supported by returned source material.

Mitigation: Keep source markers tied to actual returned references and mark unsupported conclusions as needing further verification.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dknownai/skills/dknownai-trusted-consulting)
- [DKNOWC MaaS management platform](https://platform.dknowc.cn/)
- [DKNOWC trusted unified chat endpoint](https://open.dknowc.cn/chat/trusted/unification)

## Skill Output:

**Output Type(s):** [text, markdown, files, guidance]

**Output Format:** [Cited answer text with a source list, local provenance HTML, and clean Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires DKNOWC_API_KEY; API responses and rendered reports are written under the skill's official-docs workspace.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
