## Description:

Aggregates AI trend content from Kuaishou, WeChat Official Accounts, Bilibili, WeChat Channels, and Xiaohongshu, clusters topics, and produces cross-platform HTML daily reports with structured intelligence leads.

This skill is ready for commercial/non-commercial use.

## Publisher:

[redfox-data](https://clawhub.ai/user/redfox-data)

### License/Terms of Use:

MIT-0

## Use Case:

External users such as AI content researchers, intelligence analysts, content operators, and marketing teams use this skill to track AI-related trends across five Chinese content platforms, compare topic momentum, and generate local daily reports with investigation prompts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Use sends platform queries to redfox.hk with a RedFox API key.

Mitigation: Install only when that data flow is acceptable, use a revocable key, and avoid placing the key in prompts, logs, code, or shared output.

Risk: Daily subscription can create a persistent LaunchAgent or crontab job and may store an API key on disk.

Mitigation: Enable subscription only when persistent local execution is intended, inspect the scheduled job configuration, and remove it when no longer needed.

Risk: Generated intelligence sections and person-background templates can affect reputational or employment-like judgments if treated as verified facts.

Mitigation: Treat generated findings as leads, require independent verification, and avoid private person-background screening without clear authorization and safeguards.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/redfox-data/skills/multi-ai-feed)
- [Platform Contracts](references/platforms.md)
- [Engine Strategy](references/engine-strategy.md)
- [Investigation Modes](references/investigation-modes.md)
- [Investigation Templates](references/investigation-templates.md)
- [Investigator Configuration](references/investigator-config.json)

## Skill Output:

**Output Type(s):** [Markdown, Files, JSON, Shell commands, Guidance]

**Output Format:** [Structured conversational Markdown, local HTML report files, and optional JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a RedFox API key; daily subscription can create a persistent scheduled job; generated investigation sections should be treated as leads requiring verification.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
