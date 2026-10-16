## Description:

Runs local security checks for AI agents and supports certificate-based identity, peer verification, and trust handshakes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bartelmost](https://clawhub.ai/user/bartelmost)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use AgentShield to check local agent configurations, request audit certificates, and verify peer agents before collaboration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Dry-run contacts the service and sends agent identity metadata and a signed challenge despite a no-submission claim.

Mitigation: Review network and data handling before installation; do not treat --dry-run as an offline privacy check.

Risk: Automated consent bypass or an untrusted API endpoint could expose agent information.

Mitigation: Avoid --yes for production or sensitive agents and point AGENTSHIELD_API only to a trusted endpoint.

Risk: Peer verification relies on server-backed trust rather than fully local cryptographic verification.

Mitigation: Treat verification results as service-backed signals, not independent cryptographic proof.

## Reference(s):

- [AgentShield on ClawHub](https://clawhub.ai/bartelmost/skills/agentshield-audit)
- [AgentShield documentation](https://agentshield.live/docs)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Console text and JSON certificates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Audit scores, certificate details, and peer-verification results.]

## Skill Version(s):

1.5.13 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
