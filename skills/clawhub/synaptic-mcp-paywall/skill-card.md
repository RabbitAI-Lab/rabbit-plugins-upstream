## Description:

Generate and consume native HTTP 402 ("Payment Required") API paywalls on SynapticChain for machine-to-machine micropayments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[synaptics-lab](https://clawhub.ai/user/synaptics-lab)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to add HTTP 402 paywalls to API endpoints or consume paid APIs on SynapticChain. It provides example middleware and configuration details for automated machine-to-machine micropayments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill enables agents to automatically sign and send micropayment transactions without stated approval, budget, recipient allowlist, or payment logging controls.

Mitigation: Use only wallets or accounts intended for this automation, require explicit approval where possible, enforce strict per-transaction and daily limits, allow only trusted recipients, and keep payment logs.

Risk: The security evidence marks the release suspicious because automated paid API consumption can spend funds if configured without controls.

Mitigation: Review the skill carefully before installation and validate payment behavior in a constrained environment before using it with real funds.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/synaptics-lab/skills/synaptic-mcp-paywall)
- [SynapticChain RPC endpoint](https://nodes.synapticchain.xyz/rpc)
- [SynapticChain gateway](https://api.synapticchain.xyz)
- [Synapse 402 community](https://t.me/synapse402)

## Skill Output:

**Output Type(s):** [Markdown, Code, Configuration, Guidance]

**Output Format:** [Markdown with inline code blocks and endpoint configuration]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes example HTTP 402 middleware and payment endpoint details.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
