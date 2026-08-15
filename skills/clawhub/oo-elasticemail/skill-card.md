## Description:

Elastic Email (elasticemail.com). Use this skill for ANY Elastic Email request - reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate an Elastic Email account through OOMOL's oo CLI, including reading contacts and lists, managing contact list membership, and creating, updating, or deleting contacts and lists with confirmation for state-changing actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can change or delete Elastic Email contacts and lists.

Mitigation: Confirm the exact payload, target, and expected effect with the user before running write or destructive actions.

Risk: Using the skill grants the agent operational access to Elastic Email data through OOMOL.

Mitigation: Install and connect it only when the user intends to operate that account through OOMOL and trusts the account connection path.

Risk: Incorrect payloads could update the wrong contacts or lists.

Mitigation: Fetch the live connector schema before constructing payloads and review payloads before execution.

## Reference(s):

- [Elastic Email homepage](https://elasticemail.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-elasticemail)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill instructs the agent to inspect the live connector schema before building payloads and to request confirmation before write or destructive Elastic Email actions.]

## Skill Version(s):

1.0.0 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
