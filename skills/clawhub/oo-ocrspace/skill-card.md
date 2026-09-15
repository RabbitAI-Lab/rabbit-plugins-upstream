## Description:

OCR.space lets agents extract text from public image URLs or uploaded Base64 images and retrieve OCR.space conversion statistics through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to run OCR.space OCR actions from an agent, extracting text from images and checking monthly conversion statistics through their connected OOMOL/OCR.space account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include direct execution of remote installer scripts.

Mitigation: Review the installer source and prefer a verified, versioned installation path before using the skill.

Risk: OCR actions send images or documents to an external OCR.space processing service through the connected account.

Mitigation: Only process images or documents for which external processing is acceptable.

Risk: The skill can use the connected OOMOL/OCR.space account selected by the user.

Mitigation: Connect only the OOMOL/OCR.space account intended for this agent workflow.

## Reference(s):

- [ClawHub OCR.space Skill Page](https://clawhub.ai/oomol/skills/oo-ocrspace)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [OCR.space Homepage](https://ocr.space)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return OCR text, normalized page results, conversion statistics, and connector execution metadata when actions are run.]

## Skill Version(s):

1.0.3 (source: skill frontmatter, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
