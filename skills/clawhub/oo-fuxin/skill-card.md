## Description:

Foxit Cloud API enables agents to inspect schemas and run OOMOL oo CLI commands for Foxit Cloud document conversion, creation, compression, OCR, extraction, page manipulation, file transfer, task tracking, and quota checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and teams use this skill to connect an agent to Foxit Cloud API through OOMOL for PDF and document automation, including conversion, creation, compression, OCR, extraction, protection, watermarking, file transfer, task tracking, and quota checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release security summary says the skill under-discloses document-processing actions.

Mitigation: Review the skill before installing and use it only for intentional Foxit Cloud document work.

Risk: The skill can upload documents and run state-changing or quota-consuming Foxit actions.

Mitigation: Confirm target files, payloads, and expected effects before upload, conversion, OCR, password, page manipulation, watermark, or quota-consuming actions.

Risk: The release security guidance flags unsafe remote installer commands.

Mitigation: Avoid pipe-to-shell installation unless the oo CLI installer source has been independently trusted and verified.

## Reference(s):

- [Foxit Cloud API homepage](https://cloudapi.fuxinsoft.cn)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an installed, signed-in oo CLI and a connected Foxit Cloud API account; state-changing, destructive, and quota-consuming actions require user confirmation.]

## Skill Version(s):

1.0.3 (source: evidence release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
