## Description:

深知可信咨询 answers policy, regulation, government-service, tax, social-security, subsidy, licensing, compliance, and public-service questions through dknowc's trusted consultation API, returning cited answers, source lists, local HTML verification reports, and clean Markdown.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dknownai](https://clawhub.ai/user/dknownai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, employees, and agents use this skill when they need source-backed consultation on Chinese policy, public-service, tax, social-security, enterprise-subsidy, licensing, compliance, or related government-service questions. It helps produce cited answers and verification artifacts for review rather than unsupported policy guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Consultation questions and relevant context are sent to dknowc's remote service.

Mitigation: Use the skill only when that external processing is acceptable, and avoid sending private secrets or unnecessary sensitive personal or business data.

Risk: The artifact includes privacy and security assurances that the server security summary flags as misleading.

Mitigation: Treat the release as higher risk until the publisher corrects those claims and reviewers confirm the data-handling language.

Risk: The skill can create, retrieve, and optionally persist an API key during onboarding.

Mitigation: Require explicit user consent for key creation or persistence, never expose full keys, and keep keys in approved secret or environment-variable storage.

Risk: Generated report delivery depends on copied output paths.

Mitigation: Check delivered report paths before relying on or sharing generated HTML and Markdown files.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dknownai/skills/dknownai-trusted-consulting)
- [Publisher profile](https://clawhub.ai/user/dknownai)
- [dknowc MaaS platform](https://platform.dknowc.cn/)
- [dknowc trusted unified chat API](https://open.dknowc.cn/chat/trusted/unification)
- [Consultation introduction reference](artifact/reference/consult_intro.md)
- [Sample cited consultation answer](artifact/reference/sample_consult_answer.md)
- [Sample verification report](artifact/reference/sample_trace_report.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Cited consultation text with a source list, plus generated HTML verification reports and clean Markdown files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires DKNOWC_API_KEY from the environment for full remote consultation; may guide onboarding when the key is absent.]

## Skill Version(s):

1.1.0 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
