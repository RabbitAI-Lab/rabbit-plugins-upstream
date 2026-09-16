## Description:

The folk skill helps agents read, create, update, and delete Folk people, companies, groups, custom fields, and workspace users through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Folk CRM data through an OOMOL-connected account, including listing, reading, creating, updating, and deleting Folk records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include shell commands that execute remote installer scripts.

Mitigation: Review the installer source before use and prefer a verified package, pinned release, checksum, or official installation method that can be inspected first.

Risk: Write and destructive Folk actions can change or remove CRM records.

Mitigation: Confirm the exact target, payload, and expected effect with the user before running write actions, and require explicit approval before destructive actions.

## Reference(s):

- [ClawHub folk skill page](https://clawhub.ai/oomol/skills/oo-folk)
- [Folk homepage](https://folk.app)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [shell commands, JSON, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill instructs agents to inspect live action schemas before constructing payloads and to confirm write or destructive actions with the user.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
