## Description:

Altoviz (altoviz.com). Use this skill for ANY Altoviz request — reading, creating, and updating data. Whenever a task involves Altoviz, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to work with an OOMOL-connected Altoviz account: inspect live action schemas, find or retrieve customers, list customers, and create customers after confirming write payloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Read actions may expose Altoviz customer records.

Mitigation: Install and use the skill only with an OOMOL-connected Altoviz account where the agent is allowed to access customer data.

Risk: The create_customer action changes Altoviz state.

Mitigation: Confirm the exact payload and expected effect with the user before running write actions.

Risk: Installing the oo CLI via remote installer introduces supply-chain exposure when the CLI is not already installed.

Mitigation: Review the oo CLI installer before running it, or use an already installed trusted oo CLI.

## Reference(s):

- [Altoviz homepage](https://altoviz.com/en/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Altoviz connection setup](https://console.oomol.com/app-connections?provider=altoviz)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live oo CLI schema inspection before constructing connector payloads.]

## Skill Version(s):

1.0.0 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
