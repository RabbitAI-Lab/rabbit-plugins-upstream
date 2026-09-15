## Description:

AML Sentinel is a zero-dependency CLI-oriented skill that checks transaction data for AML risk patterns such as structuring, rapid in/out movement, cross-border transactions without KYC, and unreported large transactions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

Developers, compliance teams, and agent operators use this skill to run local, structured AML checks over transaction JSON or JSONL data and surface advisory risk findings for human review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Mutable global installation instructions can install a moving version of the skill.

Mitigation: Prefer a pinned release or verified commit before installing or deploying the skill.

Risk: Input-validation flaws can understate AML risk, and output may be mistaken for a final compliance decision.

Mitigation: Validate transaction schemas before use and treat the skill's results as advisory findings requiring human compliance review.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/aml-sentinel)
- [Project homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Plain text or JSON risk results, with Markdown guidance and inline shell commands in the skill documentation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [CLI exits with code 0 when no high risk is found, 1 when high risk is found, and 2 for usage or environment errors.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter reports 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
