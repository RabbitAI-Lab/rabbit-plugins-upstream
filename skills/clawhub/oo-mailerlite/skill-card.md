## Description:

Use this skill to read, create, update, and delete MailerLite data through an OOMOL-connected account instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and operators use this skill to manage MailerLite subscribers, groups, fields, and group membership through the oo CLI. The skill supports read, write, and destructive account actions with live schema inspection before payload construction.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes internet-downloaded installer scripts for the oo CLI.

Mitigation: Review the installer source and prefer a signed, reviewed, or package-manager installation path before installing.

Risk: The skill can perform MailerLite write and destructive actions such as updating subscribers, deleting groups, and removing subscribers from groups.

Mitigation: Inspect the live connector schema and require explicit user confirmation of the exact target, payload, and expected effect before running write or destructive actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-mailerlite)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [MailerLite Homepage](https://www.mailerlite.com)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the oo CLI to inspect MailerLite connector schemas and run account actions; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
