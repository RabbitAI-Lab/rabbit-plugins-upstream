## Description:

Composes account-grouping report recipes and builds grouped account summary reports from bundled account rows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and account operations teams use this skill to turn an account report request into a structured grouping recipe and then build a grouped account summary with selected measures and columns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Account rows used for reporting may contain sensitive business data.

Mitigation: Confirm the rows are appropriate to share with the skill and avoid including credentials, private files, or unnecessary account details.

Risk: Grouped report results can be misleading if the report request, grouping recipe, or bundled account rows are incomplete or incorrect.

Mitigation: Review the generated report predicate and grouped summary before relying on the output for business decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wxt-ai/skills/account-group-report)
- [ClawHub publisher profile](https://clawhub.ai/user/wxt-ai)
- [Artifact skill definition](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Structured text or markdown containing an account-report recipe and grouped account summary.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces report_predicate for recipe planning and group_report for grouped account summaries.]

## Skill Version(s):

1.0.7 (source: frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
