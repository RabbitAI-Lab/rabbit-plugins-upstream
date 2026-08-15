## Description:

Generates editable HTML patent technology panorama reports from uploaded patent and technology-breakdown spreadsheets, including technology overview, branch, competitor, risk, and patent layout analyses.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

External analysts, patent strategists, and developers use this skill to process patent spreadsheets and generate editable HTML reports for technology landscape, competitor, FTO risk, and portfolio planning analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Patent spreadsheets and competitive-intelligence data may contain confidential business information.

Mitigation: Confirm user intent and authorization before processing files or using any PatSnap/Zhihuiya MCP integration.

Risk: Generated patent-risk and layout recommendations can be mistaken for legal advice.

Mitigation: Treat outputs as analytical drafts and have qualified reviewers validate FTO, infringement, and portfolio decisions before action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yuanzhian-patsnap/skills/patent-panorama-analysis)
- [Zhihuiya open platform](https://open.zhihuiya.com/)
- [ECharts CDN](https://cdn.jsdelivr.net/npm/echarts@5/dist/echarts.min.js)
- [Data analysis guide](references/data_analysis_guide.md)
- [Report structure guide](references/report_structure.md)
- [UI style guide](references/ui_style_guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, configuration, guidance]

**Output Format:** [Markdown guidance and generated editable HTML report code]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reads user-provided Excel spreadsheets and may guide setup for the Zhihuiya MCP integration when account authorization is not configured.]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
