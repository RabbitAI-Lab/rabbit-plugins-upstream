## Description:

Analyzes agent conversation logs or context inventories to estimate token use, identify context pollution and compaction risks, and suggest governance actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[z-zihan](https://clawhub.ai/user/z-zihan)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use the skill to see how a session's context is spent, review possible instruction loss during compaction, and prioritize practical context-management steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Session logs can contain sensitive excerpts that helper scripts may print before the final report is redacted.

Mitigation: Choose logs deliberately, inspect script output, and redact sensitive excerpts before sharing results.

Risk: The constraint audit can incorrectly report that an instruction was lost during summarization.

Mitigation: Check each loss claim against the actual summary and confirm the instruction's authority before recommending it for system instructions or configuration.

## Reference(s):

- [Project homepage](https://github.com/z-Zihan/awesome-skills)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, Guidance]

**Output Format:** [Markdown analysis report or machine-readable JSON summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Token counts are estimates except where usage data provides measured values; recommendations are read-only.]

## Skill Version(s):

1.7.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
