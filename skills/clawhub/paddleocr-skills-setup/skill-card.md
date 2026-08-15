## Description:

Install, configure, and verify both Agent Skills from Aidenwu0209/PaddleOCR-Skills. Use when a user wants the script-based PaddleOCR text-recognition and document-parsing skills installed in Codex, Claude Code, Cursor, OpenCode, OpenClaw, or another skills-compatible agent.

This skill is ready for commercial/non-commercial use.

## Publisher:

[aidenwu0209](https://clawhub.ai/user/aidenwu0209)

### License/Terms of Use:

MIT No Attribution

## Use Case:

Developers and agent users use this setup skill to install and verify the PaddleOCR text-recognition and document-parsing skills across skills-compatible agent environments. It also guides safe setup of prerequisites and PaddleOCR API token handling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup performs a global, user-level installation of both PaddleOCR skills.

Mitigation: Confirm the user wants the global install before running commands, then report the installed skill names and paths.

Risk: PaddleOCR API tokens or document contents may be exposed if pasted into chat, logs, source files, or command history.

Mitigation: Use the official PaddleOCR token flow, avoid printing or storing PADDLEOCR_ACCESS_TOKEN, and warn that OCR or parsing inputs may be sent to the configured PaddleOCR API endpoint.

Risk: Incomplete prerequisites or configuration can make the installed OCR skills appear ready when they are not usable yet.

Mitigation: Check Node.js/npx, Python 3.9+, and uv before installation, and report any configuration still required instead of claiming the OCR service works.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/aidenwu0209/skills/paddleocr-skills-setup)
- [PaddleOCR Skills repository](https://github.com/Aidenwu0209/PaddleOCR-Skills)
- [PaddleOCR official site](https://www.paddleocr.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash commands and concise setup status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports prerequisite versions, executed commands, installed skill names and paths, and remaining configuration needed from the user.]

## Skill Version(s):

1.0.1 (source: server release metadata and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
