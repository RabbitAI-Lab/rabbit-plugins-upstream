## Description: <br>
Audit OpenClaw configuration for security risks and generate a remediation report using the user's configured LLM. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[muhammad-waleed381](https://clawhub.ai/user/muhammad-waleed381) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and OpenClaw operators use this skill to audit local OpenClaw configuration for security risks and receive a prioritized remediation report. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The audit inspects local OpenClaw configuration contents. <br>
Mitigation: Install and run it only where local configuration review is intended, and rely on the documented secret-stripping behavior before sharing reports. <br>
Risk: Generated remediation guidance may affect security-sensitive configuration. <br>
Mitigation: Review findings and proposed changes before applying them, then re-run the audit to confirm the intended hardening outcome. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/muhammad-waleed381/skills/openclaw-security-auditor) <br>
- [README](README.md) <br>
- [Usage Guide](docs/USAGE.md) <br>
- [Security Checks](docs/SECURITY-CHECKS.md) <br>
- [Installation Guide](docs/INSTALLATION.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, configuration] <br>
**Output Format:** [Markdown report with risk scores, severity buckets, findings, remediation steps, and example configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Analyzes local configuration metadata and is documented to strip secrets before reporting.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
