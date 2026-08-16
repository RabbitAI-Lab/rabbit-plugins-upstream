## Description:

Integrates local Ollama AI model workflows for custom prompts, AI assistance, conversation, and automated agent tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to connect agent workflows with local Ollama-style model tasks, including custom prompts, model calls, intelligent conversation, and automation. It is not intended for decisions that require fully deterministic or unrevised outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks for broad read, write, API, and command-execution authority without clear limits.

Mitigation: Limit use to local Ollama-related tasks and require explicit confirmation before file changes, network or API calls, or shell commands.

Risk: Secrets or private files could be exposed through model prompts, API calls, command execution, or generated file operations.

Mitigation: Avoid sharing secrets or private files with the skill, keep API keys in environment variables, and review command and file-operation proposals before execution.

Risk: Model outputs and automated actions may be incorrect, nondeterministic, or unsuitable for critical decisions.

Mitigation: Review outputs before relying on them and do not use the skill for decisions that require 100 percent deterministic results.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/ollama-integration)
- [Skill homepage](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON-like task results with inline shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include command proposals, file-change guidance, API-call guidance, and model output summaries that should be reviewed before execution.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter reports 1.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
