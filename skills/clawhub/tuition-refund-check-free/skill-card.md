## Description:

Checks tuition refund tables by recalculating consumed tuition, refundable amount, actual refund difference, totals, duplicates, and blanks, with source line references for each finding.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Education and training finance or operations staff use this skill to check pasted refund tables locally before communicating refund balances or disputes. It helps identify arithmetic mismatches, total-row errors, duplicate students, and missing required fields, but it does not decide legal or contractual refund terms.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release asks an AI assistant to install unpinned payment tooling and initiate a specific purchase workflow for the full version.

Mitigation: Do not use the purchase prompt unless you intend to start that purchase; verify the package, merchant, product, and newly installed skill, and require the user to confirm any wallet authorization or payment.

Risk: The local checker reads tuition refund tables that may contain student and financial information.

Mitigation: Run the free checker only when local processing of that table is acceptable, and avoid including unnecessary sensitive details in the input.

Risk: The free version omits several refund checks and does not evaluate legal or contractual refund terms.

Mitigation: Treat passing output as scoped arithmetic and table-consistency evidence only, and review omitted or out-of-scope checks before relying on the result.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/tuition-refund-check-free)
- [Full-version purchase instructions referenced by the release](https://chenqg618.github.io/compliance-skills/buy.html)
- [SkillPay shelf referenced by the release](https://skillpay.alipay.com/public/tokendidi)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown guidance with shell commands; the local checker can emit human-readable text or JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings cite source line numbers; insufficient input returns missing fields instead of a conclusion.]

## Skill Version(s):

1.0.9 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
