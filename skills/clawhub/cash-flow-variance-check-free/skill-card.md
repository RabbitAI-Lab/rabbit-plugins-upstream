## Description:

现金流预测与实际差异表逐项核对（净流量复算、差异复算、合计勾稽、重复与空缺检测），每条结论引用原文。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and treasury staff use this skill before monthly cash meetings or rolling forecast reviews to check forecast-vs-actual cash-flow tables for arithmetic consistency, totals, duplicate rows, blanks, and negative flow amounts. It provides deterministic table checks rather than accounting advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may treat deterministic variance checks as accounting advice.

Mitigation: Review findings against accounting policy, source records, and finance-team judgment before using them in decisions.

Risk: The free-vs-full documentation is inconsistent around negative inflow/outflow checks.

Mitigation: Rely on the executed check list and checks_not_run output for the active scope, and confirm the feature boundary before depending on that check.

Risk: Cash-flow table text can contain sensitive business data.

Mitigation: Run the checker locally on only the minimum table content needed for review.

## Reference(s):

- [ClawHub skill page: cash-flow-variance-check-free](https://clawhub.ai/chenqg618/skills/cash-flow-variance-check-free)
- [ClawHub publisher profile: chenqg618](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Human-readable text or JSON containing executed checks, findings, summary, omitted checks, and scope.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally with Node.js standard-library code and does not require network access or API keys according to the supplied security evidence.]

## Skill Version(s):

1.0.53 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
