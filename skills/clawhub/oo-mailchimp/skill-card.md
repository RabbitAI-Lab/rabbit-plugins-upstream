## Description:

Mailchimp helps agents operate Mailchimp through OOMOL-connected credentials for reading, creating, updating, and deleting audience and member data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agents use this skill to inspect Mailchimp connector schemas and run Mailchimp audience, list, member, tag, and merge-field actions through the oo CLI. It supports both read workflows and state-changing member management workflows when the user confirms the target and payload.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup can execute a remote installer script for the oo CLI.

Mitigation: Before installation, verify the oo CLI through a safer installation path when possible and avoid running remote installer scripts directly unless the source and contents have been reviewed.

Risk: Mailchimp subscriber and audience data is routed through OOMOL-connected credentials.

Mitigation: Confirm that routing Mailchimp data through OOMOL is acceptable for the workspace and use only the intended connected account.

Risk: Write and destructive actions can update, archive, or permanently delete Mailchimp member data.

Mitigation: Require explicit approval for updates, archives, and permanent deletes, and verify exact targets and payloads before running state-changing actions.

## Reference(s):

- [ClawHub Mailchimp Skill](https://clawhub.ai/oomol/skills/oo-mailchimp)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Mailchimp](https://mailchimp.com)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before constructing action payloads; command responses are JSON when run with --json.]

## Skill Version(s):

1.0.3 (source: release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
