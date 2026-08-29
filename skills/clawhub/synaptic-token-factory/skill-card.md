## Description:

Deploy, mint, and trade autonomous SRC-20 tokens on SynapticChain Layer-1 in a single command.

This skill is ready for commercial/non-commercial use.

## Publisher:

[synaptics-lab](https://clawhub.ai/user/synaptics-lab)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external OpenClaw users use this skill to direct agents through SRC-20 token creation, deployment, minting, and token-operation commands on SynapticChain.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can lead an agent toward live token deployment, minting, or trading actions with financial, legal, or fee consequences.

Mitigation: Require explicit user confirmation before any transaction, and confirm wallet, fee, legal, and financial-risk handling before proceeding.

Risk: The skill does not provide enough built-in warning or confirmation guidance for live blockchain execution.

Mitigation: Prefer a testnet or dry run first, and review generated commands before allowing an agent to execute them.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/synaptics-lab/skills/synaptic-token-factory)
- [SynapticChain RPC Endpoint](https://nodes.synapticchain.xyz/rpc)
- [SynapticChain Explorer](https://explorer.synapticchain.xyz)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include token deployment, minting, transfer, approval, balance, and trading instructions for SynapticChain.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
