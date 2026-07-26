## Description: <br>
Security audit engine for OpenClaw configurations that detects vulnerabilities, misconfigurations, secret leaks, and over-privileged agents. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yun520-1](https://clawhub.ai/user/yun520-1) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to audit OpenClaw configuration files for authentication, network exposure, permissions, secret leakage, sandboxing, plugin, heartbeat, and remote configuration risks before deployment or sharing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Audit inputs and reports may contain sensitive OpenClaw configuration values. <br>
Mitigation: Treat ~/.openclaw/openclaw.json and audit output as sensitive, and avoid pasting raw output into chats or tickets. <br>
Risk: Sharing configuration files can expose tokens, private keys, or other secrets. <br>
Mitigation: Use the included sanitize command before sharing configuration material externally. <br>
Risk: The artifact advertises a remote audit option that may transmit configuration data. <br>
Mitigation: Prefer local audit unless the user understands what data will be transmitted and retained by the remote service. <br>


## Reference(s): <br>
- [ClawHub release page](https://clawhub.ai/yun520-1/ai-shield-audit) <br>
- [OpenClaw Shield homepage](https://github.com/autonomous-intelligence/openclaw-shield) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, JSON, Markdown, Shell commands, Configuration guidance] <br>
**Output Format:** [JSON audit reports and human-readable summaries with prioritized remediation guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes risk level, overall score, vulnerability counts, detailed findings, deployment recommendation, audit timestamp, and optional sanitized configuration output.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata; artifact package.json and _meta.json list 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
