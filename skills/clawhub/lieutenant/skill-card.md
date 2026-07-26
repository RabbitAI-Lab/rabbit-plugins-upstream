## Description: <br>
Lieutenant scans messages, agent cards, and A2A communications for prompt injection, jailbreaks, data exfiltration, and other malicious AI-agent patterns. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jd-delatorre](https://clawhub.ai/user/jd-delatorre) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and security engineers use Lieutenant to check untrusted prompts, agent cards, and agent-to-agent communications before allowing an agent to act on them. It can be used as a CLI scanner, Python API, or A2A middleware for local or API-backed verification. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Review before execution as proposals could introduce incorrect or misleading guidance into skills. <br>
Mitigation: Review and scan skill before deployment. <br>

## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/jd-delatorre/skills/lieutenant) <br>
- [TrustAgents](https://trustagents.dev) <br>
- [TrustAgents API Docs](https://trustagents.dev/docs) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Shell commands, Code, Guidance] <br>
**Output Format:** [Plain text or JSON scan results, with shell command and Python integration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Local scanning avoids remote submission; API mode sends scanned content to the configured TrustAgents service and should be used only when that is acceptable.] <br>

## Skill Version(s): <br>
1.0.0 (source: evidence.release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
