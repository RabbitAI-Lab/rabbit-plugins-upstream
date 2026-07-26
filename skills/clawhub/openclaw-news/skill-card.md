## Description: <br>
Aggregates and delivers curated briefings about releases, skills, security items, community discussions, and ecosystem news in the OpenClaw ecosystem. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[arc-claw-bot](https://clawhub.ai/user/arc-claw-bot) <br>

### License/Terms of Use: <br>


## Use Case: <br>
OpenClaw users and agents use this skill to collect public ecosystem updates and format them into concise scheduled or on-demand briefings. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill makes public news and registry lookups through GitHub, ClawHub, and search providers. <br>
Mitigation: Install and run it only when those public lookups are acceptable for the workspace and account configuration. <br>
Risk: Recurring cron briefings can cause repeated external lookups and recurring notifications. <br>
Mitigation: Add the cron entries only when scheduled briefings are desired; otherwise run the skill explicitly on demand. <br>
Risk: Briefings depend on public sources and search results that may be incomplete, stale, or noisy. <br>
Mitigation: Review generated briefings before taking action on time-sensitive release, security, or community information. <br>
Risk: The skill stores limited local state for last-run timestamps, raw collected data, and pending searches. <br>
Mitigation: Review or clear the state directory when resetting collection history or before sharing the skill workspace. <br>


## Reference(s): <br>
- [OpenClaw News Skill Page](https://clawhub.ai/arc-claw-bot/skills/openclaw-news) <br>
- [ClawHub Registry](https://www.clawhub.ai) <br>
- [OpenClaw Releases](https://github.com/openclaw/openclaw/releases) <br>
- [OpenClaw Pull Requests](https://github.com/openclaw/openclaw/pulls) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, JSON] <br>
**Output Format:** [Markdown briefing with supporting JSON state and search-query JSON] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Briefings can be generated on demand or scheduled with cron; local state tracks the last run and pending searches.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and artifact documentation) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
