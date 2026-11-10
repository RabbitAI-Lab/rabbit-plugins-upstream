## Description:

Creates a five-part, disclosure-backed company briefing with recent financials, qualifying events, directly found risks, and three blank opinion slots for human completion.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huhoo](https://clawhub.ai/user/huhoo)

### License/Terms of Use:

MIT-0

## Use Case:

External users and analysts use this skill to prepare a concise, source-linked briefing on an A-share company before a client meeting or for a client brief. The opinion section remains blank for a person to complete.

### Deployment Geography for Use:

China (A-share companies)

## Known Risks and Mitigations:

Risk: The connection example sends CUE_API_KEY to a destination taken from a live catalog that this release does not verify.

Mitigation: Use user-supplied disclosures until the destination is confirmed as an approved HTTPS endpoint; review the exact skill revision before enabling the connection.

Risk: The document checker can pass pages that still have incorrect or misleading content, including missing citations, risk cautions, or completed opinion slots.

Mitigation: Manually verify citations and risk cautions, and confirm that all three opinion slots remain empty before sharing a page.

Risk: The permissions and behavior of companion Cue skills and live services were not assessed.

Mitigation: Review each companion skill and connected service before enabling it.

## Reference(s):

- [Cue API key setup](https://cuecue.cn/hub/api-key)
- [Cue MCP configuration](https://cuecue.cn/hub/mcp)
- [Cue omni-reader configuration](https://cuecue.cn/hub/omni-reader)
- [Cue MCP catalog](https://cuecue.cn/api/mcp-catalog)

## Skill Output:

**Output Type(s):** [Markdown, JSON Lines, JSON]

**Output Format:** [A Markdown briefing page with a JSONL source index, JSON evidence snapshots, and a Markdown progress log.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Five fixed sections per company; up to five companies; opinion slots remain blank for human completion.]

## Skill Version(s):

0.1.21 (source: frontmatter, server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
