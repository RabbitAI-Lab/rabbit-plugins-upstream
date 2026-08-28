## Description:

Eyes monitors global news and market-moving events, produces daily briefings with market-impact analysis, and can send scheduled alerts to configured messaging channels.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kobenfang](https://clawhub.ai/user/kobenfang)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use Eyes to monitor global political, economic, technology, and market events, then generate concise news briefings with potential industry, sector, commodity, currency, and equity-market impact analysis. The skill also supports scheduled delivery of morning, hourly, and evening alerts to user-configured messaging channels.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can send alerts to messaging channels and create recurring cron jobs.

Mitigation: Install only when scheduled news and market-impact alerts are desired, and verify the destination channel, target, and cron schedule before enabling delivery.

Risk: Broad trigger phrases and update behavior may cause more activity than a user expects.

Mitigation: Review and constrain trigger phrases and update/install actions before deployment.

Risk: The skill may reuse BigA shared routing configuration and add promotional content.

Mitigation: Configure an explicit channel and target for Eyes and review outgoing message content before relying on shared routing.

Risk: Market, stock, sector, currency, and commodity references may be mistaken for financial advice.

Mitigation: Treat all market-impact output as informational and verify investment decisions with appropriate professional or internal review.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/kobenfang/skills/eyes)
- [Event Impact Matrix](references/event-impact-matrix.md)
- [Cron Templates](references/cron-templates.json)
- [Cron Install Shell Template](references/cron-install-shell.sh)
- [User Preferences Reference](references/user-preferences.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, JSON, Guidance]

**Output Format:** [Markdown briefings and segmented message text, with JSON command results and shell commands for scheduling or sending alerts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can create recurring cron jobs and send alerts to configured channels; stock, sector, and market references should be treated as informational.]

## Skill Version(s):

5.3.13 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
