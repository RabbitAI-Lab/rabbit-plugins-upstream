## Description:

Captures lint errors, type mismatches, runtime bugs, anti-patterns, refactoring opportunities, language idiom gaps, debugging insights, and tooling issues to enable continuous coding improvement.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jose-compu](https://clawhub.ai/user/jose-compu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and coding agents use this skill to capture recurring coding errors, useful debugging insights, refactoring opportunities, and feature requests in local Markdown learning logs. Teams can review those logs and promote proven patterns into style guides, lint rules, snippets, debug playbooks, or reusable skills.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local learning logs may contain secrets, private code, or sensitive error output if entries are copied without review.

Mitigation: Redact secrets and private code, prefer summaries over raw stack traces, and review .learnings content before committing or sharing it.

Risk: Optional hooks can add reminders across future sessions when enabled too broadly.

Mitigation: Keep hooks project-scoped, opt in only where coding-learning reminders are wanted, and narrow hook matchers to the relevant coding workflow.

Risk: Promoting a logged pattern into a style guide, lint rule, snippet, or new skill could preserve incorrect guidance.

Mitigation: Review proposed promotions and apply them only after explicit user approval.

## Reference(s):

- [OpenClaw Integration](references/openclaw-integration.md)
- [Hook Setup Guide](references/hooks-setup.md)
- [Entry Examples](references/examples.md)
- [Self Improving Coding on ClawHub](https://clawhub.ai/jose-compu/skills/self-improving-coding)

## Skill Output:

**Output Type(s):** [Markdown, Files, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes or updates local learning logs under .learnings/ when the agent follows the skill; optional hooks emit reminder text.]

## Skill Version(s):

1.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
