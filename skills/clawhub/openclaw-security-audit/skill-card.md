## Description: <br>
Audit OpenClaw/Clawdbot deployments for misconfigurations and attack vectors, including gateway exposure, control UI risk, skill safety, credential leakage, and hardening gaps. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[misirov](https://clawhub.ai/user/misirov) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, operators, and security reviewers use this skill to inspect OpenClaw, Clawdbot, or Moltbot environments for common misconfigurations and local security risks. It produces a read-only audit report with evidence summaries, impact, and remediation guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Review before execution as proposals could introduce incorrect or misleading guidance into skills. <br>
Mitigation: Review and scan skill before deployment. <br>

## Reference(s): <br>
- [Openclaw Security Audit on ClawHub](https://clawhub.ai/misirov/skills/openclaw-security-audit) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Terminal-style Markdown report with command output summaries and remediation steps] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only local inspection by default; reports paths and summaries while redacting secrets.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
