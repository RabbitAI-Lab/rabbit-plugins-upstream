## Description: <br>
Operate RAGFlow v0.26.4 deployments through the bundled Node CLI and API client for datasets, documents, parsing, chunks, retrieval, chat assistants, agents, embedded website access, model providers, system settings, and API diagnostics. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lunarcache](https://clawhub.ai/user/lunarcache) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to manage and diagnose RAGFlow deployments, including knowledge-base ingestion, retrieval, chat and agent workflows, embedded access, model-provider configuration, and system administration. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can perform high-impact RAGFlow administration actions, including deletes and credential-management workflows. <br>
Mitigation: Use least-privilege RAGFlow API keys and require explicit confirmation before destructive or credential-management commands. <br>
Risk: API keys, provider keys, system tokens, beta values, and embed URLs may expose operational access. <br>
Mitigation: Store secrets in environment variables or local configuration and redact tokens, beta values, and embed auth parameters from normal responses. <br>
Risk: Public webhook exposure can allow unwanted callers or unvalidated input. <br>
Mitigation: Add authentication, caller restrictions, input validation, and rate limits before exposing webhook examples publicly. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/lunarcache/skills/skill-for-ragflow) <br>
- [Project Homepage](https://github.com/LunarCache/ragflow-skill) <br>
- [RAGFlow Command Reference](artifact/references/COMMANDS.md) <br>
- [RAGFlow API Reference](artifact/references/API.md) <br>
- [RAGFlow Custom Agent Guide](artifact/references/AGENT_GUIDE.md) <br>
- [Troubleshooting Guide](artifact/references/TROUBLESHOOTING.md) <br>
- [Output Format Reference](artifact/references/REFERENCE.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands, JSON examples, and concise operational summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Prefers JSON CLI output for automation and redacts API keys, provider keys, beta values, tokens, and embed auth values unless explicitly requested.] <br>

## Skill Version(s): <br>
1.6.0 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
