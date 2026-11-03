## Description:

Analyze code-change blast radius with the impact CLI. Use when reviewing diffs, assessing merge or deployment risk, finding affected tests, diffing public contracts, visualizing callers, detecting orphan code, or writing PR/MR impact summaries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[albert-lv](https://clawhub.ai/user/albert-lv)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill with the Impact CLI to understand which callers, tests, and public contracts may be affected by code changes. It supports code review and merge or deployment risk assessment, with human review of the analysis results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The upstream implementation was not available for verification.

Mitigation: Review and pin the upstream source before building the CLI.

Risk: Analysis output may include proprietary code or credentials if shared externally.

Mitigation: Keep proprietary code and credentials out of results shared outside the trusted environment.

Risk: Impact classifications and dependency analysis may not capture every relevant behavior.

Mitigation: Review breaking and warning results, check affected call sites, and use business context and relevant tests before making decisions.

## Reference(s):

- [Impact Analyzer project homepage](https://github.com/nano-harness/impact-analyzer)
- [Impact on ClawHub](https://clawhub.ai/albert-lv/skills/impact)

## Skill Output:

**Output Type(s):** [Analysis, Text, JSON, Markdown]

**Output Format:** [Text, JSON, or Markdown from the Impact CLI, depending on the command and selected format]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May summarize affected callers, tests, public contracts, or orphan candidates; results are review guidance and not a correctness guarantee.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
