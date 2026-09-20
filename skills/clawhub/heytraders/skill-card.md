## Description:

Operate HeyTraders through the live heytraders_cli browser command catalog when the user asks to inspect, navigate, configure, or manage the HeyTraders application.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heytraders](https://clawhub.ai/user/heytraders)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to inspect, navigate, configure, and manage HeyTraders through its live browser command catalog, including backtest review, exchange onboarding, and transport recovery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Completed backtest reports may be converted into unauthenticated share links by default when performance is reported.

Mitigation: Share links should be treated as readable by anyone who has the URL, only distributed to intended recipients, and revoked with the live revoke command when continued access is no longer wanted.

Risk: Sensitive backtest results or strategy conditions may be exposed if the companion plugin or browser profile is not trusted.

Mitigation: Install the companion plugin only from a trusted source and use an isolated browser profile when testing sensitive workflows.

Risk: Exchange credentials, wallet secrets, or authorization steps could be mishandled if entered into chat or CLI arguments.

Mitigation: Keep secrets in the secure browser or venue surface identified by the live guide, and require explicit authority for orders, strategy starts, wallet approvals, credential creation, deposits, and other irreversible actions.

## Reference(s):

- [HeyTraders ClawHub skill page](https://clawhub.ai/heytraders/skills/heytraders)
- [HeyTraders OpenClaw package installation guide](https://github.com/heytraders/HeyTraders-OpenClaw/blob/main/README.md#install-in-an-existing-openclaw-environment)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline JSON and bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live heytraders_cli command discovery before issuing structured command envelopes.]

## Skill Version(s):

2.0.5 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
