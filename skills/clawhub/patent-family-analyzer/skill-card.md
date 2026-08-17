## Description:

Patent Family Analyzer helps patent analysts retrieve and compare patent-family members from a single patent number or URL and generate an interactive HTML report covering family structure, technical elements, topic coverage, evolution, and risks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

Patent analysts use this skill to examine a patent family from one patent number or PatSnap/Zhihuiya URL, compare family members, and prepare a structured interactive report for technical and protection-strategy review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Patent queries and report contents may involve confidential search topics or analysis results.

Mitigation: Use the skill only with an approved PatSnap/Zhihuiya MCP setup and review generated HTML reports before sharing them.

Risk: The skill depends on PatSnap MCP access for live patent-family retrieval and full analysis.

Mitigation: Confirm account authorization and MCP tool availability before relying on the report; without configuration, treat outputs as an analysis framework only.

Risk: Patent-family analysis may be incomplete when full text is unavailable or the family contains more than 20 members.

Mitigation: Check report notes for abstract-only analysis and family-size limits, and verify important conclusions against source patent records.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yuanzhian-patsnap/skills/patent-family-analyzer)
- [Zhihuiya Open Platform](https://open.zhihuiya.com/)

## Skill Output:

**Output Type(s):** [Analysis, Files, Code, Guidance]

**Output Format:** [Self-contained interactive HTML report, with analysis guidance when the PatSnap MCP service is not configured.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The report can include a family tree, patent analysis cards, topic matrix, evolution timeline, report metadata, and patent links; detailed analysis is limited to up to 20 family members.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
