## Description:

ima (ima.qq.com). Use this skill for ANY ima request - reading, creating, and updating data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate a connected Tencent ima account through the OOMOL oo CLI for reading, searching, creating, appending, importing, and uploading ima notes and knowledge-base content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installer commands pipe remote scripts into a shell.

Mitigation: Do not run those installer commands unless the installer source has been independently verified.

Risk: Write-capable actions can create, append, import, upload, or otherwise change ima data, and append_note is not clearly protected by confirmation.

Mitigation: Require explicit user confirmation of the exact payload and expected effect before running any state-changing action, including append_note.

Risk: The skill operates through a connected ima account scope controlled by the publisher integration.

Mitigation: Install and use it only when the OOMOL publisher and the connected ima account scope are trusted.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-ima)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ima homepage](https://ima.qq.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Directs the agent to inspect live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.4 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
