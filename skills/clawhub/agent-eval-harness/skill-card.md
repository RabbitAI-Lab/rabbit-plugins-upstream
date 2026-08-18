## Description:

Agent Eval Harness drives regression test cases against an agent, measures pass rate, and flags capability regressions against historical baselines.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qq435912743](https://clawhub.ai/user/qq435912743)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent maintainers use this skill to run repeatable regression checks after skill, prompt, or model changes and to track pass-rate drops that may require review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can retain regression baselines plus usage history, errors, notes, and preferences in plaintext local files.

Mitigation: Avoid recording sensitive prompts or private operational details, treat the learning module as optional, and review or delete learned_patterns.json and baseline files when retained history is not desired.

Risk: Baseline updates during normal runs can make regressions harder to interpret if accepted without review.

Mitigation: Use isolated regression paths in CI and review baseline changes before accepting them as the new comparison point.

Risk: Substring and custom predicate checks can miss semantically equivalent answers or unsafe outputs.

Mitigation: Review test cases before relying on pass rates and add stronger semantic checks for higher-risk evaluations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qq435912743/skills/agent-eval-harness)
- [Publisher profile](https://clawhub.ai/user/qq435912743)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with Python code and shell command examples; the harness returns structured pass-rate summaries and writes JSONL baselines.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local execution with optional persistent learning and regression baseline files.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
