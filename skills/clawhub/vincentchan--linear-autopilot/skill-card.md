## Description:

Automate Linear task processing with Discord notifications and git sync.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vincentchan](https://clawhub.ai/user/vincentchan)

### License/Terms of Use:


## Use Case:

Developers and teams use this skill to connect Linear tasks to Clawdbot workflows through Discord, including task intake, status updates, user notifications, and optional git sync.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Externally triggered tasks can update Linear, send Discord messages, write files, and optionally push git changes with broad authority.

Mitigation: Use the skill only in a tightly controlled Linear team and Discord channel, and require human review before enabling autoPush or accepting generated diffs.

Risk: Linear issue fields may contain untrusted instructions that influence agent behavior.

Mitigation: Treat issue titles, descriptions, comments, and labels as untrusted data and validate intended actions before execution.

Risk: Integration setup requires API keys, bot tokens, and webhook URLs.

Mitigation: Use least-privilege and rotated tokens, and store secrets in a proper secret manager or a locked-down local file.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/vincentchan/skills/linear-autopilot)
- [Make.com Setup Guide](references/make-setup.md)
- [Pipedream Setup Guide](references/pipedream-setup.md)
- [Zapier Setup Guide](references/zapier-setup.md)
- [Linear GraphQL API](https://api.linear.app/graphql)
- [Make.com](https://make.com)
- [Pipedream](https://pipedream.com)
- [Zapier](https://zapier.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON configuration examples, and helper script usage]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose Linear API calls, Discord notification setup, local file writes, and optional git commands depending on user configuration.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
