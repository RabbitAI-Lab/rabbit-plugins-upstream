## Description:

附加税费计算表逐项核对，执行逐行复算、合计勾稽、重复与空缺检测，并为每条结论引用原文行号。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

External finance, tax, and accounting users use this skill to check VAT surtax worksheets for recomputation errors, total-row mismatches, duplicate periods, and missing required fields. The free edition runs local deterministic checks and reports missing inputs instead of drawing unsupported conclusions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence flags an optional paid upgrade flow that asks an agent to run an unpinned external installer and follow newly installed instructions.

Mitigation: Do not let an agent run the installer, follow new paid-upgrade instructions, initiate payment, or approve wallet steps unless the package, merchant, product, and authorization flow have been independently verified.

Risk: The local checker processes worksheet text provided by the user.

Mitigation: Use the free checker only when running the bundled local Node script on that worksheet text is acceptable for the user's data handling requirements.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/surtax-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)
- [Optional paid edition shelf](https://skillpay.alipay.com/public/tokendidi)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Plain text or JSON findings with worksheet line references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally with bundled Node scripts; material is not sent over the network by the free checker.]

## Skill Version(s):

1.0.3 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
