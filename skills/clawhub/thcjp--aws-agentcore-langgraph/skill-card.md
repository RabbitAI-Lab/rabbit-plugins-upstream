## Description: <br>
Helps developers build and deploy multi-agent systems on AWS Bedrock AgentCore using LangGraph orchestration, including runtime, memory, gateway, and CLI guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and engineers use this skill to get concise implementation, deployment, troubleshooting, and configuration guidance for AWS Bedrock AgentCore agents orchestrated with LangGraph. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can lead an agent to install packages, deploy or destroy AWS resources, configure gateways, and write AgentCore memory. <br>
Mitigation: Require explicit user approval for each package install, AWS deploy, gateway deploy, memory write, or destroy command before execution. <br>
Risk: Cloud-changing actions may affect real AWS accounts or regions if run with broad credentials. <br>
Mitigation: Use a least-privilege AWS profile in a test account or isolated region before production use. <br>
Risk: AgentCore memory may retain sensitive information if prompts or customer data are stored without retention controls. <br>
Mitigation: Avoid storing secrets or sensitive customer data unless a retention policy and access controls are defined. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with Python and bash code snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose package installs, AWS CLI operations, AgentCore deployments, gateway configuration, memory operations, and cleanup commands.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata; artifact frontmatter lists 1.0.2) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
