## Description:

Helps developers build Monad blockchain dapps, deploy smart contracts, configure frontends, and troubleshoot development workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to generate and review Solidity, Foundry, deployment, verification, and frontend setup guidance for Monad blockchain applications.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Deployment examples include transaction broadcasting with a private key.

Mitigation: Use testnet-only keys, avoid production private keys on command lines, and manually confirm every broadcast step before execution.

Risk: The verification example posts contract build metadata and source-related JSON to an external service.

Mitigation: Run the verification POST only after confirming the recipient service is acceptable for the contract and source metadata being shared.

Risk: Security evidence marks the release suspicious because warnings and scoping around deployment and verification are limited.

Mitigation: Review the skill before installation in environments with real wallets, proprietary contracts, or production deployment access.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/monad-development)
- [Publisher profile](https://clawhub.ai/user/thcjp)
- [Skill homepage](https://skillhub.cn/skill/)
- [Monad testnet RPC endpoint](https://testnet-rpc.monad.xyz)
- [Devnads verification API endpoint](https://agents.devnads.com/v1/verify)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline code blocks, shell commands, configuration snippets, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include deployment, verification, troubleshooting, and error-handling guidance for agent-mediated developer workflows.]

## Skill Version(s):

1.0.1 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
