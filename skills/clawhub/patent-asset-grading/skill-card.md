## Description:

Patent Asset Grading helps agents batch-evaluate patent identifiers by retrieving patent data through the PatSnap MCP service, mapping patents to industries by IPC code, scoring five value dimensions, and producing Word or Excel grading reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to assess batches of patent application, publication, or grant numbers for portfolio review. It generates per-patent grades, dimension scores, scoring rationale, and disposition recommendations for decision support.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Patent identifiers are sent to the referenced patent-data MCP service under the user's account authorization.

Mitigation: Install and run the skill only where this data sharing is acceptable, and confirm MCP account authorization before live lookup.

Risk: Generated patent grades may be used as legal or valuation conclusions rather than decision-support outputs.

Mitigation: Review generated ratings, rationales, and recommendations with qualified patent, legal, or valuation reviewers before relying on them.

## Reference(s):

- [PatSnap Open Platform](https://open.zhihuiya.com/)
- [ClawHub skill page](https://clawhub.ai/yuanzhian-patsnap/skills/patent-asset-grading)

## Skill Output:

**Output Type(s):** [files, guidance]

**Output Format:** [Excel .xlsx or Word .docx report files with structured patent grading results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports batches up to 50 patent identifiers per run; live patent lookup requires configured PatSnap MCP account authorization.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
