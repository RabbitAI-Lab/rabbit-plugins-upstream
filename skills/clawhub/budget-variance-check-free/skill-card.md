## Description:

This free skill checks budget execution tables for row arithmetic, total-row consistency, duplicate or blank entries, and zero-budget variance-rate issues, with findings grounded in the provided table.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and treasury employees use this skill during monthly close, reconciliation, or inventory checks to review budget execution table consistency before downstream reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The free edition omits execution-rate, cumulative, negative-value, range, and direction checks.

Mitigation: Review the listed checks_not_run before relying on results, and do not treat a clean free-edition result as coverage for omitted checks.

Risk: Insufficient or unrecognized table input produces no conclusion rather than a finding.

Mitigation: Provide a budget execution table with recognizable headers and treat insufficient_input as no analysis performed.

Risk: Budget execution data may be sensitive financial material.

Mitigation: Run the checker locally on only the needed table text and review outputs before sharing them.

Risk: The checker evaluates table consistency, not whether the budget itself is reasonable.

Mitigation: Use the output as arithmetic and reconciliation evidence, then apply separate business review for budget policy or cause analysis.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/budget-variance-check-free)
- [Publisher profile: chenqg618](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Console text or JSON from a local Node.js checker]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a budget execution table with recognizable headers; inputs over 4 MB are rejected; security evidence reports no observed network use, persistence, credential handling, or unrelated behavior.]

## Skill Version(s):

1.0.57 (source: server evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
