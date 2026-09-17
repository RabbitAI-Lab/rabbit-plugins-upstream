## Description:

Use Fireberry (fireberry.com) for reading, creating, updating, and deleting Fireberry data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Fireberry through an OOMOL-connected account, including reading, creating, updating, deleting, and querying account and contact records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that pipe downloaded scripts directly into a shell.

Mitigation: Use a verified, versioned installer when available, or inspect and validate the installer before running it.

Risk: The skill can perform writes and destructive deletes against Fireberry account and contact records.

Mitigation: Confirm the exact payload, target record, and intended effect with the user before running write or destructive actions.

Risk: Fireberry access is mediated through OOMOL-connected credentials.

Mitigation: Install only when OOMOL-mediated access to Fireberry records is acceptable for the deployment.

## Reference(s):

- [Fireberry skill page](https://clawhub.ai/oomol/skills/oo-fireberry)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Fireberry homepage](https://www.fireberry.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, API calls, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live Fireberry action schemas before constructing connector requests.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
