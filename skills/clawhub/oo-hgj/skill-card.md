## Description:

HaiGuanJia enables an agent to inspect live action schemas and operate the HaiGuanJia connector through the OOMOL oo CLI for logistics, customs, tracking, recognition, subscription, update, and deletion workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to run HaiGuanJia logistics and customs workflows through an OOMOL-connected account, including manifest submission, schedule lookup, tracking, document recognition, and subscription operations. The skill is intended for agents that need schema-guided CLI commands before executing HaiGuanJia actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer one-liners that execute mutable scripts.

Mitigation: Install only through a trusted OOMOL oo CLI distribution path, prefer verified official installation steps, and do not run remote installer one-liners blindly.

Risk: Some HaiGuanJia actions write, delete, subscribe, or may incur charges.

Mitigation: Require explicit user confirmation for chargeable, write, subscription, or destructive actions before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-hgj)
- [HaiGuanJia homepage](https://openapi.hgj.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands call the oo CLI; connector responses are JSON and include data plus meta.executionId.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
