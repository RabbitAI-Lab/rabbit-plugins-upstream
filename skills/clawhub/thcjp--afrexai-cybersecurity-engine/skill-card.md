## Description: <br>
Afrexai Cybersecurity Engine helps agents produce cybersecurity assessment, STRIDE threat modeling, OWASP Top 10 audit, vulnerability management, infrastructure hardening, incident response, authentication review, and security program guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, security engineers, and response teams use this skill to scope authorized security reviews, build threat models, audit application and infrastructure controls, prioritize vulnerabilities, and draft incident-response playbooks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide an agent to inspect code, configuration, infrastructure, and security tooling output. <br>
Mitigation: Use it only on authorized targets, define scope before execution, and review proposed commands before running them. <br>
Risk: Security command suggestions or scan interpretations can be incomplete, disruptive, or misleading if applied without review. <br>
Mitigation: Validate findings with appropriate security tools and human review before production changes or incident decisions. <br>
Risk: Production credentials or sensitive incident data could be exposed during broad security assessment workflows. <br>
Mitigation: Avoid providing production credentials unless necessary and approved; use least-privilege, temporary access where possible. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/afrexai-cybersecurity-engine) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>
- [Skill homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with security findings, checklists, tables, playbooks, configuration snippets, and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include prioritized risk ratings, remediation SLAs, incident severity levels, and command suggestions for security tooling.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
