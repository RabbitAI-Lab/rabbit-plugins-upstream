## Description: <br>
Audits authorized codebases, infrastructure configurations, and agentic AI systems for security risks, compliance gaps, vulnerability findings, and remediation guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, security reviewers, and automation teams use this skill to audit authorized code, infrastructure, or agent designs and generate prioritized findings and improvement guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read, scan, execute commands, and write reports across broad audit targets. <br>
Mitigation: Use it only for targets you are authorized to audit, provide a specific target_path and audit_scope, and review proposed command execution and report-writing locations before allowing changes. <br>
Risk: Security audit output can affect remediation priorities and compliance decisions. <br>
Mitigation: Review findings before acting on them and validate high-impact recommendations against project policy and the target environment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/agentic-security-audit) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown or JSON-style structured reports with findings, scores, and remediation suggestions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include security grades, risk findings, prioritized improvements, and command or configuration review guidance.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
