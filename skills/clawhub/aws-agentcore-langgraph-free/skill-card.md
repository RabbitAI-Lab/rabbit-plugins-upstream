## Description: <br>
Aws Agentcore Langgraph Free helps developers build and deploy a basic single-agent AWS Bedrock AgentCore Runtime service with LangGraph routing and container deployment guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to prototype a single-agent LangGraph application, wrap it with AWS Bedrock AgentCore Runtime, and follow basic local development, container deployment, invocation, and cleanup steps. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: AWS deployment and destroy commands can create, modify, or delete cloud resources. <br>
Mitigation: Confirm the target AWS account and region, use least-privilege credentials, and manually review cleanup commands before execution. <br>
Risk: The skill accepts optional callback URLs and may handle cloud execution results. <br>
Mitigation: Avoid sending sensitive deployment outputs or credentials to untrusted callback URLs. <br>
Risk: AgentCore and Bedrock model setup can fail when account access, region, model use-case approval, or naming rules are not satisfied. <br>
Mitigation: Verify Bedrock model access, region support, and AgentCore naming requirements before launching the deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/aws-agentcore-langgraph-free) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>
- [Project homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline Python, bash, and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes AgentCore and LangGraph setup steps, deployment commands, troubleshooting notes, and cleanup guidance.] <br>

## Skill Version(s): <br>
1.0.1 (source: server-resolved release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
