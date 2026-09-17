## Description:

Ragie enables agents to read, create, update, delete, and retrieve Ragie data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to operate Ragie through an OOMOL-connected account, including document ingestion, inspection, retrieval, metadata updates, partition management, and connection discovery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup can run remote installer scripts through a shell.

Mitigation: Use an already installed and authenticated oo CLI when possible; before running installer commands, independently verify the official source and understand the local changes.

Risk: Write and destructive Ragie actions can create, change, or delete documents, partitions, metadata, and limits.

Mitigation: Confirm the exact action, target, payload, and expected effect with the user before running write or destructive commands.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-ragie)
- [Ragie Homepage](https://www.ragie.ai)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Text, Shell commands, JSON, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands use the oo CLI and may return JSON responses containing data and meta.executionId.]

## Skill Version(s):

1.0.3 (source: server release evidence and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
