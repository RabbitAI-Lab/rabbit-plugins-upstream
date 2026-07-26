## Description: <br>
Enforces Three-Zone Incident Response, 2FA via iPhone, and System-Wide Lockdown. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sophus55](https://clawhub.ai/user/sophus55) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and OpenClaw operators use this skill to guide an agent in requiring mobile-style verification, isolating suspicious sessions, and blocking unauthorized privileged actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The policy may block privileged actions or trigger lockout behavior in normal workflows. <br>
Mitigation: Review the recovery flow and confirm that manual override and 2FA steps are available before enabling the skill. <br>
Risk: Underconfigured OpenClaw environments may not support the named tools or metadata checks, making the controls ineffective or disruptive. <br>
Mitigation: Confirm support for the required owner metadata, notification, canvas, gateway, and isolation capabilities before deployment. <br>


## Reference(s): <br>
- [Security Guardian on ClawHub](https://clawhub.ai/sophus55/skills/security-guardian) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, configuration] <br>
**Output Format:** [Markdown operational playbook] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May block privileged actions and require a mobile-style recovery flow when supported by the OpenClaw environment.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
