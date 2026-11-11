## Description:

Registers balances, ageing, and provisions for inventory, receivables, and contract assets from Chinese listed-company filings, anchoring each item to its source sentence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huhoo](https://clawhub.ai/user/huhoo)

### License/Terms of Use:

MIT

## Use Case:

Financial analysts and filing-review teams use it to register inventory, accounts receivable, and contract asset balances, ageing, and provisions from A-share periodic reports. Each item is tied to filing text and source anchors; ratios absent from the filing are labeled as self-computed with their inputs, while quality judgments remain for human review.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: External service discovery and parsing raise privacy concerns, and scanner coverage of the skill is incomplete.

Mitigation: Before use with private report links or local files, confirm that external parsing and MCP discovery are acceptable and review the skill's behavior.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/huhoo/skills/cue-cn-working-capital-quality)
- [CUE MCP catalog](https://cuecue.cn/api/mcp-catalog)

## Skill Output:

**Output Type(s):** [Markdown, Text]

**Output Format:** [Five-section Markdown quality card with filing excerpts and source anchors]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Self-computed figures are labeled with numerator, denominator, and basis; filing-based judgments are left for human review.]

## Skill Version(s):

0.1.0 (source: frontmatter, CHANGELOG.md, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
