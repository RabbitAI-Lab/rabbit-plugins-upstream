## Description: <br>
AgentGuard monitors agent file access, API calls, and communications to detect suspicious behavior, log events, and generate actionable security reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[manas-io-ai](https://clawhub.ai/user/manas-io-ai) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and operators use AgentGuard to monitor AI agent activity, identify suspicious file or network behavior, and produce alerts and security reports for review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: AgentGuard monitors and stores sensitive agent activity, which can expose file, API, and communication metadata if configured too broadly. <br>
Mitigation: Restrict watched directories, review what is stored under ~/.agentguard, shorten retention where appropriate, and verify local file permissions for logs and alerts. <br>
Risk: Alert and report channels may send activity details outside the local console when external delivery is enabled. <br>
Mitigation: Keep alert and report channels console-only unless external delivery is explicitly required and approved. <br>
Risk: The security scan verdict is suspicious because scope and external-sharing disclosures are inconsistent. <br>
Mitigation: Install only when an agent activity monitor is intended, review configuration before running, and confirm external-sharing settings match the deployment policy. <br>


## Reference(s): <br>
- [AgentGuard ClawHub Skill Page](https://clawhub.ai/manas-io-ai/skills/agentguard) <br>
- [AgentGuard Documentation](https://docs.clawdhub.com/skills/agentguard) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Console text, Markdown reports, JSON alert and status records, and YAML configuration] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Stores local logs, alerts, baselines, and reports under ~/.agentguard.] <br>

## Skill Version(s): <br>
1.0.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
