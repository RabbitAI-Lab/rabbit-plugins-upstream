## Description:

MinerU enables agents to create precise document extraction tasks and batches, inspect their status, and retrieve result URLs through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate MinerU document extraction workflows from an agent without handling raw credentials directly. It supports creating extraction tasks or batches, then checking status and result URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include remote installer commands that pipe downloaded scripts directly into a shell.

Mitigation: Require explicit user approval before installation, inspect the installer first, or use an official package or pinned release when available.

Risk: Write actions can create MinerU extraction tasks or batches.

Mitigation: Confirm the exact action payload and expected effect with the user before running write actions.

## Reference(s):

- [MinerU homepage](https://mineru.net)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-mineru)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent responses may include live schema-inspection commands, connector run commands, setup recovery guidance, and extracted task or batch result data.]

## Skill Version(s):

1.0.3 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
