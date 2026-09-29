## Description:

Helps agents find Nano (XNO) services, use a seed-based wallet without running a node, and make or accept HTTP 402 payments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pursekeeper](https://clawhub.ai/user/pursekeeper)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and developers use this skill to discover services that accept Nano, manage a wallet, pay for API calls, and sell services through Nano payment flows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can sign and broadcast irreversible payments involving real Nano funds.

Mitigation: Authorize only intended payments; check each quoted price and recipient before paying, and keep spending caps low.

Risk: Exposure of the wallet seed could give others control of the funds.

Mitigation: Keep NANO_SEED out of shared shells, logs, CI, and screenshots.

Risk: Unpinned dependencies can change before use with meaningful funds.

Mitigation: Consider pinning dependencies before using the wallet with meaningful funds.

## Reference(s):

- [pursekeeper on ClawHub](https://clawhub.ai/pursekeeper/skills/pursekeeper)
- [pursekeeper homepage](https://pursekeeper.dev)
- [No-node wallet guide](references/no-node.md)
- [NanoGPT payment guide](references/buy-from-nanogpt.md)
- [Seller directory snapshot](references/sellers.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide users through payments involving real Nano funds.]

## Skill Version(s):

0.1.11 (source: frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
