## Description: <br>
Afrexai Cybersecurity Engine Free guides agents through security posture assessment, STRIDE threat modeling, OWASP Top 10 application review, and infrastructure hardening. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, security engineers, and authorized assessors use this skill to structure repository, web application, and infrastructure security reviews. It helps produce prioritized findings, threat models, audit checklists, hardening guidance, and remediation recommendations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Security reports may expose repository paths, infrastructure details, API keys, or vulnerability findings. <br>
Mitigation: Run the skill only in trusted workspaces and redact or protect generated reports before sharing them. <br>
Risk: Assessment commands can affect systems if executed outside an approved scope. <br>
Mitigation: Use the skill only for systems you own or are authorized to assess, and review commands before execution. <br>
Risk: The optional callback_url can send sensitive scan results to an external endpoint. <br>
Mitigation: Avoid callbacks unless the endpoint is trusted, controlled, and approved for the assessment data. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/afrexai-cybersecurity-engine-free) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>
- [Skill homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with tables, checklists, prioritized findings, remediation guidance, and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include sensitive security findings and optional callback delivery details.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
