## Description: <br>
Operate RAGFlow v0.26.4 deployments through a bundled Node CLI for everyday knowledge-base setup, document ingestion, parsing, retrieval, chat assistants, agents, GraphRAG, connectors, models, and diagnostics. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lunarcache](https://clawhub.ai/user/lunarcache) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to manage RAGFlow knowledge bases, documents, retrieval, chat assistants, agents, GraphRAG workflows, model configuration, and diagnostics from an agent session. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses powerful RAGFlow administration access through RAGFLOW_API_KEY. <br>
Mitigation: Install it only where a dedicated, rotatable API key is acceptable, and use HTTPS for production RAGFlow URLs. <br>
Risk: Delete and update commands can change or remove datasets, documents, chunks, sessions, agents, connectors, or model configuration. <br>
Mitigation: Confirm the exact resource and scope before destructive or broad update operations. <br>
Risk: Webhook or browser-enabled agent DSL can expose integrations or embedded access paths if deployed without review. <br>
Mitigation: Review webhook and browser-enabled agent DSL before deployment and avoid echoing provider keys, system tokens, beta values, or auth-bearing embed URLs into chat or logs. <br>


## Reference(s): <br>
- [RAGFlow Skill on ClawHub](https://clawhub.ai/lunarcache/skills/skill-for-ragflow) <br>
- [ClawHub metadata homepage](https://github.com/LunarCache/ragflow-skill) <br>
- [Command Reference](references/COMMANDS.md) <br>
- [Programmatic API and Configuration](references/API.md) <br>
- [RAGFlow Custom Agent Guide](references/AGENT_GUIDE.md) <br>
- [Troubleshooting](references/TROUBLESHOOTING.md) <br>
- [Output Format Reference](references/REFERENCE.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown summaries with inline shell commands and JSON snippets.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can emit raw JSON from the CLI when --json is used; user-facing responses should redact API keys, provider keys, system tokens, beta values, and auth-bearing embed URLs.] <br>

## Skill Version(s): <br>
1.7.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
