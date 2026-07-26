## Description: <br>
MoltGuard protects agents and users from prompt injection, data exfiltration, and malicious commands hidden in files and web content. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thomaslwang](https://clawhub.ai/user/thomaslwang) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to install and operate MoltGuard as a guardrail for prompt injection, data exfiltration, and risky command detection in OpenClaw workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill installs and operates a persistent external security plugin that handles telemetry and local credentials. <br>
Mitigation: Install only after confirming trust in OpenGuardrails/MoltGuard and understanding what data Core receives in the target workspace. <br>
Risk: Status and claim commands can expose API-key material. <br>
Mitigation: Redact keys before sharing command output and require explicit user approval before running account-linking commands. <br>
Risk: Enterprise enrollment changes which Core service receives security detections. <br>
Mitigation: Verify the enterprise Core URL before enrollment and require explicit user approval before enroll or unenroll operations. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thomaslwang/skills/flaw0) <br>
- [MoltGuard homepage](https://github.com/openguardrails/openguardrails/tree/main/moltguard) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [None] <br>

## Skill Version(s): <br>
6.8.20 (source: server release metadata and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
