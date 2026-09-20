## Description:

Mailchimp (mailchimp.com). Use this skill for Mailchimp requests including reading, creating, updating, and deleting data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Mailchimp through an OOMOL-connected account, including audience and member lookup, tag and merge-field inspection, and controlled member updates or deletions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may involve remote installer scripts for the oo CLI.

Mitigation: Prefer the official install guide or a verified installer, and only run setup when the oo CLI is missing.

Risk: Write and destructive Mailchimp actions can alter, archive, or permanently delete subscriber data.

Mitigation: Inspect the live action schema, confirm the exact payload and target, and require explicit approval before write or destructive actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-mailchimp)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Mailchimp](https://mailchimp.com)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The oo CLI returns JSON responses containing data and meta.executionId.]

## Skill Version(s):

1.0.4 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
