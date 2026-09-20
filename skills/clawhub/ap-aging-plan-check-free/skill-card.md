## Description:

应付账款账龄与付款计划表逐项核对，执行逐行复算、合计勾稽、重复与空缺检测，并为每条结论引用原文依据。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and accounts payable users use this skill during monthly closing, reconciliation, or payment planning to check AP aging and payment-plan tables for arithmetic mismatches, duplicate suppliers, missing fields, and withheld free-tier checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The free version intentionally omits several accounting checks, so users may mistake a clean result for a complete audit.

Mitigation: State that the result covers only the executed free-tier checks and require users to review the omitted checks before relying on the output.

Risk: Insufficient or malformed AP table input can prevent the tool from making a reliable finding.

Mitigation: Return an insufficient-input status with the missing columns or required table content instead of producing a pass or fail conclusion.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/ap-aging-plan-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [text, json, shell commands, guidance]

**Output Format:** [Human-readable text or JSON from a local Node.js command]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings include status, executed checks, omitted checks, line references, summary counts, and insufficient-input guidance.]

## Skill Version(s):

1.0.58 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
