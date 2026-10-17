## Description:

Retrieves public Kuaishou videos, creator posts, and comments through GUAIKEI and organizes their engagement data for analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators, marketers, and analysts use this skill to find public Kuaishou videos by keyword, review creators' posts, and examine video comments and engagement for content research and competitor monitoring.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Kuaishou keywords, URLs, and an API token are sent to GUAIKEI's service.

Mitigation: Use only when authorized to share the inputs and token with GUAIKEI.

Risk: Returned public social-media data is saved in local logs, including when collecting comments at scale.

Mitigation: Check privacy obligations and log retention; keep collection limits proportionate to the task.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/why20261/skills/kuaishou-record-organizer)
- [GUAIKEI service and token information](https://www.guaikei.com)
- [Options and usage](references/options.md)
- [Release notes](references/changelog.md)

## Skill Output:

**Output Type(s):** [Structured data, Text]

**Output Format:** [JSON results with optional natural-language summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results are also saved in local logs; requests require a GUAIKEI API token.]

## Skill Version(s):

1.0.0 (source: server release, SKILL.md frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
