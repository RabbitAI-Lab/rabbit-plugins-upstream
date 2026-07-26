## Description: <br>
Scans OpenClaw security posture for port exposure, authentication settings, plugin and skill-source trust, credential handling, and channel configuration, then produces remediation guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[clawhub-master](https://clawhub.ai/user/clawhub-master) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to audit OpenClaw gateway, plugin, skill-source, channel, and credential settings, then generate a security report with prioritized remediation steps. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can inspect sensitive OpenClaw configuration, local skill files, and credential-related locations. <br>
Mitigation: Use it only for intentional OpenClaw security audits and treat generated findings as sensitive operational security information. <br>
Risk: The generated report may reveal security posture or configuration weaknesses. <br>
Mitigation: Store the report in a protected workspace location and redact sensitive details before sharing it. <br>
Risk: Automatic gateway configuration fixes can affect access or service behavior. <br>
Mitigation: Approve fixes only after understanding the proposed gateway change and confirming a recovery plan. <br>
Risk: Broad trigger phrases could initiate the audit when the user did not intend a full security review. <br>
Mitigation: Review trigger phrases before installation and invoke the skill only when a security audit is intended. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/clawhub-master/skills/shield-guard) <br>
- [Publisher profile](https://clawhub.ai/user/clawhub-master) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown security report with inline PowerShell commands and configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces a single security report; proposed automatic fixes require user approval.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release and artifact frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
