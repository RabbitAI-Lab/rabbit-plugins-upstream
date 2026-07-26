## Description: <br>
Provides Qlik Cloud analytics platform integration for health checks, search, app management, reloads, Insight Advisor queries, automations, AutoML, Qlik Answers, data alerts, spaces, users, licenses, data files, and lineage. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[undsoul](https://clawhub.ai/user/undsoul) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, analysts, and data platform operators use this skill to inspect and operate Qlik Cloud tenants, manage apps and reloads, and query business data through Qlik Cloud services. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can expose broad Qlik business-tenant access and state-changing actions. <br>
Mitigation: Use a scoped, least-privilege Qlik API key and require explicit user confirmation before deleting apps, starting or canceling reloads, running automations, or triggering alerts. <br>
Risk: Credentials may be exposed if the Qlik API key is stored in shared or committed files. <br>
Mitigation: Store QLIK_API_KEY outside shared files and version control, and provide it only through a protected local environment. <br>
Risk: Referenced scripts are not included in the submitted artifact, so their behavior cannot be fully reviewed from this release evidence. <br>
Mitigation: Verify the missing scripts from a trusted source before providing credentials or running commands. <br>


## Reference(s): <br>
- [Qlik Cloud Skill on ClawHub](https://clawhub.ai/undsoul/skills/qlik-cloud-skill) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, JSON] <br>
**Output Format:** [Markdown guidance with bash command examples and JSON script responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires QLIK_TENANT and QLIK_API_KEY; some Qlik Cloud features may require additional product licenses.] <br>

## Skill Version(s): <br>
0.1.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
