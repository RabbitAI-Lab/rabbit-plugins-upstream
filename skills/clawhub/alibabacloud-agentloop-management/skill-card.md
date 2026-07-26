## Description: <br>
Guides developers and operations engineers through AgentLoop APM and AI observability onboarding with Alibaba Cloud CLI commands, configuration snippets, and safety checks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sdk-team](https://clawhub.ai/user/sdk-team) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operations engineers use this skill to onboard server-side applications, Kubernetes workloads, and AI frameworks into AgentLoop application monitoring. It helps collect required parameters, run Alibaba Cloud CLI checks, initialize APM resources, register services, and generate deployment-specific observability configuration. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Automatic installer commands and cloud CLI upgrades may change the local environment. <br>
Mitigation: Review installer and upgrade commands before execution, prefer official manual installation paths when possible, and do not run curl-to-bash commands automatically. <br>
Risk: Alibaba Cloud and Kubernetes permissions can allow service creation, deletion, addon installation, and workload patching. <br>
Mitigation: Use a least-privilege RAM profile, limit cluster permissions to the target resources, and require explicit two-phase approval before Kubernetes or application mutations. <br>
Risk: AgentLoop LicenseKey/authToken and kubeconfig output are sensitive credentials. <br>
Mitigation: Treat these values as secrets, avoid logging them, and redact them from generated output and shared transcripts. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/sdk-team/skills/alibabacloud-agentloop-management) <br>
- [Application Monitoring Module](artifact/references/apm.md) <br>
- [AI Observability Module](artifact/references/ai.md) <br>
- [RAM Policy Reference](artifact/references/ram-policies.md) <br>
- [Alibaba Cloud CLI Installation](https://help.aliyun.com/document_detail/121541.html) <br>
- [Alibaba Cloud CLI Update Guide](https://help.aliyun.com/zh/cli/update-cli) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration, code] <br>
**Output Format:** [Markdown with inline shell commands, JSON bodies, YAML references, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include two-phase execution plans for cluster or application mutations and reminders to protect secrets such as authToken, LicenseKey, and kubeconfig output.] <br>

## Skill Version(s): <br>
0.1.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
