## Description:

AI-ready skill to format and publish Markdown articles to WeChat Official Accounts using Wenyan CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kyriswu](https://clawhub.ai/user/kyriswu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content teams use this skill to prepare and publish Markdown articles to WeChat Official Accounts with frontmatter metadata, theme selection, code highlighting, and image handling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can publish prepared content and referenced local or remote images to WeChat.

Mitigation: Review article text, metadata, and images before running the publish command.

Risk: The publishing flow requires WECHAT_APP_ID and WECHAT_APP_SECRET credentials.

Mitigation: Keep credentials out of prompts, files, logs, and shell history where possible.

Risk: The workflow depends on an external Wenyan CLI installation.

Mitigation: Use a reviewed and pinned Wenyan CLI version in an isolated project or container.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kyriswu/skills/publish-to-wechat)
- [Publisher profile](https://clawhub.ai/user/kyriswu)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and YAML frontmatter examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires WeChat credentials in environment variables and a Wenyan CLI installation.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
