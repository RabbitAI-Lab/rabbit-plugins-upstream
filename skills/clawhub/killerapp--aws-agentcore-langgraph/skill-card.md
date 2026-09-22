## Description:

Deploy production LangGraph agents on AWS Bedrock AgentCore for multi-agent orchestration, persistent memory, external tools through AgentCore Gateway, shared context, and CLI-based deployment with observability and scaling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[killerapp](https://clawhub.ai/user/killerapp)

### License/Terms of Use:


## Use Case:

Developers and engineers use this skill to design, deploy, inspect, and troubleshoot LangGraph agents running on AWS Bedrock AgentCore. It is suited for multi-agent systems that need runtime deployment, managed memory, Gateway tool integration, CloudWatch observability, and AWS CLI operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cloud deployment commands can create AWS resources, persistent memory, and external service integrations.

Mitigation: Use a least-privilege AWS profile, confirm the target account and region, and review what data will be stored or sent before running AgentCore memory or Gateway examples.

Risk: Destroy and delete commands can remove AgentCore resources.

Mitigation: Verify the exact resource identifiers, account, and region before running cleanup commands, and use dry-run or inspection commands when available.

Risk: Unpinned dependencies can change behavior across environments.

Mitigation: Install in a virtual environment and prefer pinned versions or a lockfile for repeatable deployments.

## Reference(s):

- [AgentCore CLI Reference](references/agentcore-cli.md)
- [AgentCore Runtime Patterns](references/agentcore-runtime.md)
- [AgentCore Memory Integration](references/agentcore-memory.md)
- [AgentCore Gateway Integration](references/agentcore-gateway.md)
- [LangGraph 1.0 Patterns](references/langgraph-patterns.md)
- [AWS Bedrock AgentCore starter toolkit](https://github.com/aws/bedrock-agentcore-starter-toolkit)
- [AWS Bedrock AgentCore Runtime documentation](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime.html)
- [AWS Bedrock AgentCore Memory documentation](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html)
- [AWS Bedrock AgentCore Gateway documentation](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html)
- [LangGraph documentation](https://langchain-ai.github.io/langgraph/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline Python and bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes operational helper scripts for AWS AgentCore resource listing, runtime details, memory details, and CloudWatch log tailing.]

## Skill Version(s):

1.0.2 (source: server evidence release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
