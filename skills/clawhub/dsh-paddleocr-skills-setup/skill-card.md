## Description:

Installs, launches, configures, and verifies the Aidenwu0209/dsh-PaddleOCR-Skills native DeepSeek Harness bundle for PaddleOCR text recognition and document parsing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[aidenwu0209](https://clawhub.ai/user/aidenwu0209)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to set up the Aidenwu0209 DeepSeek Harness PaddleOCR bundle, verify the local DSH web UI, and configure OCR and layout parsing endpoints and credentials safely.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing from the referenced GitHub main branch can pull future upstream changes.

Mitigation: Confirm trust in the repository before installation and review the commands before running them.

Risk: API tokens could be exposed if entered into ordinary settings, logs, or source files.

Mitigation: Enter tokens only through the DSH Credential field and avoid echoing or storing them elsewhere.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/aidenwu0209/skills/dsh-paddleocr-skills-setup)
- [Repository homepage](https://github.com/Aidenwu0209/dsh-PaddleOCR-Skills)
- [PaddleOCR documentation](https://www.paddleocr.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash code blocks and concise setup status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports prerequisite versions, commands, local Web URL, visible configuration status, and values still required from the user.]

## Skill Version(s):

1.0.0 (source: server release metadata and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
