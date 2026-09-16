## Description:

GageList lets agents operate a connected GageList account through OOMOL's oo CLI to read, create, update, and delete gage, calibration, manufacturer, account, and usage records.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate GageList accounts from an agent workflow after the OOMOL oo CLI is installed and the GageList connection is configured. It supports read workflows for gage, calibration, manufacturer, account, and usage information, plus user-confirmed manufacturer create, update, and delete actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that execute shell scripts when the oo CLI is missing.

Mitigation: Install the oo CLI only through a verified, user-initiated process before allowing the agent to run connector actions.

Risk: Manufacturer create, update, and delete actions can change or remove GageList account data.

Mitigation: Confirm the exact payload, target record, and expected effect with the user before write actions, and require explicit approval before destructive actions.

Risk: Connector actions depend on live schemas and server-managed credentials.

Mitigation: Fetch the action schema before constructing each payload and avoid exposing or requesting raw credentials.

## Reference(s):

- [GageList homepage](https://gagelist.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-gagelist)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, API Calls, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON command payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses OOMOL server-managed credentials through the oo CLI; action responses are JSON.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
