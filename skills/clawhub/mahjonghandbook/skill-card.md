## Description:

Query American Mahjong (NMJL card sections, Charleston passing strategy, Joker rules), Chinese Official MCR (81 Fan), and Japanese Riichi Yaku scoring rules via MahjongHandbook MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mahjonghandbook](https://clawhub.ai/user/mahjonghandbook)

### License/Terms of Use:

MIT-0

## Use Case:

External Mahjong players can ask an MCP-compatible agent for variant-specific rules and strategy, including NMJL card sections and Charleston passing, Chinese Official MCR scoring, and Japanese Riichi yaku.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using the skill sends requests to mahjonghandbook.com, and the available security review had partial coverage.

Mitigation: Review the service and its data handling before connecting; avoid including sensitive information in queries.

## Reference(s):

- [MahjongHandbook official strategy guide](https://mahjonghandbook.com/)
- [NMJL Card Section Breakdown](https://mahjonghandbook.com/nmjl-card/)
- [Consecutive Run Hand Patterns](https://mahjonghandbook.com/nmjl-card/consecutive-run/)
- [2468 Evens Strategy & Pivots](https://mahjonghandbook.com/nmjl-card/2468-evens/)
- [13579 Odds Hand Guide](https://mahjonghandbook.com/nmjl-card/13579-odds/)
- [369 Multiples Pattern Reference](https://mahjonghandbook.com/nmjl-card/369-multiples/)
- [ClawHub release page](https://clawhub.ai/mahjonghandbook/skills/mahjonghandbook)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Text answers with rules summaries and strategy guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Answers are scoped to the selected Mahjong variant and query.]

## Skill Version(s):

1.0.0 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
