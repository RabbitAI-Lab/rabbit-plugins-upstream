## Description:

CentralStationCRM helps agents read, create, update, delete, list, and search CentralStationCRM companies, people, and deals through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users, CRM operators, and developers use this skill to manage CentralStationCRM records through an OOMOL-connected account. The skill supports read, search, create, update, and delete workflows with live schema inspection before payload construction.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include direct execution of remote installer scripts.

Mitigation: Prefer installing the oo CLI through a versioned, verifiable package, or download and inspect the installer before running it.

Risk: Create, update, and delete actions can change or remove CentralStationCRM business data.

Mitigation: Require explicit user confirmation of the target record, payload, and expected effect before running write or destructive actions.

## Reference(s):

- [CentralStationCRM homepage](https://centralstationcrm.de)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown with bash and JSON command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before payload construction and returns oo CLI JSON responses when actions are run.]

## Skill Version(s):

1.0.2 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
