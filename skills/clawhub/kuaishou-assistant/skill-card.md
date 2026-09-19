## Description:

快手数据助手 helps agents search Kuaishou videos by keyword, retrieve public creator posts, and collect public video comments for short-video research and analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT

## Use Case:

External users, marketers, content teams, and analysts use this skill to collect public Kuaishou video, creator, and comment data for trend research, competitive monitoring, KOL review, and follow-on reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries, Kuaishou links, and related metadata are sent to the GuaiKei third-party API.

Mitigation: Install only when third-party API use is acceptable, and use the skill only for public Kuaishou data.

Risk: Generated logs may retain comments, profile URLs, keywords, or video metadata on disk.

Mitigation: Review or delete generated logs when saved Kuaishou research data should not remain locally.

Risk: The skill requires GUAIKEI_API_TOKEN, which is a secret used to access the data API.

Mitigation: Store GUAIKEI_API_TOKEN securely and avoid exposing it in prompts, logs, screenshots, or shared shell history.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/why20261/skills/kuaishou-assistant)
- [Server-resolved source repository](https://github.com/why20261/kuaishou-assistant)
- [GuaiKei API website](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON command results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Command results may be saved locally under logs/ and depend on a configured GUAIKEI_API_TOKEN.]

## Skill Version(s):

0.1.0 (source: server release metadata; artifact frontmatter and package.json report 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
