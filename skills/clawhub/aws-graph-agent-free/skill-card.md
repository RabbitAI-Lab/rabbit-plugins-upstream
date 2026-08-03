## Description: <br>
AWS Graph Agent Free helps developers build basic AWS Bedrock AgentCore and LangGraph agents with StateGraph orchestration, ToolNode execution, and AgentCore Runtime container deployment as an HTTP service on port 8080. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to scaffold and deploy a single-agent LangGraph workflow on AWS Bedrock AgentCore, including local development, container launch, invocation testing, and cleanup. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may run local package installation commands and AgentCore CLI commands. <br>
Mitigation: Review proposed commands before execution and run them in an appropriate local or sandboxed development environment. <br>
Risk: The skill may use API or AWS credentials and configure callback URLs. <br>
Mitigation: Use trusted callback URLs only, avoid committing secrets, and provide credentials with the minimum permissions needed for the deployment task. <br>
Risk: The skill may expose an HTTP service on port 8080 and deploy billable cloud resources. <br>
Mitigation: Restrict service exposure during testing and run cleanup commands such as agentcore destroy when finished to avoid ongoing costs. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with bash, Python, and JSON code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Provides deployment steps, troubleshooting notes, and cleanup guidance for AWS Bedrock AgentCore and LangGraph workflows.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
