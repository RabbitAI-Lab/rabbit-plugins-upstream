## Description:

Supermemory connector for reading, creating, updating, and deleting data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Supermemory through a connected OOMOL account, including recall search, profile or document retrieval, document ingestion, memory creation, updates, and deletion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can add memories, update memories, and permanently delete documents through the connected Supermemory account.

Mitigation: Review each write or delete payload and require explicit user confirmation before approving state-changing actions.

Risk: Incorrect document, memory, or tenant identifiers can affect real Supermemory data.

Mitigation: Inspect the action schema before each call and confirm target identifiers before execution.

## Reference(s):

- [ClawHub Supermemory skill page](https://clawhub.ai/oomol/skills/oo-supermemory)
- [Supermemory homepage](https://supermemory.ai)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live action schema inspection before constructing payloads; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.0 (source: release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
