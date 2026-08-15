## Description:

Discovers candidate patent white spaces from patent maps, evaluates problem value, diagnoses key contradictions behind the white space, and proposes contradiction-resolution directions while requiring user confirmation before deeper analysis stages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

Patent analysts, innovation teams, and strategy users use this skill to identify and prioritize patent-map white space, assess whether the underlying problem is valuable, and produce a structured contradiction analysis with candidate resolution directions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may use an authorized PatSnap/Zhihuiya MCP connection for patent data.

Mitigation: Confirm the user is authorized to access the patent data source before using it for an analysis.

Risk: The generated HTML report may contain confidential business or patent-analysis material provided during the session.

Mitigation: Avoid including confidential material unless it is appropriate for that information to appear in the session report.

## Reference(s):

- [Candidate White Space Evaluation Framework](artifact/references/evaluation-framework.md)
- [Output Templates](artifact/references/output-templates.md)
- [ClawHub Skill Page](https://clawhub.ai/yuanzhian-patsnap/skills/discover-patent-white-space-opportunities)
- [Zhihuiya Open Platform](https://open.zhihuiya.com/)

## Skill Output:

**Output Type(s):** [text, markdown, HTML files, guidance]

**Output Format:** [Markdown analysis with structured tables and a self-contained HTML report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires explicit user confirmation before candidate deep-dive and before contradiction diagnosis.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
