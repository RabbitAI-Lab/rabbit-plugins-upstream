## Description:

Checks SaaS subscription revenue-recognition tables locally for row-level arithmetic, totals, duplicates, blanks, and negative values, with findings tied to source lines.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and accounting teams use this skill during month-end reconciliation to check SaaS subscription revenue-recognition tables for mechanical arithmetic, totals, duplicate rows, missing fields, and negative values. It supports table checks and does not replace accounting judgment for when or how revenue should be recognized.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes prompts and links that direct users or agents toward an external paid install and purchase workflow beyond the free local checker.

Mitigation: Use the free checker only for local table checks, prefer `--json` output, and do not execute upgrade, purchase, or `npx ... @latest` instructions unless the user separately trusts the payment package and intends to buy it.

Risk: The free checker intentionally omits several checks, so a clean result may not cover all revenue-recognition table issues.

Mitigation: Review the reported checks_not_run and checks_out_of_scope before relying on results, and route accounting judgments or omitted checks to qualified review.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/saas-revenue-recognition-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)
- [Paid upgrade instructions referenced by artifact](https://chenqg618.github.io/compliance-skills/buy.html)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Human-readable console text or structured JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local Node.js execution; findings cite source lines when checks run.]

## Skill Version(s):

1.0.3 (source: evidence release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
