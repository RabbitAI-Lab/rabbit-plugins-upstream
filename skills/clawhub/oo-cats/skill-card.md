## Description:

CATS lets an agent search and read CATS candidates, companies, jobs, and site information through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve and search CATS recruiting records through an OOMOL-connected CATS account without handling raw credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include unverified remote installer commands that can execute arbitrary code on the user's machine.

Mitigation: Install the oo CLI only from a trusted OOMOL distribution path and prefer a verified, versioned installer with checksum or signature validation.

Risk: The skill can read CATS recruiting data through the user's connected account.

Mitigation: Use it only with accounts authorized for the requested CATS data and keep actions limited to the documented read-only get, list, and search operations.

## Reference(s):

- [CATS ClawHub listing](https://clawhub.ai/oomol/skills/oo-cats)
- [CATS homepage](https://catsone.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Text, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live CATS connector schema inspection and an OOMOL-connected CATS account.]

## Skill Version(s):

1.0.2 (source: server release metadata and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
