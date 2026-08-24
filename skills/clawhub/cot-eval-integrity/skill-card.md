## Description:

eval-integrity audits LLM evaluation or benchmark repositories for credibility practices and emits a scored report with evidence, severity, and concrete fixes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[conorbronsdon](https://clawhub.ai/user/conorbronsdon)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, benchmark maintainers, and reviewers use this skill before publishing or submitting evaluation results to audit integrity practices across pre-registration, contamination, holdout hygiene, judge validity, statistical honesty, reproducibility, and leaderboard publish mechanics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The audit may expose benchmark files, CI configuration, results, and open PR metadata to the agent running the skill.

Mitigation: Install and run it only in repositories you are comfortable letting the agent inspect.

Risk: Suggested fixes could change benchmark methodology or published leaderboard behavior if applied automatically.

Mitigation: Use the skill as a read-only audit and require explicit user approval before editing the benchmark, rerunning evaluations, or changing leaderboard artifacts.

## Reference(s):

- [Canonical GitHub repository](https://github.com/conorbronsdon/eval-integrity)
- [ClawHub skill page](https://clawhub.ai/conorbronsdon/skills/cot-eval-integrity)
- [Dimension audit briefs](patterns/dimension-prompts.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown audit report with file:line evidence, severity ratings, and concrete fixes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only workflow; runs dimension audits in parallel when subagents are available or sequentially when they are not.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
