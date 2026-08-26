## Description:

Doubao Chat helps an agent use a Doubao chat API for conversational responses, model calls, and search-style retrieval workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, independent builders, and workflow teams can use this skill to ask an agent for Doubao-backed chat responses, model-call assistance, and search or retrieval support. It is not appropriate for decisions that require deterministic or human-reviewed judgment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence reports broad local read, write, and command execution authority without clear implementation or scope limits.

Mitigation: Install only in a constrained environment and allow only the file and command access needed for the intended chat/API workflow.

Risk: The skill may send prompts, context, or configuration values to external APIs.

Mitigation: Review inputs for secrets or sensitive data, keep API keys in environment variables, and confirm what data is sent before use.

Risk: The scanner verdict is suspicious even though no clear malicious behavior was found.

Mitigation: Review the skill before installation and monitor execution, file access, and outbound API activity during initial use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/doubao-chat)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON examples and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May require an API key and external API access.]

## Skill Version(s):

1.0.2 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
