## Description:

Krexa helps users research and test trading ideas, paper-trade strategies, and request or manage live trading agents with user-approved deployments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[krexa](https://clawhub.ai/user/krexa)

### License/Terms of Use:

MIT-0

## Use Case:

Traders and their assistants use the skill to turn trading ideas or media into strategies, review research and backtests, paper-trade, and request or monitor live agents on Krexa.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An exposed Krexa key can reveal trading workflow data and authorize immediate pauses of live agents.

Mitigation: Store KREXA_AGENT_KEY in an environment variable or secret store, not shared chat or plain-text config; revoke it if exposed.

Risk: Pausing the wrong live agent takes effect immediately.

Mitigation: Confirm the exact agent and the user's intent before requesting a pause.

Risk: A deploy request can lead to live trading after wallet approval.

Mitigation: Request deployment only with the user's explicit instruction and limits; leave wallet approval to the user.

## Reference(s):

- [Krexa on ClawHub](https://clawhub.ai/krexa/skills/krexa)
- [Krexa homepage](https://krexa.xyz)
- [Connection setup](artifact/references/setup.md)
- [Krexa tools](artifact/references/tools.md)
- [Trading limits](artifact/references/limits.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with results, links, and optional setup commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports backtest assumptions and losses; deploy requests require user approval before trading.]

## Skill Version(s):

1.3.1 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
