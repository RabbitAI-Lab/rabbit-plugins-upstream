## Description:

Turns a financial report's cash-flow statements into a source-linked record of cash flows, disclosed or explicitly self-calculated ratios, and indirect-method adjustments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huhoo](https://clawhub.ai/user/huhoo)

### License/Terms of Use:

MIT-0

## Use Case:

External users and financial analysts can use the skill to organize a company's operating, investing, and financing cash flows from a financial report into a Markdown register with quoted source lines, anchors, and references. It keeps disclosed ratios separate from self-calculations and records missing information without making fraud, distress, forecast, or investment-rating judgments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security summary labels the release suspicious, citing persistent local usage markers and concerns about validation reliability; it also says the scan is partial and its evidence is incomplete.

Mitigation: Review the first-run marker behavior and package contents before execution. Check reported figures and calculations against the original financial filing, and treat the automated checks as formatting and consistency aids rather than financial assurance.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/huhoo/skills/cue-cn-cash-flow-quality)
- [CUE MCP catalog](https://cuecue.cn/api/mcp-catalog)

## Skill Output:

**Output Type(s):** [Markdown, Text]

**Output Format:** [Markdown cash-flow register with sourced figures, ratios, basis notes, and information gaps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Figures are tied to quoted source text and anchors; ratios not stated in the source are marked as self-calculated with their inputs identified.]

## Skill Version(s):

0.2.0 (source: SKILL.md frontmatter, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
