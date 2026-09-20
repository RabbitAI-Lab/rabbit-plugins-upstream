## Description:

应付账款保理与贴现表逐项核对（逐行复算、合计勾稽、重复与空缺检测），每条结论引用原文。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and treasury users can use this skill during month-end close, reconciliation, or inventory review to check AP factoring and discounting tables. It recalculates line items and totals, flags duplicates and missing fields, and cites the source lines used for each finding.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: AP factoring and discounting data may contain sensitive business information.

Mitigation: Provide only files intended for inspection and run the local checker in a trusted environment.

Risk: The free version omits some checks that may matter for accounting review.

Mitigation: Review the listed checks that were not run and perform any required additional review before relying on the result.

Risk: Incomplete or malformed table input can prevent a supported conclusion.

Mitigation: Include the required table headers and line items, and treat insufficient-input output as no conclusion.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/ap-factoring-check-free)
- [ClawHub publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [text, json, guidance]

**Output Format:** [Human-readable reconciliation report or JSON result with checks, findings, summary, and scope.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally with Node.js standard library; reads a user-provided AP factoring table and does not use network, credentials, or persistence according to evidence.security.]

## Skill Version(s):

1.0.59 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
