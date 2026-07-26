## Description: <br>
Security audit engine for OpenClaw configurations that detects vulnerabilities, misconfigurations, secret leaks, and over-privileged agents during security, hardening, config review, or audit workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[LaurentAIA](https://clawhub.ai/user/LaurentAIA) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and operators use this skill to audit OpenClaw configuration files for authentication, network exposure, channel, subagent, tool permission, secret leakage, sandbox, plugin, heartbeat, and remote configuration risks. It supports local CLI audits, JSON reports, human-readable summaries, and config sanitization before sharing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: OpenClaw configuration files may contain API keys, tokens, and remote access details. <br>
Mitigation: Run audits locally where possible and sanitize configs or outputs before sharing them. <br>
Risk: Remote or premium audit flows may send sensitive configuration data outside the local environment. <br>
Mitigation: Use remote audit features only after reviewing clear data-handling terms for that flow. <br>
Risk: Security findings and remediation suggestions may affect access controls or deployment behavior. <br>
Mitigation: Review prioritized findings before applying changes to production OpenClaw configurations. <br>


## Reference(s): <br>
- [ClawHub release page](https://clawhub.ai/LaurentAIA/ai-shield-audit) <br>
- [Project homepage](https://github.com/autonomous-intelligence/openclaw-shield) <br>
- [Autonomous Intelligence](https://autonomousintelligence.ai) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [JSON security reports, human-readable summaries, Markdown guidance, JavaScript API examples, and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports include risk_level, overall_score, vulnerabilities, vulnerability_count, compliance, recommended action, deployment safety, timestamp, and engine version.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
