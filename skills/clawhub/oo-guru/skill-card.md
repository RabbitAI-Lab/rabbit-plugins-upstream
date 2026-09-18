## Description:

Guru (getguru.com). Use this skill for Guru requests that search and read data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and external users use this skill to search, list, and read Guru knowledge resources available to their connected Guru account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions can run remote installer scripts.

Mitigation: Review and trust the OOMOL installer source before running install commands, or use safer install and verification options.

Risk: Connector payloads may not match the current Guru action contract.

Mitigation: Inspect the live action schema before constructing payloads.

## Reference(s):

- [Guru homepage](https://www.getguru.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Configuration guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector actions are read-only in the artifact and require live schema inspection before execution.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
