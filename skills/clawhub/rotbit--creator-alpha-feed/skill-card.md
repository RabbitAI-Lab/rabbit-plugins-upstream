## Description:

Collect and rank daily AI content for creator-focused publishing workflows, including AI topic scouting, X/Twitter KOL tracking, tutorial picks, industry updates, and Feishu/Obsidian briefing pushes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rotbit](https://clawhub.ai/user/rotbit)

### License/Terms of Use:


## Use Case:

Content creators, editorial operators, and automation-focused agents use this skill to collect AI-related items from public sources, rank them for creator workflows, and prepare concise group updates plus full Obsidian reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Browser collection can use an active X/Twitter session and may collect from a logged-in homepage if the operator chooses that path.

Mitigation: Use public pages or a dedicated low-privilege browser profile, avoid private areas, and confirm browser collection targets before running.

Risk: Generated reports may contain incorrect rankings, stale source data, or misleading briefing text before being posted to a group channel.

Mitigation: Review the concise Feishu update and full Obsidian report before posting or scheduling automated pushes.

Risk: Misconfigured Feishu chat IDs or Obsidian paths can send summaries to the wrong place or write durable files outside the intended vault structure.

Mitigation: Confirm Feishu identifiers and Obsidian report directories in configuration before enabling routine runs.

Risk: Cleanup behavior can delete old local pipeline data.

Mitigation: Run cleanup with explicit retention settings, maintain backups for important reports, and treat cleanup as destructive unless a dry run has been reviewed.

Risk: Shell scripts fetch external content and write logs, JSON, Markdown, and task files into local pipeline directories.

Mitigation: Run the scripts as a least-privileged user in a scoped workspace and inspect generated files before using them downstream.

## Reference(s):

- [Creator Alpha Feed on ClawHub](https://clawhub.ai/rotbit/skills/creator-alpha-feed)
- [Data Collection Rules](references/data-collection-rules.md)
- [Cron Prompt Template](references/cron-prompt-template.md)
- [Push Format](references/push-format.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown reports, JSON content files, shell command snippets, and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes concise Feishu-ready summaries, full Obsidian report paths, collection logs, fallback/degradation notes, and source status checks.]

## Skill Version(s):

1.0.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
