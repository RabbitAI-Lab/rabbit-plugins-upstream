## Description: <br>
Browser automation for Kubernetes dashboards and web UIs. Use when interacting with Kubernetes Dashboard, Grafana, ArgoCD UI, or other web interfaces. Requires MCP_BROWSER_ENABLED=true. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[rohitg00](https://clawhub.ai/user/rohitg00) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and platform engineers use this skill to automate browser-based Kubernetes interfaces, including Kubernetes Dashboard, Grafana, ArgoCD, and similar web UIs. It helps agents navigate dashboards, inspect content, interact with forms, manage browser sessions, and capture screenshots. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Browser automation may send credentials or authorization headers to the wrong Kubernetes-related web UI. <br>
Mitigation: Verify target URLs before sending headers or passwords, and use short-lived least-privilege credentials. <br>
Risk: Screenshots and page dumps from dashboards may capture secrets or sensitive cluster information. <br>
Mitigation: Avoid capturing secrets in screenshots or page content, and review generated artifacts before sharing them. <br>
Risk: Agent-driven UI interactions can trigger production-changing actions such as ArgoCD synchronization. <br>
Mitigation: Require explicit approval before ArgoCD sync or any action that changes production state. <br>
Risk: Cloud browser providers may expose sensitive cluster activity outside the local environment. <br>
Mitigation: Prefer local browser execution for sensitive clusters and use cloud browser providers only when appropriate for the data involved. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline bash and Python code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires MCP_BROWSER_ENABLED=true; optional browser providers may require credentials such as BROWSERBASE_API_KEY.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
