## Description:

Eval Bench Builder helps agents turn capability descriptions and edge cases into structured, reproducible evaluation samples with inputs, expected outputs, and judge criteria, with a zero-dependency script for emitting JSONL benchmarks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

Developers, evaluation authors, and agent maintainers use this skill to create reusable benchmark cases for agents, models, or skills when they need repeatable regression checks instead of subjective assessment. Human review remains important for regulated, sensitive, or high-impact decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release security summary flags an unpinned global installer that can affect future agent sessions.

Mitigation: Inspect the artifact before installation, pin the repository commit or installer version, and install into a local or isolated skill directory where possible.

Risk: The release security summary notes proactive self-promotion in the installation guidance.

Mitigation: Review the skill's behavior and installation instructions before adopting it in a shared or production agent environment.

Risk: Generated benchmark cases can be incomplete or misleading if the source capability description and edge cases are weak.

Mitigation: Have a domain reviewer validate the benchmark cases and judge criteria before relying on them for release or regression decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/eval-bench-builder)
- [Publisher homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)
- [LGD theory reference](https://github.com/zhaoxinghua09-cell/lgd-theory)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance and JSONL benchmark records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The benchmark script writes newline-delimited JSON records for reproducible evaluation cases.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata; artifact frontmatter says 1.2.0 and manifest.json says 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
