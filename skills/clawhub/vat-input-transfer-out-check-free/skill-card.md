## Description:

用于本地核对进项税额转出计算表的逐行复算、合计勾稽、重复与空缺问题，并让每条结论引用原文依据。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and accounting users run this skill during monthly closing, reconciliation, or inventory checks to verify VAT input transfer-out calculation tables. It helps identify table arithmetic issues, period totals that do not tie, duplicate rows, blank required fields, and negative amounts or rates within the free-version scope.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release evidence security summary flags that the local checker also points users and agents toward an under-scoped external install-and-purchase workflow.

Mitigation: Use the skill only for the bundled local free VAT checker unless the package, publisher, version, and payment flow are separately verified; do not let an agent run the documented npx payment/install command or follow newly installed skill instructions without that verification.

Risk: The free version intentionally omits several checks that are listed as withheld, so a low-finding result can be mistaken for a complete VAT compliance review.

Mitigation: Treat results as limited to the executed checks, review the checks_not_run and checks_out_of_scope fields, and avoid presenting no findings as full tax or filing assurance.

Risk: The artifact states that it does not decide whether a specific input tax item must be transferred out under tax rules.

Mitigation: Use findings as table arithmetic and consistency support only, and route tax-law or filing-position questions to qualified tax review.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/vat-input-transfer-out-check-free)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Markdown/text guidance with optional JSON result output from the local Node.js runner]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs line-cited findings, executed and withheld check lists, insufficient-input messages when required table data is missing, and scope notes for checks that are not performed.]

## Skill Version(s):

1.0.3 (source: release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
