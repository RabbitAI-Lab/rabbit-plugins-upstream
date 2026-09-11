## Description:

Operate HeyTraders through the live heytraders_cli browser command catalog when the user asks to inspect, navigate, configure, or manage the HeyTraders application.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heytraders](https://clawhub.ai/user/heytraders)

### License/Terms of Use:

MIT-0

## Use Case:

External operators and developers use this skill to operate the HeyTraders application through its live command catalog for strategy research, backtest inspection, exchange onboarding, and workflow management.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Completed backtest reports can be created as public-by-link snapshots when performance is reported.

Mitigation: Review commercially sensitive backtest conditions before reporting performance, share generated URLs only with intended recipients, and use revoke-backtest-share to stop future access while noting saved copies cannot be recalled.

Risk: The skill depends on a separate HeyTraders plugin and managed browser access.

Mitigation: Confirm the plugin is trusted before installation and grant only the heytraders_cli and browser access needed for the requested task.

Risk: Exchange onboarding may involve venue accounts, wallets, or credentials outside HeyTraders.

Mitigation: Enter secrets only through the secure venue or browser surfaces identified by live guidance, and do not place API keys, private keys, seed phrases, tokens, or cookies in chat or heytraders_cli arguments.

## Reference(s):

- [HeyTraders ClawHub skill page](https://clawhub.ai/heytraders/skills/heytraders)
- [HeyTraders OpenClaw package installation guide](https://github.com/heytraders/HeyTraders-OpenClaw/blob/main/README.md#install-in-an-existing-openclaw-environment)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with bash and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live heytraders_cli command discovery before issuing structured tool envelopes.]

## Skill Version(s):

2.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
