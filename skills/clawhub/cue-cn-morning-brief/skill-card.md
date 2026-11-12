## Description:

Creates a point-in-time A-share pre-market brief with five market slots and three covered-instrument slots, each anchored to a source and retrieval date, with reconciled coverage and human-only judgments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huhoo](https://clawhub.ai/user/huhoo)

### License/Terms of Use:

MIT-0

## Use Case:

Users preparing an overnight or pre-market brief for a list of A-share instruments can use the skill to assemble five market slots and three instrument slots, attach sources and retrieval dates, and reconcile the reported coverage against the slot table. It leaves market and instrument judgments for a human.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan reports concerns about MCP tool discovery, privacy and scope, and incomplete analysis of one referenced script.

Mitigation: Before installing, review the skill’s external MCP requests and its handling of announcement URLs and local paths; treat the incomplete scan as inconclusive.

Risk: The skill can use supplied announcement titles and local files when CUE_API_KEY is absent, and those inputs may provide incomplete coverage.

Mitigation: Check each filled slot against its cited source and retrieval date, and name every slot that was not obtained.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/huhoo/skills/cue-cn-morning-brief)
- [Cue MCP catalog](https://cuecue.cn/api/mcp-catalog)

## Skill Output:

**Output Type(s):** [Markdown, Guidance]

**Output Format:** [Structured Markdown brief with an eight-slot coverage table and dated source anchors]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports filled and missing slots against the fixed eight-slot table; leaves judgments marked for human review. Source authority and data freshness require human verification.]

## Skill Version(s):

0.1.0 (source: frontmatter, ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
