## Description: <br>
Security layer protecting agents from prompt injection, social engineering, and malicious content on Moltbook and similar platforms. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[machinesbefree](https://clawhub.ai/user/machinesbefree) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External developers and agents use this skill to scan Moltbook or similar social content for prompt injection, malicious code requests, social engineering, suspicious URLs, and data exfiltration attempts before deciding whether to process, flag, or block the content. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Local audit logging may retain a preview of scanned text, including private or sensitive content. <br>
Mitigation: Avoid scanning secrets or private text unless local retention is acceptable, and periodically delete or disable the audit log when retention is not desired. <br>
Risk: Regex-based threat detection can produce false positives or miss novel attacks. <br>
Mitigation: Treat SUSPICIOUS and BLOCKED results as review signals, keep threat patterns current, and use human review for ambiguous cases. <br>
Risk: The scanner expects jq to be available for logging. <br>
Mitigation: Verify jq is installed before integrating the scanner into an agent workflow. <br>


## Reference(s): <br>
- [Moltbook Firewall on ClawHub](https://clawhub.ai/machinesbefree/skills/moltbook-firewall) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Plain text scan results and Markdown guidance with bash examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Scanner output classifies content as SAFE, SUSPICIOUS, or BLOCKED and may write a local audit log preview of scanned text.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
