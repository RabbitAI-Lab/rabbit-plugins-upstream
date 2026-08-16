## Description:

Install and configure two PaddleOCR Agent Skills for text recognition and structured document parsing in Codex, Claude Code, GitHub Copilot, Cursor, OpenCode, OpenClaw, and other compatible agents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[aidenwu0209](https://clawhub.ai/user/aidenwu0209)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this setup skill to install and verify PaddleOCR skills for OCR and structured document parsing from screenshots, photos, scans, PDFs, tables, formulas, and layout-rich documents.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup flow installs PaddleOCR-related skills globally for the user.

Mitigation: Confirm the user trusts the referenced repository and wants a global user-level installation, then verify the installed skill names and paths after running the command.

Risk: PaddleOCR access tokens or endpoint details could be exposed in chat, command history, source files, or logs.

Mitigation: Ask for endpoint details only when needed by the target skill, and do not invent, print, paste, or store PaddleOCR tokens.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/aidenwu0209/skills/paddleocr-skills-setup)
- [Publisher profile](https://clawhub.ai/user/aidenwu0209)
- [Project homepage](https://github.com/Aidenwu0209/PaddleOCR-Skills)
- [PaddleOCR official site](https://www.paddleocr.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash commands and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports prerequisite versions, executed commands, installed skill names and paths, and any remaining configuration needed from the user.]

## Skill Version(s):

1.0.2 (source: server release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
