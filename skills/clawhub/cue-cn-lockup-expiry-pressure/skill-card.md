## Description:

Organizes one A-share issuer's upcoming restricted-share unlocks into a date-ordered calendar with announcement sources, share counts, sourced ownership ratios, and documented cost prices.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huhoo](https://clawhub.ai/user/huhoo)

### License/Terms of Use:

MIT-0

## Use Case:

A-share analysts and research users use this skill to track upcoming lockup expiries for one stock and prepare a source-anchored calendar of dates, holder types, share counts, ownership ratios, and stated issue or grant prices. It does not provide price forecasts or trading recommendations.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: The scan reports undeclared remote tool discovery.

Mitigation: Review the remote discovery path and allow only the tools needed for the task before enabling the skill.

Risk: The scan reports that calculated financial percentages may be permitted despite the stated policy.

Mitigation: Check each ratio against its source documents; label any calculated ratio and its method clearly, then have a reviewer verify it.

Risk: The installation source is not pinned to a specific revision.

Mitigation: Install a reviewed, version-pinned release and verify its contents before use.

Risk: One fixture script was only partly inspected, leaving the scan incomplete.

Mitigation: Complete a full inspection of all artifact files before installation.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/huhoo/skills/cue-cn-lockup-expiry-pressure)
- [Cue MCP catalog](https://cuecue.cn/api/mcp-catalog)

## Skill Output:

**Output Type(s):** [Markdown, Text]

**Output Format:** [Chinese seven-section lockup-expiry note with source anchors and a dated calendar]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Records future unlock dates, holder types, share counts, sourced ownership ratios, cost prices stated in source documents, and explicitly named missing information. No price forecasts or investment recommendations.]

## Skill Version(s):

0.1.1 (source: server-resolved release, SKILL.md frontmatter, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
