## Description:

Lightfield helps agents search and read Lightfield accounts, contacts, opportunities, custom object records, object definitions, and API key metadata through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to let an agent retrieve Lightfield records, inspect live action schemas, and handle setup, authentication, connection, and billing errors for Lightfield access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer scripts that execute directly on the user's machine.

Mitigation: Use verified, versioned vendor installation instructions and inspect installer sources before allowing an agent or shell session to run them.

Risk: The skill can retrieve Lightfield business records through connected account credentials.

Mitigation: Limit requests to the user's stated task, use the disclosed OOMOL credential flow, and avoid collecting raw API tokens.

## Reference(s):

- [ClawHUB skill page](https://clawhub.ai/oomol/skills/oo-lightfield)
- [Lightfield homepage](https://lightfield.app)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-oriented connector actions; live schemas are inspected before JSON payload construction.]

## Skill Version(s):

1.0.3 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
