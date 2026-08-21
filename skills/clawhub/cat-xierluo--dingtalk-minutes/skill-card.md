## Description:

dingtalk-minutes helps agents read DingTalk AI Minutes lists, summaries, transcripts, keywords, todos, and audio links through the official dws CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cat-xierluo](https://clawhub.ai/user/cat-xierluo)

### License/Terms of Use:

MIT

## Use Case:

Employees and developers with authorized DingTalk access use this skill to find accessible AI Minutes, retrieve meeting content, and optionally archive or mirror local Markdown outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Archived transcripts, summaries, todos, audio URLs, and optional audio files can contain sensitive business or personal meeting data.

Mitigation: Use private archive and mirror directories, avoid public repositories or unintended shared sync targets, and download audio only when needed.

Risk: The skill can read DingTalk minutes only for accounts and organizations that have authorized CLI access.

Mitigation: Install and use it only where you are authorized to access the relevant DingTalk minutes.

Risk: Setup uses the external dws installer and temporary device-login logs.

Mitigation: Verify the dws installer source before running it and remove temporary auth logs after login.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/cat-xierluo/skills/dingtalk-minutes)
- [Publisher homepage](https://github.com/cat-xierluo/legal-skills)
- [DingTalk Workspace CLI](https://github.com/DingTalk-Real-AI/dingtalk-workspace-cli)
- [AI Minutes command reference](references/01-commands.md)
- [Setup and authorization guide](references/02-setup.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance, shell commands, JSON responses, and local Markdown files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can write local archive and mirror files when the user explicitly runs the provided scripts.]

## Skill Version(s):

1.1.0 (source: server release metadata, SKILL.md frontmatter, and CHANGELOG.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
