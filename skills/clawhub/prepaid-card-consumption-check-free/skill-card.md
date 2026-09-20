## Description:

预付卡消费核销表逐项核对（逐行复算、合计勾稽、重复与空缺检测），每条结论引用原文。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and operations staff use this skill during monthly close, reconciliation, or inventory checks to validate prepaid card consumption tables. It recalculates row arithmetic, totals, duplicate rows, missing fields, and negative transaction amounts, and it reports each finding with source evidence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The checker may be mistaken for professional accounting or legal advice.

Mitigation: Use the output as an arithmetic consistency aid and have qualified reviewers apply the organization's accounting policy, contract terms, and legal requirements.

Risk: The skill does not inspect bank records, POS systems, or withheld paid-version checks.

Mitigation: Reconcile source systems separately and treat unexecuted checks as out of scope for this free release.

Risk: Input tables may contain sensitive prepaid-card or member information.

Mitigation: Run the Node-based checker in a controlled local environment and limit input files to the records needed for reconciliation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/prepaid-card-consumption-check-free)

## Skill Output:

**Output Type(s):** [analysis, text, json, shell commands, guidance]

**Output Format:** [Human-readable text or JSON findings from a local Node.js command]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings cite source rows and evidence; insufficient input returns missing requirements instead of a conclusion.]

## Skill Version(s):

1.0.41 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
