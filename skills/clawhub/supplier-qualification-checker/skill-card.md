## Description:

Produces evidence-linked supplier due-diligence reports from Chinese bidding records, covering delivery history, business relationships, competitors, and public risk signals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement teams, project owners, and contractors use the skill to check a supplier's claimed experience and delivery capacity, or compare two prospective suppliers using bidding history and cited public information.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The service uses an API key stored in a local configuration file when an environment key is unavailable.

Mitigation: Protect the API key and local configuration file; avoid including credentials in reports or shared material.

Risk: Trial registration sends a hashed MAC address and system metadata for account deduplication.

Mitigation: Obtain user consent before registration, or use an existing API key to skip device-based registration.

Risk: Report links may contain sk sign-in-bypass parameters, and exported HTML may expose those links.

Mitigation: Treat reports and links as sensitive and limit sharing, including recharge and login URLs.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zhiliaobiaoxun/skills/supplier-qualification-checker)
- [API quick reference](references/api-quick.md)
- [Supplier review workflow](references/workflow.md)
- [Report templates](references/report-template.md)
- [Account registration and recovery](references/auto-register.md)
- [Publisher's skill documentation](https://ai.zhiliaobiaoxun.com/docs/skill)

## Skill Output:

**Output Type(s):** [Markdown, HTML, Guidance]

**Output Format:** [Cited Markdown report with an optional shareable HTML report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Single-supplier review or two-supplier comparison; includes source links and a summary of evidence limits.]

## Skill Version(s):

1.0.5 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
