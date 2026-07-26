## Description: <br>
Qlik provides a Qlik Cloud analytics integration with tools for health checks, search, app management, reloads, Insight Advisor queries, automations, AutoML, Qlik Answers, data alerts, spaces, users, licenses, data files, and lineage. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fianabates1](https://clawhub.ai/user/fianabates1) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, operators, and analysts use this skill to let an agent inspect and operate Qlik Cloud resources through documented shell tools. It supports analytics discovery, app and reload management, governance lookup, natural-language data questions, and cloud-only Qlik services when appropriate credentials are provided. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The agent receives Qlik Cloud access scoped to the configured API key, which may expose or modify business analytics assets. <br>
Mitigation: Use a least-privilege, revocable API key and install only when those permissions are acceptable for the intended workspace. <br>
Risk: Some tools can perform production-impacting actions such as deleting apps, cancelling reloads, running automations, or triggering alert evaluations. <br>
Mitigation: Require human confirmation before invoking destructive or operationally sensitive scripts. <br>
Risk: A wrong tenant value could send requests to an unintended Qlik Cloud tenant. <br>
Mitigation: Verify QLIK_TENANT is the exact HTTPS Qlik Cloud tenant before running the tools. <br>
Risk: API keys can leak through committed files or command history if handled casually. <br>
Mitigation: Keep QLIK_API_KEY out of committed files and shell history, and rotate it if exposure is suspected. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/fianabates1/skills/qlik) <br>
- [Artifact README](artifact/README.md) <br>
- [Artifact Skill Instructions](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON responses from helper scripts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires QLIK_TENANT and QLIK_API_KEY for live Qlik Cloud API calls.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
