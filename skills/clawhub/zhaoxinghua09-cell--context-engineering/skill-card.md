## Description:

Helps agents audit context relevance, redundancy, token budgets, and decay, then plan improvements to prompts, memory, retrieval, and tool outputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent builders use this skill to diagnose long-conversation quality and token-cost problems, assess context blocks, and plan prompt, memory, and retrieval adjustments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Some documented CLI flags and examples may not match the included script.

Mitigation: Check the script's actual --help output before running examples.

Risk: Context estimates and suggested prompt, memory, or retrieval changes may be inaccurate.

Mitigation: Review estimates and proposed changes before applying them; do not automatically rewrite settings.

## Reference(s):

- [Context Engineering on ClawHub](https://clawhub.ai/zhaoxinghua09-cell/skills/context-engineering)

## Skill Output:

**Output Type(s):** [Guidance, Text]

**Output Format:** [Markdown guidance and plain-text CLI reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [CLI reports include approximate token allocations, duplicate-block warnings, and an audit checklist.]

## Skill Version(s):

1.0.5 (source: server-resolved ClawHub release; artifact frontmatter says 1.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
