## Description:

Supermemory lets agents read, create, update, delete, and search Supermemory data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agent users use this skill to manage Supermemory memories, documents, profile context, search results, and processing status from an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that could execute changing network code on the user's machine.

Mitigation: Install the OOMOL oo CLI manually from a trusted source, verify the installer or package before use, and do not let an agent run pasted remote installer commands automatically.

Risk: Write and destructive Supermemory actions can change or delete user data.

Mitigation: Require explicit user confirmation of the target, payload, and expected effect before running write or destructive actions.

Risk: Connector action schemas can change over time.

Mitigation: Inspect the live action schema before constructing each connector payload.

## Reference(s):

- [ClawHub Skill: Supermemory](https://clawhub.ai/oomol/skills/oo-supermemory)
- [Supermemory homepage](https://supermemory.ai)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Text or Markdown, often with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.2 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
