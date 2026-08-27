## Description:

memory-bench helps agent developers, AI product teams, and model evaluators run a local long-term-memory benchmark with 12 question types, EM/F1 scoring, a deterministic internal backend, and an optional OpenAI-compatible LLM backend.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

Developers, AI product managers, and evaluation teams use this skill to measure whether an agent or LLM can retain and retrieve long-term memory across temporal, entity, negation, counterfactual, and cross-session questions. It supports local reproducible checks and optional real-model evaluation when the user supplies API credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A self-test or API-mode run may use existing REAL_API_KEY, SILICONFLOW_API_KEY, or DEEPSEEK_API_KEY values and contact an external model service.

Mitigation: Run in a clean shell or unset those variables unless external model evaluation is intended; set MODEL_BACKEND=internal for local-only benchmarking.

Risk: API-mode evaluation sends benchmark context and questions to the configured model provider and may incur usage cost.

Mitigation: Use only trusted providers, avoid sensitive custom benchmark content, and set REAL_API_BASE and REAL_MODEL explicitly before running API mode.

Risk: Result JSON or radar output files can be overwritten in the workspace.

Mitigation: Use a disposable workspace or explicit output paths, especially when generating radar SVG output.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zhaoxinghua09-cell/skills/memory-bench)
- [Publisher Profile](https://clawhub.ai/user/zhaoxinghua09-cell)
- [SiliconFlow API Base](https://api.siliconflow.cn/v1)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, JSON, Code]

**Output Format:** [Markdown guidance with inline shell commands; benchmark tools emit console text, JSON results, and optional SVG files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Default benchmark mode is local and deterministic; API mode depends on user-supplied environment variables and an OpenAI-compatible model service.]

## Skill Version(s):

1.0.1 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
