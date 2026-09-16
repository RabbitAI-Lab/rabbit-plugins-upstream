## Description:

Y.GY lets an agent read, create, update, and delete Y.GY short-link data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage Y.GY short links from an OOMOL-connected account, including listing links, retrieving a link, creating links, updating mutable settings, and deleting links after confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup instructions include remote installer commands that execute code from OOMOL-hosted URLs.

Mitigation: Review the installer source before running it, and prefer pinned versions with verified checksums or signatures when available.

Risk: Write and destructive Y.GY actions can change or delete short links.

Mitigation: Confirm the exact payload and target with the user before create, update, or delete actions.

## Reference(s):

- [Y.GY homepage](https://app.y.gy)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-y-gy)
- [Publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before building action payloads and requires confirmation before write or destructive actions.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
