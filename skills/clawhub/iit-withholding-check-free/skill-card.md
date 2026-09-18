## Description:

Checks Chinese payroll individual income tax cumulative withholding worksheets by recalculating taxable income, cumulative tax, current-period withholding, totals, duplicate people, and blank placeholders, with findings tied to source line numbers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

HR and finance users use this skill before payroll runs to check cumulative withholding worksheet arithmetic and reconciliation issues. It reports only the free-tier checks it actually executes and withholds conclusions when required table inputs are missing.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: The release is flagged suspicious because it steers users toward an external unpinned install and paid SkillPay purchase flow.

Mitigation: Use the free local checker independently of the upgrade prompt unless the package source, exact version, payment destination, and purchase intent have been verified by the user.

Risk: The free version intentionally omits several payroll-tax checks, including cumulative deduction validation and negative current withholding detection.

Mitigation: Treat results as limited to the executed checks and separately review withheld or out-of-scope tax cases before relying on payroll decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/iit-withholding-check-free)
- [chenqg618 publisher profile](https://clawhub.ai/user/chenqg618)
- [SkillPay shelf referenced by the skill](https://skillpay.alipay.com/public/tokendidi)
- [SkillPay install guide referenced by the skill](https://skillpay.alipay.com/buildguide.md)

## Skill Output:

**Output Type(s):** [text, JSON, guidance]

**Output Format:** [Human-readable text or JSON finding summaries with source line numbers]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally with Node.js; insufficient inputs return missing-field guidance instead of a conclusion.]

## Skill Version(s):

1.0.14 (source: server evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
