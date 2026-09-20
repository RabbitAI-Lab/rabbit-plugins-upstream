## Description:

现金盘点表逐项核对（逐行复算、合计勾稽、重复与空缺检测），每条结论引用原文行号。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Store operations, finance, and audit staff use this skill to check cash-count tables for arithmetic inconsistencies, duplicate shifts, blank fields, and mismatch between shortage/overage type and sign. It is intended for local reconciliation support, not for determining fraud, legal liability, or a complete audit outcome.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A clean result could be mistaken for a full audit or fraud determination.

Mitigation: Use the output only as a deterministic cash-count table check and review audit evidence, cash handling procedures, and out-of-scope items separately.

Risk: The free version explicitly omits several checks, including threshold checks and negative cash field checks.

Mitigation: Review the reported withheld checks before relying on a result, and run additional checks when those controls matter.

Risk: Cash-count tables may contain sensitive operational data.

Mitigation: Provide only the cash-count data intended for analysis and avoid adding unrelated confidential information.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/cash-count-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Plain text or JSON findings with cited source line numbers]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally; reports executed and withheld checks; insufficient input returns missing fields instead of a conclusion.]

## Skill Version(s):

1.0.56 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
