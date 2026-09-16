## Description:

Use this skill for Perdoo (perdoo.com) requests: reading, creating, and updating data through the OOMOL `oo` CLI connector instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operational teams use this skill to let an agent retrieve Perdoo goals, list goals, execute Perdoo GraphQL operations, and create or update progress commits through an OOMOL-connected Perdoo account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The connected Perdoo account may allow the agent to read and update Perdoo data.

Mitigation: Install only when that account access is acceptable for the intended workspace and users.

Risk: GraphQL mutations and progress updates can change Perdoo state.

Mitigation: Before any mutation or update, require the agent to show the exact operation, variables, target objects, and expected effect for user confirmation.

Risk: The first-time setup instructions include pipe-to-shell online installers.

Mitigation: Use a verified official installation method or independently verify the installer source before running it.

## Reference(s):

- [Perdoo homepage](https://www.perdoo.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL app connections for Perdoo](https://console.oomol.com/app-connections?provider=perdoo)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands return JSON responses from the OOMOL connector, including data and execution metadata when actions run successfully.]

## Skill Version(s):

1.0.3 (source: server evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
