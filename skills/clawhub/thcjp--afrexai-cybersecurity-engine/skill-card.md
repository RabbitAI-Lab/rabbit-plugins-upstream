## Description: <br>
Afrexai Cybersecurity Engine helps agents produce cybersecurity assessment, STRIDE threat modeling, OWASP Top 10 audit, vulnerability management, infrastructure hardening, and incident response guidance for authorized security work. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, security engineers, and authorized operations teams use this skill to structure security reviews, threat models, vulnerability triage, hardening plans, and incident response playbooks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requests command execution and broad scanning workflow authority for security tasks. <br>
Mitigation: Use it only for authorized security work, approve targets explicitly, and review commands before execution. <br>
Risk: Security scans or response actions can affect production systems if run without clear scope and rate limits. <br>
Mitigation: Avoid production-impacting scans unless authorized, set conservative scope and timing, and monitor for operational impact. <br>
Risk: The skill text describes validation and human review behavior that may not be enforced automatically. <br>
Mitigation: Treat generated findings and remediation guidance as review-required and confirm results with approved security processes. <br>


## Reference(s): <br>
- [ClawHub skill release](https://clawhub.ai/thcjp/skills/afrexai-cybersecurity-engine) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown reports, checklists, tables, shell command suggestions, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs should be reviewed before use, especially commands, target scope, scan intensity, and security findings.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
