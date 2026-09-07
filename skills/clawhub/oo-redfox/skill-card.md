## Description:

RedFoxHub (redfox.hk). Use this skill for searching and reading data from RedFoxHub through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search, list, and fetch RedFoxHub content across supported social platforms through the oo CLI. It is aimed at read-oriented research and content retrieval workflows using an OOMOL-connected RedFoxHub account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup directs users to execute remote installer scripts directly in a shell.

Mitigation: Review the installer path before installing; prefer a pinned, verifiable oo CLI release or inspect the downloaded installer before running it.

Risk: RedFoxHub access depends on credentials brokered through OOMOL for read and search actions.

Mitigation: Connect RedFoxHub credentials only when the user is comfortable with OOMOL brokering access for the intended actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-redfox)
- [RedFoxHub homepage](https://redfox.hk)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-oriented connector actions should fetch the live schema before constructing payloads.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
