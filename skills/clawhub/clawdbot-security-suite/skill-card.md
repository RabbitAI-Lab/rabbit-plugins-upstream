## Description: <br>
Advanced security validation for Clawdbot - pattern detection, command sanitization, and threat monitoring. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gtrusler](https://clawhub.ai/user/gtrusler) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and AI agent operators use this skill to validate commands, URLs, file paths, and external content before execution or processing. It is intended to help detect command injection, SSRF, path traversal, prompt injection, API key exposure, and suspicious data exfiltration patterns. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Automatic protection can fail open. <br>
Mitigation: Review and harden the validator path, shell invocation, and validation-error behavior before relying on the automatic hook as a security boundary. <br>
Risk: Sensitive commands or tool arguments may be stored in local logs. <br>
Mitigation: Disable logging or sanitize logged values when tool inputs may contain secrets, credentials, or sensitive user data. <br>
Risk: Installation from a raw main-branch archive can bypass normal package review expectations. <br>
Mitigation: Prefer the package-manager installation path and review the skill before deployment. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/gtrusler/skills/clawdbot-security-suite) <br>
- [Security Policy](SECURITY.md) <br>
- [Security Skill Reference](skills/security/SKILL.md) <br>
- [Agent Integration Guide](skills/security/CLAWDBOT-INSTRUCTIONS.md) <br>
- [Installation Guide](skills/security/INSTALL.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands, configuration snippets, and plain-text validation results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires jq according to server-parsed metadata and bash plus jq according to package metadata.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
