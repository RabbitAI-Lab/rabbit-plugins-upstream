## Description:

Tuskr (tuskr.app). Use this skill for ANY Tuskr request - reading, creating, and updating data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent read Tuskr projects, test cases, and test runs, and to create or update Tuskr records through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create or update Tuskr data through OOMOL-connected actions.

Mitigation: Confirm the exact payload and expected effect with the user before running write actions.

Risk: The skill may require oo CLI installation, login, or account connection steps when authentication or connection errors occur.

Mitigation: Review installation, login, and connection steps with the user before proceeding.

## Reference(s):

- [Tuskr homepage](https://tuskr.app)
- [oo CLI repository](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-tuskr)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
