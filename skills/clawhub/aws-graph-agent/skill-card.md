## Description: <br>
AWS Graph Agent guides agents through AWS Bedrock AgentCore and LangGraph multi-agent deployment, covering StateGraph orchestration, Runtime HTTP packaging, memory, Gateway integration, and CLI lifecycle management. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to plan, configure, deploy, test, and clean up AWS Bedrock AgentCore and LangGraph multi-agent systems. It is most relevant for AWS-based agents that need orchestration, memory, external tool integration, and CLI lifecycle guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: AWS commands may create, modify, or destroy cloud resources and can incur ongoing costs. <br>
Mitigation: Verify the AWS account and region before execution, use least-privilege credentials, and run cleanup commands such as agentcore destroy after testing. <br>
Risk: Callback URLs and credentials can expose deployment data or account access if mishandled. <br>
Mitigation: Use only trusted callback URLs, keep API keys and AWS credentials out of version control, and review generated commands before running them. <br>
Risk: Bedrock AgentCore deployments may fail when model approval, region support, naming, or memory settings are incomplete. <br>
Mitigation: Complete the deployment preflight checks, confirm Bedrock model access, choose a supported region, and decide whether memory should be enabled before launch. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/thcjp/skills/aws-graph-agent) <br>
- [SkillHub homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with Python and bash code blocks plus JSON-shaped result examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include AWS deployment commands, configuration steps, execution logs, and cleanup guidance.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata; artifact frontmatter reports 1.0.1) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
