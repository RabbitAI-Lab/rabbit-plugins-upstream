## Description: <br>
Audits datasets for missingness, duplicates, outliers, type and range errors, consistency, freshness, and produces a prioritized fix list. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mohitagw15856](https://clawhub.ai/user/mohitagw15856) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and data practitioners use this skill to review a dataset, schema, sample, or description before analysis and identify quality issues that could distort decisions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may generate plausible audit checks from limited dataset descriptions. <br>
Mitigation: Provide real schema, sample rows, source and freshness details, known issues, and intended use so the audit can ground findings in the available evidence. <br>
Risk: A data-quality report can be misleading if inferred issues are treated as confirmed defects. <br>
Mitigation: Use the concrete SQL or pandas-style checks in the output to confirm each issue before changing data or relying on conclusions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/mohitagw15856/skills/data-quality-audit) <br>
- [Skill homepage](https://mohitagw15856.github.io/pm-claude-skills/skill/data-quality-audit.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, guidance] <br>
**Output Format:** [Markdown structured report with scorecards, issue lists, SQL or pandas-style checks, fix plan, and guardrails.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Findings are more grounded when the user provides schema, sample rows, source, freshness, known issues, and intended use.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
