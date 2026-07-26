## Description: <br>
Protect OpenClaw installations from prompt injection, data exfiltration, malicious skills, and workspace tampering. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kylejfrost](https://clawhub.ai/user/kylejfrost) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to audit OpenClaw skill directories, monitor file integrity, review outbound data-flow patterns, and harden workspace settings before or after installing skills. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The bundled shell scripts inspect local skill directories and sensitive-looking paths. <br>
Mitigation: Run check-only modes first and review reported paths before taking corrective action. <br>
Risk: Fix modes can change local workspace files or settings. <br>
Mitigation: Review planned changes before using --fix and inspect any resulting modifications. <br>
Risk: Security rule templates can alter agent operating guidance when appended to AGENTS.md. <br>
Mitigation: Manually review the template before applying it to an agent configuration. <br>
Risk: The security scanner is advisory and server guidance notes that it may skip files whose path contains the skill's own name. <br>
Mitigation: Supplement scanner results with manual review for high-risk or newly installed skills. <br>


## Reference(s): <br>
- [OpenClaw Security Hardening on ClawHub](https://clawhub.ai/kylejfrost/skills/openclaw-security-hardening) <br>
- [kylejfrost Publisher Profile](https://clawhub.ai/user/kylejfrost) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and local script output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes check-only and optional fix workflows for local OpenClaw workspace hardening.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
