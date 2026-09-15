## Description:

Feathery helps agents read, create, update, and delete Feathery account data through an OOMOL-connected CLI workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Feathery forms, schemas, submissions, users, sessions, account details, and hidden fields from an agent. It is intended for Feathery tasks where the agent should inspect each action schema before running read, write, or destructive operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup includes remote installer commands that pipe downloaded scripts directly to a shell.

Mitigation: Use a verified OOMOL CLI installation method with pinned versions or checksum/signature validation before installing.

Risk: The skill can perform write and destructive actions against Feathery account data.

Mitigation: Inspect the live action schema, review the exact payload and target, and require explicit user approval before write or delete actions.

## Reference(s):

- [ClawHub Feathery skill](https://clawhub.ai/oomol/skills/oo-feathery)
- [Feathery homepage](https://www.feathery.io/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose or run Feathery connector commands after schema inspection; write and destructive operations require user confirmation.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
