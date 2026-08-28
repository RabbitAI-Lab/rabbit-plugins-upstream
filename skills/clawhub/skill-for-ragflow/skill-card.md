## Description:

Operate RAGFlow v0.27.0 deployments through a bundled Node CLI for knowledge-base setup, document ingestion, parsing, retrieval, chat assistants, agents, GraphRAG, connectors, models, and diagnostics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lunarcache](https://clawhub.ai/user/lunarcache)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to administer RAGFlow servers, manage datasets and document pipelines, run retrieval and chat workflows, configure agents, connectors, and models, and diagnose server issues.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can administer a configured RAGFlow server and make real data or configuration changes.

Mitigation: Install it only for a RAGFlow server the agent is intended to administer, use HTTPS and a dedicated rotatable RAGFlow API key, and review delete, provider, connector, embed-token, and log-level operations before production execution.

Risk: RAGFlow API keys, provider credentials, system tokens, beta values, and embed URLs can expose operational access if printed or stored insecurely.

Mitigation: Keep credentials in environment variables or files, prefer RAGFLOW_PROVIDER_API_KEY or api-key files for provider credentials, and redact secret values in user-facing responses unless explicitly requested.

## Reference(s):

- [RAGFlow Skill Source](https://github.com/LunarCache/ragflow-skill)
- [Command Reference](references/COMMANDS.md)
- [Programmatic API and Configuration](references/API.md)
- [RAGFlow Custom Agent Guide](references/AGENT_GUIDE.md)
- [Troubleshooting](references/TROUBLESHOOTING.md)
- [Output Format Reference](references/REFERENCE.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown summaries with inline shell commands and JSON command output when requested.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Operational output should redact API keys, provider keys, system tokens, beta values, and embed URLs containing auth query values unless the user explicitly requests copy-paste secret material.]

## Skill Version(s):

1.8.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
