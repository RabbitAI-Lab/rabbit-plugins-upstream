## Description:

Provides agent access to GitHub Gist through the OOMOL oo CLI for reading, creating, updating, deleting, forking, starring, commenting on, and listing gists.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate GitHub Gist through an OOMOL-connected account, including retrieving gist data and carrying out user-approved write or destructive gist operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path includes a remote installer fallback for the OOMOL oo CLI.

Mitigation: Install or review the OOMOL oo CLI through a trusted path before using this skill.

Risk: The fork_gist action changes GitHub Gist state but is not labeled as a write action in the artifact.

Mitigation: Treat fork_gist as a write action and require explicit user confirmation before running it.

Risk: Write and destructive actions can create, update, star, unstar, or delete GitHub Gist content.

Mitigation: Confirm the target gist, payload, and expected effect with the user before executing write or destructive commands.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-gist)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [GitHub Gist](https://gist.github.com)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with bash commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live action-schema inspection before constructing connector payloads.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
