## Description: <br>
Deploy production LangGraph agents on AWS Bedrock AgentCore. Use for (1) multi-agent systems with orchestrator and specialist agent patterns, (2) building stateful agents with persistent cross-session memory, (3) connecting external tools via AgentCore Gateway (MCP, Lambda, APIs), (4) managing shared context across distributed agents, or (5) deploying complex agent ecosystems via CLI with production observability and scaling. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[killerapp](https://clawhub.ai/user/killerapp) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to design, deploy, observe, and operate LangGraph-based multi-agent systems on AWS Bedrock AgentCore, including runtime, memory, gateway, and CLI workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Deployment, cleanup, logging, and memory examples can affect AWS account resources. <br>
Mitigation: Use least-privileged AWS credentials and confirm AWS profile, account, and region before running deploy, logging, memory, or destroy commands. <br>
Risk: AgentCore memory workflows may store sensitive, personal, or regulated data across sessions. <br>
Mitigation: Avoid storing secrets, PII, or regulated data unless retention and deletion controls are in place. <br>
Risk: Production deployment examples may create or modify cloud infrastructure. <br>
Mitigation: Prefer dry-run or non-production environments before applying changes to production resources. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/killerapp/skills/aws-agentcore-langgraph) <br>
- [AWS Bedrock AgentCore starter toolkit](https://github.com/aws/bedrock-agentcore-starter-toolkit) <br>
- [AgentCore CLI Reference](references/agentcore-cli.md) <br>
- [AgentCore Runtime Patterns](references/agentcore-runtime.md) <br>
- [AgentCore Memory Integration](references/agentcore-memory.md) <br>
- [AgentCore Gateway Integration](references/agentcore-gateway.md) <br>
- [LangGraph 1.0 Patterns](references/langgraph-patterns.md) <br>
- [AWS AgentCore runtime documentation](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime.html) <br>
- [AWS AgentCore memory documentation](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html) <br>
- [AWS AgentCore gateway documentation](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with Python examples, shell commands, configuration notes, and troubleshooting guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes optional shell scripts that query AWS Bedrock AgentCore resources and CloudWatch logs.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
