## Description:

门店销售与成本毛利表逐项核对（销售额与收款勾稽、成本差异复算、毛利率逐行复算、损耗率超限、重复与空缺），每条结论引用原文行号。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

门店财务、会计和店长 use this skill during monthly closing, operating analysis, and inventory-difference review to check a store sales-and-cost gross margin table before reporting or audit review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The interface and domain guidance are primarily Chinese, which can make review harder for teams that do not read Chinese.

Mitigation: Use a reviewer who can validate the Chinese prompts, output labels, and finance terminology before operational use.

Risk: Comments and user-facing text mention anonymous usage statistics, while the inspected security evidence says those comments are stale and the behavior is not implemented.

Mitigation: Rely on the current inspected release behavior and re-scan future versions if telemetry-related code is added.

Risk: The skill checks table consistency only and does not validate pricing policy, tax treatment, physical loss causes, inventory systems, or source-system exports.

Mitigation: Treat findings as reconciliation signals and confirm accounting policy, inventory records, and source-system data outside the skill.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/store-gross-margin-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands; CLI output can be human-readable text or JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings cite source row numbers; insufficient input returns missing fields instead of conclusions.]

## Skill Version(s):

1.0.4 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
