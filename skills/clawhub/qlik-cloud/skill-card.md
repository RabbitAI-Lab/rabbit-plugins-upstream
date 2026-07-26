## Description: <br>
Complete Qlik Cloud analytics platform integration with 37 tools for health checks, search, app management, reloads, Insight Advisor natural language queries, automations, AutoML, Qlik Answers, alerts, spaces, users, licenses, data files, and lineage. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[undsoul](https://clawhub.ai/user/undsoul) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and data teams use this skill to let an agent inspect and operate a Qlik Cloud tenant, including analytics apps, reloads, natural language data questions, automations, AutoML, alerts, users, spaces, files, and lineage. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill gives an agent broad access to business data and production-changing Qlik Cloud actions. <br>
Mitigation: Install only when agent access to the tenant is intended, use a least-privilege Qlik API key, and require human confirmation before delete, reload cancel, automation run, alert trigger, or other production-changing actions. <br>
Risk: A misplaced or exposed Qlik API key could allow unauthorized access to the tenant. <br>
Mitigation: Keep QLIK_API_KEY out of version control and shared notes, and verify QLIK_TENANT is the legitimate HTTPS Qlik Cloud tenant before running scripts. <br>


## Reference(s): <br>
- [ClawHub Qlik Cloud listing](https://clawhub.ai/undsoul/skills/qlik-cloud) <br>
- [Skill instructions](artifact/SKILL.md) <br>
- [Artifact README](artifact/README.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with bash commands and JSON command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Scripts require QLIK_TENANT and QLIK_API_KEY and return JSON success/error payloads.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
