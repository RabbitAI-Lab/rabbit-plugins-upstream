## Description:

Super Agent orchestrates a local closed-loop agent workflow that senses context, plans long-horizon work, executes tool-assisted steps, verifies results, reflects on progress, and stores run memory for later iterations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qq435912743](https://clawhub.ai/user/qq435912743)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent builders use this skill to run a stateful local orchestration loop for long-horizon goals, producing plans, progress reports, verification signals, reflections, and memory for the next run.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Goals, preferences, progress reports, and memory can be written to local JSON or JSONL files.

Mitigation: Avoid entering secrets or sensitive business data unless local persistence is acceptable, and review or delete generated state, report, memory, and learned-pattern files when needed.

Risk: The skill can invoke local helper scripts as part of its orchestration loop.

Mitigation: Review generated plans and local script behavior before deployment, especially in environments with access to sensitive files or tools.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qq435912743/skills/super-agent)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON run artifacts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write local state, report, memory, and learned-pattern JSON or JSONL files during use.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
