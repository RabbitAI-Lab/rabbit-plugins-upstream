## Description:

Use this skill to operate Mailchimp through an OOMOL-connected account for reading, creating, updating, and deleting Mailchimp data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage Mailchimp audiences, members, tags, and merge fields via the OOMOL Mailchimp connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup guidance uses remote installer commands for the oo CLI.

Mitigation: Review the setup instructions before installation and prefer a verified or package-manager installation path when available.

Risk: Write and destructive Mailchimp actions can change or permanently delete audience data.

Mitigation: Confirm the exact payload, target audience or member, and expected effect with the user before running write or destructive actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-mailchimp)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Mailchimp homepage](https://mailchimp.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: server release metadata and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
