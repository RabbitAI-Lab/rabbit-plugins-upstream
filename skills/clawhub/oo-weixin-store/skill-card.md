## Description:

WeChat Store (channels.weixin.qq.com) helps agents read, create, update, and delete WeChat Store data through the OOMOL connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and store operators use this skill to inspect and manage WeChat Store shops, products, orders, after-sale requests, shipping, and merchant notes through the OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional first-time setup includes remote installer commands that can execute shell or PowerShell scripts.

Mitigation: Use OOMOL's documented installer path and inspect or verify installer scripts before execution.

Risk: Write and destructive actions can change store state, including product deletion, product overwrites, shipment creation, and after-sale decisions.

Mitigation: Review the live action schema, exact target, payload, and expected effect with the user before running write or destructive commands.

Risk: The skill operates through an OOMOL-connected WeChat Store account.

Mitigation: Install and use it only when the user trusts OOMOL and has intentionally connected the relevant WeChat Store account.

## Reference(s):

- [WeChat Store homepage](https://channels.weixin.qq.com/shop)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [WeChat Store skill on ClawHub](https://clawhub.ai/oomol/skills/oo-weixin-store)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration guidance, JSON payload guidance, Operational guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing payloads; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.0 (source: release evidence and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
