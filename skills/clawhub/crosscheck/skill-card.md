## Description:

Reviews drafts, delivered work, and skill files through Crosscheck's paid remote service, returning verdicts and signed receipts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[maxugc](https://clawhub.ai/user/maxugc)

### License/Terms of Use:

MIT-0

## Use Case:

People and agents preparing drafts can request a second opinion before sharing them. Developers can check delivered work against a task or review skill files before installation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Drafts, deliverables, sources, or skill files may contain confidential material sent to crosscheckapi.com.

Mitigation: Send only material approved for remote review and redact secrets before checking folders.

Risk: Running a mutable npm package with a wallet key can expose funds or cause unexpected charges.

Mitigation: Pin the package version, use a dedicated low-balance wallet, and enforce a strict spending cap.

## Reference(s):

- [Crosscheck HTTP API](references/API.md)
- [Crosscheck service documentation](https://crosscheckapi.com/llms.txt)
- [Crosscheck ClawHub release](https://clawhub.ai/maxugc/skills/crosscheck)

## Skill Output:

**Output Type(s):** [Text, Guidance, JSON]

**Output Format:** [Markdown guidance based on JSON verdicts and signed receipts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Paid checks return a verdict and a signed receipt.]

## Skill Version(s):

0.5.4 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
