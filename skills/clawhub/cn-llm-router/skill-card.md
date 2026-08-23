## Description:

cn-llm-router provides a unified command-line router for Chinese text and vision LLM providers, selecting models by task, cost, reasoning needs, context length, and multimodal requirements while supporting streaming, cost reports, local cache, mock mode, and update checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fyniujin](https://clawhub.ai/user/fyniujin)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technical users use this skill to route prompts across supported Chinese LLM providers, compare cost and quality, manage provider keys through environment variables, and run offline mock or dry-run flows before making live API calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and responses may be sent to the selected third-party model provider during live chat or arena use.

Mitigation: Configure only trusted provider keys and use dry-run, manual, or mock flows when live provider traffic is not appropriate.

Risk: Local caching can store prompts and responses on the user's machine.

Mitigation: Use --no-cache for sensitive prompts and clear the cache regularly.

Risk: Arena voting can expose confidential content to multiple configured providers.

Mitigation: Avoid arena voting on confidential content and restrict model comparisons to approved providers.

Risk: Health checks and update or webhook settings can create network traffic in restricted environments.

Mitigation: Use dry-run, manual, or mock flows in restricted networks and configure only trusted update URLs or webhooks.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/fyniujin/skills/cn-llm-router)
- [Publisher profile](https://clawhub.ai/user/fyniujin)
- [SkillHub homepage](https://skillhub.cn/skill/cn-llm-router)
- [routing-rules.md](artifact/references/routing-rules.md)
- [models.yaml](artifact/references/models.yaml)
- [config.example.json](artifact/config.example.json)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [CLI text, JSON, Markdown guidance, and generated provider responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May stream model output, emit routing decisions and cost reports, and write local SQLite cache, cost, mock, and arena records.]

## Skill Version(s):

2.4.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
