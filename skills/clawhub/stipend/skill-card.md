## Description:

A non-custodial USDC wallet on Base that lets an AI agent receive payments, pay HTTP 402 / x402 charges automatically, and report earned, spent, and refused funds under configured spending limits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[graphiker-australia](https://clawhub.ai/user/graphiker-australia)

### License/Terms of Use:

MIT-0

## Use Case:

External agents and developers use stipend to create and operate a non-custodial Base USDC wallet, receive payments, make small payouts, and automatically pay HTTP 402 / x402 charges. It is intended for real payment workflows where spending limits, destination controls, and reporting are part of the agent's operating posture.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill recommends remote-code installation paths for wallet software.

Mitigation: Verify the installer and package independently before running them, and prefer controlled installation paths where the code can be reviewed first.

Risk: The skill creates persistent wallet keys and handles real USDC on Base.

Mitigation: Keep balances small, protect the passphrase outside agent-readable storage, and back up key material according to the operator's custody policy.

Risk: The skill can spend small amounts without a human and may process payment instructions from untrusted sources.

Mitigation: Use tight per-payment and daily limits, configure destination allowlists, require confirmation for new destinations, dry-run new payments, and lock configuration with a human-held secret.

## Reference(s):

- [stipend homepage](https://stipend.sh)
- [ClawHub skill page](https://clawhub.ai/graphiker-australia/skills/stipend)
- [ClawHub publisher profile](https://clawhub.ai/user/graphiker-australia)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, Python snippets, and JSON command-output examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance can direct the agent to install wallet software, create local key material, configure limits, and run payment or reporting commands.]

## Skill Version(s):

1.0.1 (source: server release metadata); artifact frontmatter reports 0.46.1

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
