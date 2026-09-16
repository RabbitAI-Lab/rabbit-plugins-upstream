## Description:

Enables an agent to read, create, update, and delete Sendmator contact data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage Sendmator contacts from an agent session, including listing, reading, creating, updating, and deleting contact records through the OOMOL connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that can execute changing code on the user's computer.

Mitigation: Do not let an agent run pipe-to-shell or invoke-expression installer commands automatically; inspect official installation steps before installing.

Risk: Write and destructive actions can change or permanently delete Sendmator contact data.

Mitigation: Confirm the exact payload and expected effect before write actions, and require explicit approval before delete actions.

Risk: Incorrect payloads could target the wrong contact fields or fail against the live connector contract.

Mitigation: Fetch the action schema with the oo CLI before constructing each payload.

## Reference(s):

- [Sendmator homepage](https://sendmator.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub Sendmator skill page](https://clawhub.ai/oomol/skills/oo-sendmator)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector action responses are JSON objects that include data and meta.executionId.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
