## Description:

Provides a template and workflow for planning a 13-week US small-business cash-flow forecast from user-supplied bank and accounts-receivable data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rapidworker1](https://clawhub.ai/user/rapidworker1)

### License/Terms of Use:

MIT-0

## Use Case:

US small-business owners, controllers, and fractional CFOs use the workflow and template to organize weekly cash inflows, outflows, timing assumptions, and potential cash shortfalls over a 13-week horizon.

### Deployment Geography for Use:

United States

## Known Risks and Mitigations:

Risk: The supplied script does not implement the promised weekly forecast calculations.

Mitigation: Do not rely on its output for payroll, tax, or funding decisions until weekly calculations are implemented and independently checked.

Risk: Missing or invalid amounts are silently replaced with zero.

Mitigation: Validate all required financial inputs independently and resolve missing or invalid values before using any output.

Risk: Bank and accounts-receivable exports contain sensitive financial information.

Mitigation: Keep financial exports private and share only what is necessary.

Risk: The optional Windows application is unsigned and is unnecessary for the Python workflow.

Mitigation: Avoid the optional application unless it has undergone a separate review.

## Reference(s):

- [US payment timing and payroll rules that change a forecast](references/cash-flow-basics.md)
- [ClawHub skill page](https://clawhub.ai/rapidworker1/skills/cash-flow-forecast)
- [Publisher homepage](https://github.com/rapidworker1)

## Skill Output:

**Output Type(s):** [Markdown, Configuration]

**Output Format:** [Markdown forecast summary and YAML input template]

**Output Parameters:** [13 weekly periods]

**Other Properties Related to Output:** [Uses user-supplied financial data; output is not a financial statement, tax position, or guaranteed result.]

## Skill Version(s):

1.0.7 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
