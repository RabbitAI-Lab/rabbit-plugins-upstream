## Description:

Checks insurance agency fee and commission settlement tables for row-level arithmetic, total reconciliation, duplicate rows, blanks, and negative amount or rate values, with findings tied back to the supplied table text.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance, cashier, and insurance agency operations staff use this skill during monthly close or reconciliation to check insurance agency fee and commission settlement tables. It helps verify table arithmetic, totals, duplicate rows, missing required fields, and negative values, while declining to conclude when the submitted table is insufficient.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The artifact promotes an unpinned external installer and a paid SkillPay workflow.

Mitigation: Use the free local checker for its stated table checks, and do not run the installer or start the paid workflow until the package source, exact version, installer behavior, and payment flow are independently verified.

Risk: The checker only covers the free subset of settlement checks and lists additional checks that are not executed.

Mitigation: Treat the output as limited to the executed local checks, review the checks-not-run list, and do not rely on the skill for withheld checks or broader accounting, contract, or regulatory judgments.

Risk: Insufficient or malformed settlement table input can prevent reliable conclusions.

Mitigation: Provide the required table headers and rows, and treat insufficient-input output as no conclusion rather than evidence that no issues were found.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/insurance-agency-fee-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)
- [Purchase information referenced by artifact](https://chenqg618.github.io/compliance-skills/buy.html)
- [SkillPay shelf referenced by artifact](https://skillpay.alipay.com/public/tokendidi)

## Skill Output:

**Output Type(s):** [text, json, shell commands, guidance]

**Output Format:** [Human-readable text or JSON results from local command execution]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs executed checks, checks not run, source-cited findings, summary counts, local execution status, and insufficient-input guidance when required table fields are missing.]

## Skill Version(s):

1.0.2 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
