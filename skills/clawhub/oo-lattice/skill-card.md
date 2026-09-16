## Description:

Lattice helps agents search and read Lattice data through an OOMOL-connected account using the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and developers use this skill to retrieve Lattice users, departments, goals, tags, and current-user information from a connected Lattice account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security summary reports that the setup path tells an agent to run an unverified remote installer when the oo CLI is missing.

Mitigation: Install the oo CLI only through a verified, pinned, or manually inspected method before using the skill.

Risk: Lattice data flows through the OOMOL connector.

Mitigation: Install only when the user trusts OOMOL and is comfortable with using its connector for the listed read-only Lattice actions.

## Reference(s):

- [ClawHub Lattice Skill](https://clawhub.ai/oomol/skills/oo-lattice)
- [Lattice Homepage](https://lattice.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with oo CLI shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands can return JSON from the oo connector when run with --json.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
