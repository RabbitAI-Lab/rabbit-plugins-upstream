## Description:

API Security Auditor guides static audits of REST and GraphQL APIs against the OWASP API Security Top 10 (2023), producing prioritized findings, proof-of-concept examples, and code fixes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heroinyan-stack](https://clawhub.ai/user/heroinyan-stack)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security reviewers use this skill to perform static API security reviews of REST and GraphQL endpoints before release, audit, or penetration testing. It helps organize findings by OWASP API Security Top 10 category and prioritize remediation guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Proof-of-concept curl commands and exploit examples could be misused against systems without authorization.

Mitigation: Use generated testing examples only for systems the user owns or is explicitly authorized to assess.

Risk: Generated code fixes and security recommendations may be incomplete or inappropriate for a specific production environment.

Mitigation: Review proposed fixes before applying them and validate changes with the application's security, testing, and deployment process.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, guidance]

**Output Format:** [Markdown reports with tables, code examples, and curl proof-of-concept commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Static-analysis guidance only; exploit examples should be used only on systems the user owns or is authorized to test.]

## Skill Version(s):

1.0.0 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
