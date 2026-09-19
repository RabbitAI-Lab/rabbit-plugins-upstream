## Description:

Routes prompts and multimodal tasks across Chinese LLM providers with task-aware model selection, streaming calls, cost reporting, local cache/session features, and offline mock workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fyniujin](https://clawhub.ai/user/fyniujin)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to choose, call, compare, and monitor multiple Chinese LLM providers from one CLI entry point. It supports routing for chat, code, reasoning, summarization, translation, extraction, embeddings, reranking, long-document workflows, and multimodal description.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and task content may be sent to configured model providers during live calls.

Mitigation: Configure only trusted providers, use offline route or mock modes for planning, and avoid sending confidential prompts unless the selected provider is approved for that data.

Risk: Prompt and response history may be retained locally by cache, session, and arena features.

Mitigation: Use --no-cache for confidential or critical work, avoid --session unless needed, and periodically clear local cache and session data.

Risk: Configured update_url or webhook destinations can disclose usage or operational metadata.

Mitigation: Leave optional destinations unset unless needed, and configure only trusted update and webhook endpoints.

Risk: Local semantic cache matching may return stale or incorrect results for similar but different prompts.

Mitigation: Use --no-cache for production, financial, code-generation, and real-time information tasks that require a fresh model call.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/fyniujin/skills/cn-llm-router)
- [models.yaml](artifact/references/models.yaml)
- [routing-rules.md](artifact/references/routing-rules.md)
- [version.json homepage](https://skillhub.cn/skill/cn-llm-router)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, JSON, Guidance]

**Output Format:** [Markdown and terminal-oriented text, with optional JSON outputs for supported commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include routed provider/model choices, generated model responses, token and cost estimates, local reports, configuration guidance, and mock outputs.]

## Skill Version(s):

2.6.0 (source: SKILL.md frontmatter, artifact/version.json, and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
