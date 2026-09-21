## Description:

Provides a bilingual finance research framework for generating macro, fixed income, equity, strategy, and quantitative research report outlines with source tagging, review checkpoints, and non-advisory boundaries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gechengling](https://clawhub.ai/user/gechengling)

### License/Terms of Use:

MIT-0

## Use Case:

Investment researchers, analysts, and finance teams use this skill to draft structured research briefs and report outlines across macro, fixed income, company, strategy, and quantitative workflows. Outputs are intended as draft research material that must be reviewed by qualified professionals before use.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may direct agents toward external financial data tools, web search, and user-provided documents.

Mitigation: Use it only in environments where those data sources and tools are explicitly approved, and require source and cutoff-date review for generated research.

Risk: Generated allocation, trading, or investment language may be mistaken for final advice.

Mitigation: Treat all outputs as draft research and require review by qualified professionals before investment or business decisions.

Risk: Recurring report or cron-style examples could create unattended reporting behavior.

Mitigation: Enable scheduled use only with a visible schedule, duration, cancellation path, and human review process.

Risk: Reports or exports may include sensitive financial or user-provided information.

Mitigation: Preview outputs before saving or sending, minimize data, and require explicit user confirmation for report delivery.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/gechengling/skills/investment-researcher-digital-employee)
- [Skill source artifact](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown research frameworks, report outlines, tables, and illustrative code or shell-command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires authorized financial data access and human review before use, saving, delivery, or decisions.]

## Skill Version(s):

2.0.5 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
