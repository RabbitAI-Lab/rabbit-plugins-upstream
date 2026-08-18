## Description:

Identify candidate patent white-space signals from a patent map, technology-effect matrix, technology-application matrix, cluster map, roadmap, or sparse portfolio region; test whether the signal is a search or classification artifact; assess the value of the underlying problem; diagnose route breaks and primary contradictions; and propose two to four principle-level resolution directions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

Innovation teams, patent analysts, and IP professionals use this skill to explore sparse or unusual areas in patent maps as hypotheses, test obvious false-space explanations, assess whether an underlying problem appears valuable, and generate principle-level resolution directions. The skill excludes technical feasibility validation, commercial validation, FTO, patentability analysis, and filing-strategy justification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Patent-map, portfolio, and business-context details may be sensitive when included in the generated local HTML report.

Mitigation: Store generated reports only in an approved workspace, review report contents before sharing, and avoid including confidential inputs unless the deployment environment is authorized for them.

Risk: Optional patent-data retrieval may contact PatSnap MCP services and expand the evidence used in the analysis.

Mitigation: Use MCP retrieval only after user authorization and disclose which patent checks were executed or not executed.

Risk: Sparse patent-map areas can be artifacts of search terms, classification, family handling, time windows, database coverage, or non-patent protection.

Mitigation: Run the skill's false-space checks, show supporting and opposing explanations, and treat white-space findings as hypotheses until independently validated.

Risk: Resolution directions may be mistaken for validated inventions, filing recommendations, or commercial opportunities.

Mitigation: Keep the stated exclusions visible: no technical feasibility validation, commercial validation, FTO, patentability analysis, or filing-strategy justification.

## Reference(s):

- [Candidate patent white-space evaluation framework](references/evaluation-framework.md)
- [Patent white-space output templates](references/output-templates.md)
- [PatSnap Advanced Patent Search MCP server](https://open.patsnap.com/marketplace/mcp-servers/patent-search)
- [PatSnap Patent Briefing MCP server](https://open.patsnap.com/marketplace/mcp-servers/patent-briefing)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Files, Guidance]

**Output Format:** [Markdown analysis with tables, confirmation prompts, and a self-contained HTML report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes two mandatory user confirmation gates and labels observed facts, retrieved evidence, inference, uncertainty, and recommendation.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
