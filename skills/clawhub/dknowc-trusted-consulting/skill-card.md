## Description:

深知可信咨询 answers policy, regulation, government-service, tax, social-security, housing-fund, subsidy, licensing, standards, compliance, and public-service questions through dknowc's trusted unified chat API, returning citation-backed consultation answers plus local trace HTML and clean Markdown.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dylanzhangzx](https://clawhub.ai/user/dylanzhangzx)

### License/Terms of Use:

MIT-0

## Use Case:

External users, employees, and agents use this skill to obtain citation-backed guidance for Chinese policy, government-service, tax, social-security, housing-fund, subsidy, licensing, industry-standard, public-service, and compliance questions. It is intended for consultation workflows where answers need source markers, a source list, and a local trace report.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Consultation questions, phone verification details, and API credential flow interact with dknowc remote services.

Mitigation: Tell users before use that their question is sent to dknowc's remote service and that phone verification may create or retrieve a reusable access key.

Risk: The security summary says privacy and account/key disclosures are incomplete or potentially misleading.

Mitigation: Use plain consent language for remote processing, phone verification, account/key creation or retrieval, and any credential persistence before proceeding.

Risk: A reusable DKNOWC_API_KEY may be exposed if handled in chat, files, or command arguments.

Mitigation: Read the credential only from a secret environment variable, mask displayed values, and persist it only after explicit user consent.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dylanzhangzx/skills/dknowc-trusted-consulting)
- [dknowc MaaS Platform](https://platform.dknowc.cn/)
- [dknowc Trusted Unified Chat API](https://open.dknowc.cn/chat/trusted/unification)
- [Consultation Introduction Reference](reference/consult_intro.md)
- [Sample Consultation Answer](reference/sample_consult_answer.md)
- [Sample Trace Report](reference/sample_trace_report.html)

## Skill Output:

**Output Type(s):** [text, markdown, HTML files, JSON files, shell commands, configuration guidance]

**Output Format:** [Markdown answer with numeric source markers, a source list, local HTML trace report, clean Markdown, and optional JSON API result files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires DKNOWC_API_KEY for full remote consultation; without it, the skill falls back to clearly marked non-verified guidance.]

## Skill Version(s):

1.0.5 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
