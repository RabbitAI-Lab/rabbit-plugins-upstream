## Description: <br>
Audit helps agents review code, contracts, and assets for security, compliance, vulnerability, and risk concerns, with Chinese-language interaction support. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, security reviewers, and automation teams use this skill to ask an agent for security audit, compliance review, vulnerability scanning, and risk-assessment guidance for technical projects. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requests broad read, write, and command-execution authority without enough scoping or enforceable safety controls. <br>
Mitigation: Use it in a controlled workspace, avoid sensitive or production repositories unless command restrictions are added, and require explicit approval for changes or deployments. <br>
Risk: Security audit guidance may be incomplete or unsuitable for complex decisions that require human judgment. <br>
Mitigation: Treat results as review assistance, validate findings with trusted security tools, and require qualified human review before acting on high-impact recommendations. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/audit) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown, text, or JSON responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose file changes or command execution through the host agent; review outputs before applying them.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
