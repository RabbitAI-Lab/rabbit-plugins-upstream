## Description:

Greenhouse (greenhouse.com) lets an agent read, create, and update Greenhouse data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, recruiters, and operations teams use this skill to retrieve Greenhouse candidates, applications, and jobs, list records with filters, and add candidate notes through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes an unverified internet installer.

Mitigation: Prefer a verified package or inspect the downloaded installer before running it.

Risk: The skill can access sensitive Greenhouse candidate, job, and application data.

Mitigation: Install only for trusted OOMOL-connected accounts and limit use to authorized recruiting workflows.

Risk: The add_candidate_note action changes Greenhouse state.

Mitigation: Confirm the exact payload and effect with the user before running write actions.

## Reference(s):

- [ClawHub Greenhouse Skill](https://clawhub.ai/oomol/skills/oo-greenhouse)
- [Greenhouse Homepage](https://www.greenhouse.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON objects with data and meta.executionId.]

## Skill Version(s):

1.0.2 (source: evidence release version and skill frontmatter metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
