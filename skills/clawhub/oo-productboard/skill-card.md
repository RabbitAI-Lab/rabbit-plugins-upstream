## Description:

Productboard lets an agent search and read Productboard workspace data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve Productboard entities, notes, configurations, members, teams, and team memberships from an OOMOL-connected Productboard account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that execute downloaded scripts in a shell.

Mitigation: Use a verified, versioned installer or official package-manager method when available, and only run the setup path after reviewing and trusting OOMOL's CLI distribution source.

Risk: Productboard connector requests depend on live action schemas and may fail or behave unexpectedly if payloads are guessed.

Mitigation: Inspect the connector schema for the selected action before building each payload and keep requests limited to the documented read actions unless the skill adds explicit write guidance.

## Reference(s):

- [Productboard homepage](https://www.productboard.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-productboard)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides agents to inspect live connector schemas before constructing Productboard requests.]

## Skill Version(s):

1.0.3 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
