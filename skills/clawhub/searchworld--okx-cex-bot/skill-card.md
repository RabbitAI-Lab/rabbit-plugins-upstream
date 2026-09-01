## Description:

Helps an agent manage OKX Grid and DCA Martingale bots, including creation, stopping, amendment, P&L monitoring, TP/SL, margin or investment adjustment, and AI-recommended parameters.

This skill is ready for commercial/non-commercial use.

## Publisher:

[searchworld](https://clawhub.ai/user/searchworld)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to guide an agent through authenticated OKX CLI workflows for native server-side Grid and DCA bot management. It is intended for bot-specific operations, not regular orders, market data, or portfolio account queries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide actions that affect real funds through OKX Grid and DCA bots.

Mitigation: Use demo mode first, limit API permissions to the minimum needed, and review every create, amend, stop, leverage, margin, and live-mode action before approval.

Risk: Native OKX bots can continue running on OKX servers after local CLI interaction ends.

Mitigation: Confirm trading mode, verify writes by listing or checking bot details afterward, and explicitly stop bots when the desired strategy should end.

Risk: Credential exposure would give inappropriate access to an OKX account.

Mitigation: Never collect credentials in chat; guide users through the configured OKX authentication flow and verify credential status with CLI checks.

## Reference(s):

- [OKX homepage](https://www.okx.com)
- [ClawHub skill page](https://clawhub.ai/searchworld/skills/okx-cex-bot)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown guidance with OKX CLI command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include JSON-returning OKX CLI commands; authenticated write actions require user confirmation.]

## Skill Version(s):

1.4.5 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
