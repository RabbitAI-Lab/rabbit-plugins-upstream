## Description: <br>
Discovers AWS-hosted AI agent and MCP-relevant assets, emits canonical agent-bom inventory JSON, and optionally scans or exports that inventory under operator control. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[msaad00](https://clawhub.ai/user/msaad00) <br>

### License/Terms of Use: <br>
Apache-2.0 <br>


## Use Case: <br>
Developers, security engineers, and cloud operators use this skill to inventory AWS Bedrock, ECS, SageMaker, Lambda, EKS, Step Functions, EC2, and related agentic infrastructure as canonical agent-bom inventory without handing over long-lived cloud credentials. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: AWS discovery can expose sensitive account, resource, and workload metadata in generated inventory files. <br>
Mitigation: Use read-only AWS profiles or short-lived roles, choose the narrowest required regions and services, and review generated inventory before sharing or exporting it. <br>
Risk: Using broad or long-lived AWS credentials could expand the impact of accidental disclosure or misuse. <br>
Mitigation: Prefer AWS SSO, WebIdentity, or STS assumed-role credentials and do not paste or print access key values. <br>


## Reference(s): <br>
- [agent-bom GitHub repository](https://github.com/msaad00/agent-bom) <br>
- [agent-bom PyPI package](https://pypi.org/project/agent-bom/) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, JSON] <br>
**Output Format:** [Markdown guidance with bash commands and generated JSON inventory files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes inventory or scan/export files only to operator-selected paths.] <br>

## Skill Version(s): <br>
0.98.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
