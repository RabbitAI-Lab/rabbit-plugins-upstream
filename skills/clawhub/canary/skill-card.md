## Description: <br>
Canary scans an OpenClaw environment for leaked secrets, including API keys, tokens, credentials in .env files, installed skills, and shell history; it can run silently on startup, perform deep scans on demand, and offer fixes with user permission. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sukiraman](https://clawhub.ai/user/sukiraman) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and OpenClaw users use Canary to audit local environments for exposed credentials, understand findings in plain language, and apply confirmed fixes or guided remediation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill is a broad local credential-audit helper and may inspect sensitive credential files and paths. <br>
Mitigation: Install and run it only for environments you are authorized to audit, and review or narrow scan paths before deep scans. <br>
Risk: Credential findings and command output can expose secrets if copied into chat or logs. <br>
Mitigation: Do not paste raw secrets or full sensitive command output; share only masked or minimal output needed to understand the finding. <br>
Risk: Fixes can modify local files, and Canary state, backups, or integrity markers may persist after use. <br>
Mitigation: Approve fixes one by one, review backup and state locations, and remove Canary-created state when it is no longer needed. <br>


## Reference(s): <br>
- [Canary ClawHub page](https://clawhub.ai/sukiraman/skills/canary) <br>
- [README.md](README.md) <br>
- [Claude Project setup guide](claude-project/project-instructions.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and plain-language text with optional shell command blocks and configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose local file permission changes, credential cleanup steps, scan configuration, and remediation guidance; fixes should require user confirmation.] <br>

## Skill Version(s): <br>
1.0.0 (source: SKILL.md frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
