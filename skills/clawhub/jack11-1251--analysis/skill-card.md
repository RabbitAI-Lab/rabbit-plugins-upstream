## Description: <br>
Run deep system health checks across workspace, config, skills, and integrations with prioritized findings and remediation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jack11-1251](https://clawhub.ai/user/jack11-1251) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to audit an agent workspace, configuration, skills, integrations, and operational health, then prioritize security, operational, and hygiene findings with remediation steps. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can inspect sensitive local configuration, credentials, integrations, and workspace state. <br>
Mitigation: Run it intentionally in workspaces you want audited, and review findings before sharing or persisting the results. <br>
Risk: Suggested remediation or auto-fix steps can affect credentials, services, git history, permissions, or workspace files. <br>
Mitigation: Review each proposed action before applying it, and require manual confirmation for credential rotation, history rewriting, service changes, and file cleanup. <br>
Risk: Persistent tracking or heartbeat analysis can store health summaries over time. <br>
Mitigation: Enable ongoing tracking only when persistent operational summaries are acceptable for the workspace. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown findings with severity labels, remediation actions, and optional shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Findings are grouped by severity and may include auto-fixability notes.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
