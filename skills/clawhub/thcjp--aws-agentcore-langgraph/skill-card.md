## Description: <br>
Helps developers build and deploy multi-agent systems on AWS Bedrock AgentCore with LangGraph orchestration, including runtime setup, memory, gateway tools, container deployment, and operational commands. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to plan, configure, deploy, invoke, and clean up AWS Bedrock AgentCore applications that use LangGraph for multi-agent orchestration. It is most relevant for teams building cloud-hosted agent workflows that need shared session context, persistent memory, and Gateway-based tool integration. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Cloud deployment and cleanup commands can affect AWS resources if run with broad credentials or in the wrong account or region. <br>
Mitigation: Use least-privilege AWS credentials and verify the target AWS account and region before running deployment or destroy commands. <br>
Risk: Callback URLs can send task results to external endpoints. <br>
Mitigation: Treat callback URLs as data-sharing endpoints and use only approved destinations for sensitive or regulated data. <br>
Risk: Persistent memory workflows may store sensitive or regulated data beyond a single session. <br>
Mitigation: Avoid storing secrets or regulated data in AgentCore Memory unless retention, deletion, and access controls are defined. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/aws-agentcore-langgraph) <br>
- [SkillHub homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline code blocks, shell commands, configuration guidance, and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include AWS CLI and AgentCore CLI commands, LangGraph code snippets, deployment steps, troubleshooting guidance, and cleanup instructions.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
