## Description:

Audits a web page's technical SEO, compares preview and production results, and suggests fixes with supporting evidence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wrpbr](https://clawhub.ai/user/wrpbr)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and site owners use PageAudit to check technical SEO, compare deployments, and obtain suggested changes. Account holders can also track pages and review domain health.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submitted URLs and related audit history are handled by a hosted service, including potentially sensitive preview or organization-managed domains.

Mitigation: Use the service only when appropriate for the URLs and audit history being shared; avoid submitting sensitive domains without authorization.

Risk: The skill includes actions that change watches, domain monitoring and alerts, event acknowledgments, or TLS reviews.

Mitigation: Get explicit user approval before enabling watches, changing monitoring or alerts, acknowledging events, or cancelling TLS reviews.

Risk: The audit reads server-delivered HTML without executing JavaScript, and partial TLS results do not establish safety.

Mitigation: Review findings against the live page and do not treat the audit as a security or accessibility certification.

## Reference(s):

- [PageAudit API reference](https://pageaudit.online/llms-full.txt)
- [PageAudit API discovery](https://pageaudit.online/api/)
- [PageAudit on ClawHub](https://clawhub.ai/wrpbr/skills/pageaudit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands]

**Output Format:** [Markdown audit findings and suggested patches or commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings include evidence and suggested fixes; reports do not certify security or accessibility.]

## Skill Version(s):

1.0.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
