## Description:

Checks advance receipt and revenue recognition ledgers for row arithmetic, total reconciliation, duplicate customers, and blank or placeholder fields, with findings tied to source rows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and accounting staff use this skill during month-end closing, reconciliation, or inventory checks to review advance receipt ledgers before continuing downstream accounting work. It performs the free local checks only and does not decide revenue recognition timing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill documentation and normal output promote an external paid-edition install and purchase flow.

Mitigation: Use the free local checker without following the paid-edition prompt unless the external package, installed skill, and payment steps have been independently reviewed.

Risk: The free edition omits several checks that may matter for complete accounting review.

Mitigation: Treat results as limited to the listed free checks and review withheld checks and out-of-scope items before relying on the output.

Risk: Materials with missing required columns or insufficient ledger text produce no accounting conclusion.

Mitigation: Provide a ledger with recognized headers for customer, opening balance, current receipts, recognized revenue, and closing balance, then review insufficient-input messages before rerunning.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/advance-receipt-check-free)
- [chenqg618 publisher profile](https://clawhub.ai/user/chenqg618)
- [Complete-edition purchase information](https://chenqg618.github.io/compliance-skills/buy.html)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and optional JSON result output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local Node.js execution; reports executed checks, withheld checks, findings, summary, and insufficient-input guidance.]

## Skill Version(s):

1.0.8 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
