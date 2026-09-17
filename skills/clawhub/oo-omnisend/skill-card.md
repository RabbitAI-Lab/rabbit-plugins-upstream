## Description:

Omnisend helps agents read, create, update, and delete Omnisend data through the OOMOL oo CLI instead of direct API calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage Omnisend contacts, segments, and contact tags from an agent session through OOMOL-connected account credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup flow includes remote installer commands that pipe downloaded scripts directly into a shell.

Mitigation: Use an official, versioned, signed, or checksum-verified oo CLI installation method before enabling the skill.

Risk: Write and destructive actions can change Omnisend contacts or remove contact tags.

Mitigation: Confirm the exact action, target records, payload, and expected effect with the user before running any write or destructive command.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-omnisend)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Omnisend Homepage](https://www.omnisend.com)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Actions executed with --json return JSON data and execution metadata from the oo connector.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
