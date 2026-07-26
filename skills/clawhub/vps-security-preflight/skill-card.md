## Description: <br>
Run and interpret a read-only OpenClaw security preflight on an authorized Linux VPS. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tinyopsstudio](https://clawhub.ai/user/tinyopsstudio) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to audit OpenClaw VPS gateway exposure, authentication, RPC health, service supervision, firewall and SSH posture, security updates, time sync, backup readiness, rollback readiness, and deployment acceptance before connecting real accounts or data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Audit output can include sensitive host posture details or raw security findings. <br>
Mitigation: Treat audit output as sensitive, redact secrets, and avoid raw deep-audit output unless the operator explicitly requests it. <br>
Risk: Suggested remediation could change firewall, authentication, package, or service state on a production VPS. <br>
Mitigation: Use the skill for read-only preflight by default and require separate explicit approval before applying any remediation. <br>
Risk: A passing preflight is not a penetration test or security certification. <br>
Mitigation: Use the results as deployment acceptance evidence alongside manual checks for backups, restore tests, provider spend limits, and rollback readiness. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/tinyopsstudio/skills/vps-security-preflight) <br>
- [OpenClaw security documentation](https://docs.openclaw.ai/gateway/security) <br>
- [TinyOps preflight repository](https://github.com/tinyopsstudio/openclaw-vps-security-preflight) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown summary with shell command examples and prioritized remediation guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports pass, warning, failure, and informational counts; raw audit output is omitted unless explicitly requested.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
