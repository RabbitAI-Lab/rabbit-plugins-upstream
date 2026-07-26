## Description: <br>
Memory Scan helps agents audit memory files and workspace configuration for malicious instructions, prompt injection, credential leakage, data exfiltration, guardrail bypass, behavior manipulation, and privilege-escalation indicators. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, security engineers, and agent operators use Memory Scan to review agent memory and workspace configuration before continued agent work, after importing external data, or before multi-agent collaboration. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill needs access to memory and workspace configuration files that may contain sensitive information. <br>
Mitigation: Install and run it only in workspaces where that access is acceptable, and review the files in scope before scanning. <br>
Risk: Optional remote LLM analysis may send redacted memory content to an external provider. <br>
Mitigation: Keep remote mode disabled unless external analysis is intentional, and confirm redaction and provider settings before enabling it. <br>
Risk: Quarantine and scheduled monitoring can change workspace files or recurring task configuration. <br>
Mitigation: Review and approve quarantine, restore, cron, or heartbeat changes before applying them. <br>


## Reference(s): <br>
- [Memory Scan on ClawHub](https://clawhub.ai/thcjp/skills/memory-scan) <br>
- [Skill homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and optional JSON scan reports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose local scans, optional remote LLM analysis, quarantine and restore actions, and scheduled monitoring steps.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
