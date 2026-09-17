## Description:

GenPage (genpage.ai) enables agents to read, create, update, and delete GenPage data through the OOMOL-connected oo CLI instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage GenPage workspaces, audiences, campaigns, leads, variables, analytics, and billing-related status through authenticated oo CLI connector actions. It supports read workflows directly and requires confirmation before write or destructive GenPage changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include remote installer commands that can execute shell code from external URLs.

Mitigation: Do not let an agent run the installer pipeline automatically; install the oo CLI through a trusted, verifiable method before using the skill.

Risk: Write and destructive GenPage connector actions can change or remove campaign, audience, or lead data.

Mitigation: Confirm the target resource, exact payload, and expected effect with the user before executing any action tagged write or destructive.

Risk: Connector payloads may be malformed or stale if inferred without checking the current action contract.

Mitigation: Fetch the live connector schema for the selected GenPage action before constructing or running a JSON payload.

## Reference(s):

- [GenPage homepage](https://www.genpage.ai/)
- [oo CLI repository](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-genpage)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with oo CLI shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; read actions may be run directly, while write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.2 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
