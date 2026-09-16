## Description:

HaiGuanJia helps agents operate the HaiGuanJia open API through an OOMOL-connected account for reading, creating, updating, and deleting logistics and customs data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations teams use this skill to let an agent inspect HaiGuanJia action schemas and run authorized HaiGuanJia logistics, customs, tracking, manifest, and document-recognition workflows through the oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that should not be trusted blindly.

Mitigation: Review the installer source and integrity independently before running installer commands.

Risk: The skill can run write, destructive, and billed HaiGuanJia actions.

Mitigation: Confirm the exact action, payload, business effect, and expected charges before write or delete operations.

Risk: Actions operate through the connected OOMOL and HaiGuanJia account.

Mitigation: Use only an account the user intends the agent to operate and limit requests to data the user is authorized to access.

## Reference(s):

- [HaiGuanJia homepage](https://openapi.hgj.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-hgj)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON payloads or results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the oo CLI to inspect live action schemas before constructing request payloads.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
