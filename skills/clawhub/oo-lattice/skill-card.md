## Description:

Lattice (lattice.com). Use this skill for ANY Lattice request -- searching and reading data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, operators, and agents use this skill to retrieve Lattice users, departments, goals, tags, and current-user details through an OOMOL-connected Lattice account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include direct execution of remote installer scripts without verification.

Mitigation: Prefer a verified or package-managed oo CLI installation instead of running the one-line remote installer directly.

Risk: Using the skill routes Lattice data through OOMOL as an intermediary.

Mitigation: Install only when the deployment is comfortable with OOMOL handling the connected Lattice data.

Risk: Lattice actions depend on live connector schemas and authenticated account state.

Mitigation: Inspect the action schema before constructing payloads and use first-time setup only after auth or connection errors.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-lattice)
- [Lattice homepage](https://lattice.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Retrieves read-only Lattice connector responses as JSON through the oo CLI.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
