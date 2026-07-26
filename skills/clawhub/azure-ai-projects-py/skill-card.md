## Description: <br>
Build AI applications using the Azure AI Projects Python SDK for Foundry project clients, versioned agents, tools, evaluations, connections, deployments, datasets, indexes, async workflows, and OpenAI-compatible clients. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thegovind](https://clawhub.ai/user/thegovind) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to generate Azure AI Foundry Python SDK guidance, examples, and implementation patterns for project clients, agents, tools, evaluations, deployments, connections, datasets, indexes, and async workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Azure connection examples can expose credentials when credentials are requested or printed. <br>
Mitigation: Use least-privilege Azure credentials, treat include_credentials=True results as sensitive, and avoid logging or sharing connection secrets. <br>
Risk: File, dataset, index, and tool examples can upload or route user data to Azure services or connected external services. <br>
Mitigation: Confirm organizational approval before uploading secrets or regulated data and review privacy, retention, and storage behavior for each connected service. <br>
Risk: The skill provides documentation and examples rather than an autonomous runtime safety boundary. <br>
Mitigation: Review generated code and configuration before execution, and scan adapted examples as part of normal deployment review. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thegovind/skills/azure-ai-projects-py) <br>
- [Agent Operations Reference](references/agents.md) <br>
- [Agent Tools Reference](references/tools.md) <br>
- [Evaluation Reference](references/evaluation.md) <br>
- [Connections Operations Reference](references/connections.md) <br>
- [Deployments Operations Reference](references/deployments.md) <br>
- [Datasets and Indexes Reference](references/datasets-indexes.md) <br>
- [Async Patterns Reference](references/async-patterns.md) <br>
- [Azure AI Projects SDK Acceptance Criteria](references/acceptance-criteria.md) <br>
- [Azure SDK for Python technical reference repository](https://github.com/Azure/azure-sdk-for-python) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with Python and shell code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only guidance; examples may include Azure SDK calls, environment variables, and configuration snippets.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
