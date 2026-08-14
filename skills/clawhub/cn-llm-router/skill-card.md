## Description:

Routes prompts across supported Chinese LLM providers from one CLI, with task-aware model selection, cost tracking, streaming output, local cache support, offline mock mode, and update checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fyniujin](https://clawhub.ai/user/fyniujin)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to choose and call a suitable Chinese LLM provider for chat, code, reasoning, translation, summarization, extraction, and cost-sensitive workloads while keeping provider keys in their own environment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and responses may be sent to configured third-party model providers during chat or arena use.

Mitigation: Use only approved providers and avoid secrets, regulated data, or other sensitive content unless the provider path has been reviewed.

Risk: Prompt, response, cost, cache, and arena history can be stored in local SQLite databases.

Mitigation: Disable cache for sensitive sessions where appropriate and manage or delete the local databases according to local data-retention requirements.

Risk: Semantic or fuzzy cache matching can return a stale or incorrect cached response for a similar but different prompt.

Mitigation: Use --no-cache for critical, real-time, financial, or code-generation tasks, and clear local cache entries when outputs must be fresh.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/fyniujin/skills/cn-llm-router)
- [Routing rules](references/routing-rules.md)
- [Model registry](references/models.yaml)
- [Configuration example](config.example.json)
- [Version metadata](version.json)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, JSON]

**Output Format:** [CLI text, JSON responses, shell commands, configuration guidance, and local text or HTML reports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May stream model output, estimate token usage when providers omit usage data, and write local SQLite cost, cache, and arena history.]

## Skill Version(s):

2.3.0 (source: SKILL.md frontmatter, evidence release metadata, version.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
