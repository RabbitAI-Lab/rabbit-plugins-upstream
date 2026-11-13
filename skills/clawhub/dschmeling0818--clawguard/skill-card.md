## Description:

Checks public source paths for third-party skills and returns a free security verdict, with an optional paid detailed report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dschmeling0818](https://clawhub.ai/user/dschmeling0818)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use ClawGuard to assess a third-party skill before installing, running, or trusting it. The free preview provides a verdict and risk score; a detailed report is optional and paid.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The remote service receives the public source path submitted for scanning.

Mitigation: Submit public repository paths only; do not provide private paths or secrets.

Risk: A detailed scan can trigger a $0.03 USDC charge when a wallet is configured.

Mitigation: Keep payment approval enabled and explicitly approve any paid report.

Risk: A PASS verdict is advisory and does not prove a skill is safe.

Mitigation: Review the skill and its findings before installation or execution.

## Reference(s):

- [ClawGuard ClawHub release](https://clawhub.ai/dschmeling0818/skills/clawguard)
- [ClawGuard scan service](https://clawguard.duckdns.org:8082)
- [ClawGuard MCP endpoint](https://clawguard.duckdns.org:8082/mcp)

## Skill Output:

**Output Type(s):** [Text, Analysis, Guidance]

**Output Format:** [Plain-text verdict, risk score, and scan findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Free preview; detailed reports cost $0.03 USDC.]

## Skill Version(s):

1.0.5 (source: frontmatter; server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
