## Description: <br>
Clawdbot Security Check teaches Clawdbot to audit its own configuration across 13 security domains and recommend security hardening steps. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thesethrose](https://clawhub.ai/user/thesethrose) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External Clawdbot users and developers use this skill to inspect local Clawdbot configuration, identify security misconfigurations, and receive prioritized remediation guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security scan flagged the release as suspicious because it claims read-only audit behavior while documenting a fix mode that changes bot policies, logging behavior, and file permissions. <br>
Mitigation: Use the skill for reviewed audit guidance by default, and run any fix mode only after backing up affected configuration and intentionally approving persistent changes. <br>
Risk: The skill may inspect local Clawdbot configuration and surface sensitive configuration values during audit output. <br>
Mitigation: Review audit output before sharing it, redact secrets or tokens, and run the skill only in environments where local configuration inspection is acceptable. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/thesethrose/skills/clawdbot-security-check) <br>
- [ClawdBot Gateway Security Documentation](https://docs.clawd.bot/gateway/security) <br>
- [Artifact Homepage](https://github.com/TheSethRose/Clawdbot-Security-Check) <br>
- [Original Framework Reference](https://x.com/DanielMiessler/status/2015865548714975475) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown security audit report with shell commands and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes prioritized findings, remediation steps, and optional commands for deeper audit workflows.] <br>

## Skill Version(s): <br>
2.2.2 (source: server release metadata and artifact/skill.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
