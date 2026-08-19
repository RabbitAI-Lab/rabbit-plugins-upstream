## Description:

Generates self-contained Chinese HTML inventor profile reports that analyze patent data for a named inventor and organization, including innovation capability ratings, patent evidence, risk sections, and credit-support guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

External users such as bank credit managers, HR teams, investors, and patent-data analysts use this skill to generate HTML reports that frame patent data as an inventor's innovation capability profile. The reports support review of technical output, leadership, influence, asset risks, and credit-style recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reports may be used for credit, hiring, investment, or other consequential decisions, where misleading ratings or recommendations could affect people or organizations.

Mitigation: Require human review before using report conclusions in consequential decisions, and treat the generated ratings as decision support rather than a standalone determination.

Risk: Conflicting data-collection instructions could produce incomplete or sample-based metrics while the report presents formal inventor ratings.

Mitigation: Require full paginated data collection for all metrics and label any capped or sample-based results as incomplete before relying on the report.

Risk: Generated report or progress files may retain personal names and patent-profile details.

Mitigation: Store and retain generated files only in environments where keeping those personal details is acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yuanzhian-patsnap/skills/patent-inventor-profile-report)
- [Data collection steps](artifact/references/data_collection_steps.md)
- [Key data summary specification](artifact/references/key_data_summary_spec.md)
- [Report design specification](artifact/references/report_design_spec.md)
- [PatSnap open platform](https://open.zhihuiya.com/)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Code, Files, Configuration guidance]

**Output Format:** [Self-contained HTML report with inline CSS and JavaScript, plus progress/report-generation guidance in Markdown when configuration is missing]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Report output is intended for @session/reports/[name]_profile_[date].html and depends on configured PatSnap/Zhihuiya MCP access for live patent data.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
