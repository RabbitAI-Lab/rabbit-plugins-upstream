## Description:

SuperSaaS helps an agent read SuperSaaS schedules, appointments, resources, groups, forms, fields, and recent booking changes through the OOMOL-connected SuperSaaS connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents with an OOMOL-connected SuperSaaS account use this skill to inspect live connector schemas and read SuperSaaS schedules, appointments, slots, resources, groups, SuperForms, available fields, and recent booking changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup flow includes unverified remote installer scripts for the oo CLI, which could alter the local environment if executed automatically.

Mitigation: Have a human install oo from a trusted, versioned source with checksum or signature verification where available, and do not let an agent run the installer proactively.

## Reference(s):

- [ClawHub SuperSaaS skill page](https://clawhub.ai/oomol/skills/oo-super-saas)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [SuperSaaS homepage](https://www.supersaas.com/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Normal connector responses are JSON objects containing data and metadata, including an execution id.]

## Skill Version(s):

1.0.3 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
