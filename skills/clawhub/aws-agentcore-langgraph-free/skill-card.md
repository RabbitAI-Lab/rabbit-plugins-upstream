## Description: <br>
This skill helps developers build and deploy a basic single-agent LangGraph application on AWS Bedrock AgentCore Runtime with tool routing and container deployment guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to prototype and validate a single-agent AWS Bedrock AgentCore Runtime service backed by LangGraph routing, local development commands, and container deployment steps. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Agent command execution over an AWS deployment workflow can create, modify, or delete cloud resources. <br>
Mitigation: Confirm the active AWS account and region before running deployment commands, review each proposed command, and treat `agentcore destroy` as resource-deleting. <br>
Risk: Callback URLs can send workflow results to an external endpoint. <br>
Mitigation: Use only trusted HTTPS callback URLs and confirm the recipient before including a callback URL in a request. <br>
Risk: Secret handling guidance may encourage storing sensitive values in container build files. <br>
Mitigation: Do not put secrets in Dockerfile `ENV` lines; prefer runtime environment variables or a managed secret store appropriate for the deployment environment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/aws-agentcore-langgraph-free) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with Python, JSON, and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [None] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata; artifact frontmatter lists 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
