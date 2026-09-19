## Description:

Retrieves public Douyin search results, hot-ranking entries, creator posts, and video or image-post comments for content research and analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to collect structured public Douyin data for content research, competitor monitoring, trend tracking, and comment analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Douyin keywords, profile or video URLs, and GUAIKEI_API_TOKEN to guaikei.com.

Mitigation: Use it only when that external data sharing is acceptable, keep the token secret, and rotate the token if it is exposed.

Risk: The skill automatically saves collected Douyin data locally, which may include public usernames, IDs, comments, URLs, and research queries.

Mitigation: Review generated log files, delete them when no longer needed, and redact personal or sensitive research data before sharing outputs.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/why20261/skills/douyin-comments-assistant)
- [Server-Resolved Source Repository](https://github.com/why20261/douyin-comments-assistant)
- [Options Reference](references/options.md)
- [Changelog](references/changelog.md)
- [GUAIKEI API Service](https://www.guaikei.com)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [JSON from command-line tools, with human-facing guidance and optional local JSON log files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GUAIKEI_API_TOKEN and Node.js 16.14.0 or newer; command output is written to stdout while logs are written to stderr and may also be saved under logs/.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
