## Description:

Helps developers operate RAGFlow v0.27.2 datasets, document ingestion, retrieval, chat, agents, and related services.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lunarcache](https://clawhub.ai/user/lunarcache)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to administer a configured RAGFlow deployment, including knowledge bases, document pipelines, retrieval, chat assistants, and agents.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Administrative commands can alter or delete resources on the configured RAGFlow server.

Mitigation: Check the exact target resources and obtain authorization before confirming destructive commands.

Risk: API keys, provider credentials, and embedded access tokens may be exposed.

Mitigation: Use a dedicated rotatable API key over HTTPS and keep credentials and token-bearing URLs out of chat and logs.

Risk: Agent or webhook examples may cause unintended behavior if deployed unchanged.

Mitigation: Review agent and webhook configurations before deployment.

## Reference(s):

- [Project homepage (listed in skill metadata)](https://github.com/LunarCache/ragflow-skill)
- [Command reference](references/COMMANDS.md)
- [Agent authoring guide](references/AGENT_GUIDE.md)
- [API reference](references/API.md)
- [Troubleshooting](references/TROUBLESHOOTING.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown summaries with optional shell commands and JSON results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Summaries can include parsing status, retrieval scores, and redacted operational results.]

## Skill Version(s):

3.0.0 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
