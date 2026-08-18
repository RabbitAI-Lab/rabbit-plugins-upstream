## Description:

This skill lets an agent operate esa.io through the OOMOL oo CLI to read, create, update, and delete esa content.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external collaborators, and developers use this skill to work with esa teams, posts, comments, categories, tags, activity, attachments, and search through an authenticated OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create, update, delete, archive, ship, duplicate, and roll back esa content available to the connected account.

Mitigation: Confirm write payloads and effects with the user before execution, and require explicit approval before destructive actions.

Risk: The connected account may expose team posts, comments, members, attachments, activity, and other esa data beyond the immediate task.

Mitigation: Limit each request to the necessary team, post, comment, attachment, category, tag, or search query and verify targets before running commands.

Risk: Installing or signing in to the oo CLI from an untrusted source could put account access at risk.

Mitigation: Use OOMOL-provided CLI installation and sign-in sources, and avoid handling raw esa credentials directly.

## Reference(s):

- [esa homepage](https://esa.io)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-esa)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and shell commands with JSON payloads and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands use the OOMOL oo CLI and should be scoped to the requested esa team, post, comment, or search task.]

## Skill Version(s):

1.0.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
