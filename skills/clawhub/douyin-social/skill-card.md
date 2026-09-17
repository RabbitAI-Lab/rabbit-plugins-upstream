## Description:

Provides command-driven lookup of public Douyin hot searches, keyword video or note results, creator public works, and comment data for social media operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT

## Use Case:

External users and content operators use this skill to collect structured public Douyin data for topic selection, competitor monitoring, trend tracking, comment review, and social media reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Douyin keywords, video or creator identifiers, and the GUAIKEI_API_TOKEN to guaikei.com.

Mitigation: Install and use it only when that data sharing is acceptable, and rotate the token if terminal history, logs, or network traces may have exposed it.

Risk: The security review notes that authentication is performed through URL query parameters.

Mitigation: Treat the token as sensitive, avoid sharing command output or logs, and prefer fresh tokens for sensitive work.

Risk: Retrieved Douyin social data is automatically saved locally and may include public usernames, comments, and interaction metadata.

Mitigation: Treat generated logs as sensitive working files; delete them when no longer needed and do not commit or redistribute them without authorization.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/why20261/skills/douyin-social)
- [Server-resolved source repository](https://github.com/why20261/douyin-social)
- [Server-resolved source commit](https://github.com/why20261/douyin-social/tree/e7841027e7ead71161a97b2096682be7f61a6373)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)
- [Guaikei API token setup](https://www.guaikei.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Command stdout is structured JSON; runtime logs and status messages are separate from result data.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata; artifact metadata reports 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
