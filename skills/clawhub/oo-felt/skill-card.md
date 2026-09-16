## Description:

Enables agents to read, create, update, and delete Felt maps and projects through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Felt maps and projects from an agent workflow through the OOMOL-connected oo CLI. It supports profile, map, and project reads, plus confirmed create, update, move, duplicate, and delete operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote installer one-liners can execute arbitrary code on the user's machine.

Mitigation: Avoid running the installer commands unless the installer source is independently trusted and verified; review installation documentation first.

Risk: Write and destructive Felt actions can modify or delete maps and projects.

Mitigation: Inspect the live action schema and confirm the exact payload, target, and expected effect with the user before write or delete operations.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-felt)
- [Felt Homepage](https://felt.com/)
- [oo CLI Repository](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include oo connector action payloads, JSON responses, and recovery guidance for authentication, connection, CLI setup, or billing errors.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
