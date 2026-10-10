## Description:

KingDoc helps agents create, edit, search, convert, and manage WPS/Kingsoft documents through cloud and local workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fyniujin](https://clawhub.ai/user/fyniujin)

### License/Terms of Use:

MIT-0

## Use Case:

Individuals and teams use this skill to draft and manage WPS/Kingsoft documents, collaborate on cloud files, and perform local conversion, OCR, and compliance checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sharing production App Secrets in chat can expose cloud credentials.

Mitigation: Use a scoped test app, store secrets locally instead of pasting them into chat, and rotate secrets after setup.

Risk: Deletion, permission changes, webhooks, and memory-bridge operations may have significant consequences without enforced confirmation or webhook signatures.

Mitigation: Review and explicitly authorize high-impact operations before use; do not rely on confirmation tokens or webhook signatures until they are enforced.

## Reference(s):

- [KingDoc release on ClawHub](https://clawhub.ai/fyniujin/skills/kingdoc)
- [Kingsoft Documents developer platform](https://developer.kdocs.cn)
- [Authentication guide](references/auth.md)
- [Security guide](references/security.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Configuration instructions]

**Output Format:** [Document content, generated files, and workflow guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Cloud document actions require a WPS/Kingsoft developer app; local document creation and OCR can work without one.]

## Skill Version(s):

4.3.0 (source: frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
