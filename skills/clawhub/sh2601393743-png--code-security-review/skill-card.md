## Description: <br>
Code Security Review helps agents inspect code repositories or pasted snippets for OWASP Top 10 issues, common security defects, exposed secrets, insecure configuration, and remediation options. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sh2601393743-png](https://clawhub.ai/user/sh2601393743-png) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering teams use this skill to review code before commits, pull requests, or releases and receive severity-ranked findings with suggested fixes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill asks an agent to read user-provided source code, which may include secrets or sensitive business logic. <br>
Mitigation: Use explicit paths or pasted snippets, avoid unnecessary sensitive repositories, and review outputs before sharing them. <br>
Risk: Security findings and remediation suggestions may be incomplete or context-dependent. <br>
Mitigation: Treat the report as developer guidance and validate material findings with project owners or a qualified security reviewer before release decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/sh2601393743-png/skills/code-security-review) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, guidance] <br>
**Output Format:** [Markdown security review report with severity tables, findings, affected locations, and remediation examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include OWASP category labels, dependency findings, secret-exposure findings, risk ratings, and prioritized remediation steps.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
