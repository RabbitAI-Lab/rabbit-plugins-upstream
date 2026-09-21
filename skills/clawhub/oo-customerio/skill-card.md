## Description:

Customer.io enables an agent to read, create, update, and delete Customer.io data through an OOMOL-connected account using the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and operators use this skill to manage Customer.io people and events from an agent session while relying on OOMOL account connections for credentials. It supports customer identification, event tracking, merge, delete, suppress, and unsuppress workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup instructions include remote installer commands for the oo CLI.

Mitigation: Install the oo CLI through a trusted, verified method before using the skill, and do not allow an agent to run the remote installer automatically.

Risk: Customer.io write and destructive actions can change, delete, merge, suppress, or unsuppress customer records.

Mitigation: Confirm the exact target, payload, and expected effect with the user before approving write or destructive actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-customerio)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Customer.io homepage](https://customer.io/)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill directs the agent to inspect live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
