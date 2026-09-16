## Description:

Enables agents to inspect schemas and run Simla.com customer and order actions through the OOMOL simla connector using the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to read, create, and update Simla.com customers and orders through an OOMOL-connected account while checking connector schemas and confirming write payloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup may encourage direct execution of remote installer scripts without integrity checks.

Mitigation: Install the oo CLI from a verified official release channel and check available checksums or signatures before running installer code.

Risk: Write actions can create or edit Simla.com customer and order records.

Mitigation: Inspect the live connector schema, review the exact JSON payload, and get user confirmation before running write actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-simla)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Simla.com homepage](https://www.simla.com/en)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before constructing payloads; write actions require user confirmation.]

## Skill Version(s):

1.0.3 (source: artifact frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
