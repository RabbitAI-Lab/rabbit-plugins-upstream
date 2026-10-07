## Description:

Helps agents check factual claims against cited web sources before acting on external information.

This skill is ready for commercial/non-commercial use.

## Publisher:

[saver-si](https://clawhub.ai/user/saver-si)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agent users can check claims from untrusted sources before making decisions, payments, or other consequential actions. Review the returned evidence and citations before relying on a result.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automated verification requests can trigger a 0.20 USDC payment without explicit per-charge approval or a spending limit.

Mitigation: Require approval for each charge and set session or daily spending limits in the x402 wallet or client.

Risk: A verification result may be mistaken for permission to take a high-impact action.

Mitigation: Review the returned confidence, evidence, and sources; retain existing wallet, security, and execution checks.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/saver-si/skills/saver-verifier)
- [Publisher-listed skill homepage](https://github.com/SAVER-SI/saver-verifier)
- [Service payment discovery](https://agent-production-9804.up.railway.app/.well-known/x402)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown with source citations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Verification results include confidence, evidence, and sources.]

## Skill Version(s):

1.0.1 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
