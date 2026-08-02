## Description: <br>
Afrexai Cybersecurity Engine Free helps authorized users perform security posture assessment, STRIDE threat modeling, OWASP Top 10 application review, and infrastructure hardening guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, security engineers, and authorized teams use this skill to review codebases, architecture descriptions, applications, and infrastructure configurations, then produce risk-prioritized findings and remediation guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may inspect security-relevant project files and generate local audit command suggestions. <br>
Mitigation: Use it only on systems you own or are authorized to test, and review commands before execution. <br>
Risk: Security review outputs can be incomplete or incorrect because automated scans and agent analysis have limited coverage. <br>
Mitigation: Treat reports as review aids and validate findings manually before making security or compliance decisions. <br>
Risk: Repository data, API keys, or other sensitive information could be exposed during assessment workflows. <br>
Mitigation: Avoid sharing secrets with untrusted external services and keep credentials out of prompts, logs, and generated reports. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/afrexai-cybersecurity-engine-free) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown reports, checklists, risk tables, remediation guidance, and optional shell command suggestions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may depend on the agent's access to local files and user-approved command execution.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release evidence and artifact frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
