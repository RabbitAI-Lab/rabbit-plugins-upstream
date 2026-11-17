## Description:

This skill guides agents in managing OKX spot, swap, futures, options, and event-contract orders, including conditional orders and position settings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[okx-retail](https://clawhub.ai/user/okx-retail)

### License/Terms of Use:

MIT-0

## Use Case:

External traders use this skill to review and manage OKX orders across spot, derivatives, options, and event contracts through the OKX CLI. It requires configured API credentials and calls for confirmation before trade-affecting actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan marked the release suspicious; its review was partial, so the security evidence is incomplete.

Mitigation: Review the skill and its scope carefully before installation, and verify the commands it recommends.

Risk: Trading commands can place or change live orders and positions using real funds.

Mitigation: Confirm live or demo mode and the instrument, side, size, and order settings before each write; use demo mode for practice.

Risk: The skill requires API credentials.

Mitigation: Do not share credentials in chat; configure them through the OKX CLI and grant only the access needed.

## Reference(s):

- [OKX](https://www.okx.com)
- [OKX CEX Trade on ClawHub](https://clawhub.ai/okx-retail/skills/okx-cex-trade)
- [Spot command reference](artifact/references/spot-commands.md)
- [Swap command reference](artifact/references/swap-commands.md)
- [Futures command reference](artifact/references/futures-commands.md)
- [Options command reference](artifact/references/options-commands.md)
- [Event contract command reference](artifact/references/event-commands.md)
- [Trading workflows](artifact/references/workflows.md)
- [Event contract workflows](artifact/references/event-workflows.md)
- [Command examples and templates](artifact/references/templates.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Text]

**Output Format:** [Markdown with shell command examples and trading status summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires configured OKX API credentials; results depend on the selected live or demo profile.]

## Skill Version(s):

1.5.1 (source: frontmatter, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
