## Description:

费用分摊表逐项核对（逐行算术、合计勾稽、重复与空缺检测），每条结论引用原文行号。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance, cashier, and property operations staff use this skill during month-end reconciliation to check utility allocation tables for arithmetic mismatches, total-line inconsistencies, duplicate tenants, and blank or placeholder fields. It is intended for local review of copied table text and cites source lines for each finding.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The free checker is local, but documentation and normal output steer users toward a paid external SkillPay package and purchase flow.

Mitigation: Do not paste or execute the purchase prompt, run npx @latest installers, authorize wallets, or install paid packages unless the user intentionally wants that workflow and independently verifies the package, publisher, and payment terms.

Risk: The free release omits several allocation checks that users may expect from a complete reconciliation workflow.

Mitigation: Treat results as limited to the listed free checks and review any withheld or out-of-scope checks before relying on the output for business decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/utility-allocation-check-free)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON-style check results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local Node.js execution; findings include severity, category, source line, evidence text, and advice when checks run successfully.]

## Skill Version(s):

1.0.8 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
