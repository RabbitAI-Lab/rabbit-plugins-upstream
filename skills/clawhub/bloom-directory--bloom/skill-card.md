## Description:

Bloom is a programmable financial harness for agents to check balances and positions, handle payments, and work with trades, wallets, and digital assets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bloom](https://clawhub.ai/user/bloom)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI agents use Bloom to read balances and positions, prepare payments, and work with trades, wallets, and supported digital-asset protocols through Bloom's file interface. The setup guidance covers Linux x86_64 and aarch64 and macOS arm64.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence flags elevated setup steps, undeclared tool scope, and broad activation wording, with only partial inspection completed.

Mitigation: Review the complete setup instructions and the skill's tool scope before installing or enabling it; treat the security assessment as incomplete.

Risk: The skill covers payments and other financial actions.

Mitigation: Require the user's passkey or a valid Sealed Approval for transactions, and never request or handle private keys, seed phrases, passwords, or passkey secrets.

## Reference(s):

- [Bloom skill page](https://clawhub.ai/bloom/skills/bloom-directory)
- [Install Bloom](artifact/references/install.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with shell commands and Bloom file or VFS paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide file-based financial actions; transactions require the user's passkey or a valid Sealed Approval.]

## Skill Version(s):

0.5.0+1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
