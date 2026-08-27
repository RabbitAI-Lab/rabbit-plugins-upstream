## Description:

BigA provides A-share stock analysis, quant stock selection, real-time quotes, timing scores, buy/sell signals, stock-pool management, and scheduled message pushes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kobenfang](https://clawhub.ai/user/kobenfang)

### License/Terms of Use:

MIT-0

## Use Case:

External users interested in A-share market analysis use BigA to monitor stock pools, screen candidates, and receive concise stock-analysis messages combining market data, technical timing, fundamentals, and catalysts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad trigger phrases may start stock-analysis workflows or send messages when the user did not intend to run BigA.

Mitigation: Review and narrow the trigger set before installation, and avoid installing it in channels where accidental stock-analysis prompts are likely.

Risk: Scheduled jobs can create recurring OpenClaw runs and push messages to configured channels.

Mitigation: Install only after confirming the cron schedule, channel, target, and timeout settings, and periodically review active OpenClaw cron jobs.

Risk: Stock-analysis outputs can be mistaken for financial advice.

Mitigation: Keep the skill's risk disclaimer visible and review market-data, catalyst, and scoring assumptions before acting on any signal.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/kobenfang/skills/biga)
- [BigA Technical Timing Score Framework](artifact/references/technical-timing-score.md)
- [BigA User Preferences](artifact/references/user-preferences.md)
- [BigA Sector Matrix](artifact/references/sector-matrix.md)
- [BigA Cron Templates](artifact/references/cron-templates.json)
- [BigA Cron Installation Shell](artifact/references/cron-install-shell.sh)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown-formatted stock analysis messages, segmented text, JSON scan data, and OpenClaw cron or message commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May schedule recurring market-analysis jobs and send messages to a configured channel.]

## Skill Version(s):

6.0.19 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
