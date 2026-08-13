## Description:

Identify candidate patent white-space signals from a patent map, technology-effect matrix, technology-application matrix, cluster map, roadmap, or sparse portfolio region; test whether the signal is a search or classification artifact; assess the value of the underlying problem; diagnose route breaks and primary contradictions; and propose two to four principle-level resolution directions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

External users and patent-strategy analysts use this skill to examine patent-map sparsity, separate apparent gaps from defensible white-space hypotheses, and generate principle-level resolution directions. The workflow keeps legal, commercial, patentability, freedom-to-operate, and filing-strategy validation out of scope.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow may retain confidential patent maps or strategy material in a local HTML report.

Mitigation: Review the generated whitespace-[topic-keyword]-report.html file and remove it from the workspace when retention is not intended.

Risk: External patent retrieval can disclose search intent or query material to PatSnap MCP tools.

Mitigation: Authorize PatSnap MCP retrieval only when external patent-tool queries are intended; otherwise continue from user-provided map evidence and mark patent-level validation as not executed.

Risk: Sparse patent-map areas can be mistaken for validated opportunities.

Mitigation: Use the skill's required false-space checks, evidence separation, and confirmation gates, and keep technical, commercial, patentability, FTO, and filing validation out of scope.

## Reference(s):

- [Candidate patent white-space evaluation framework](references/evaluation-framework.md)
- [Patent white-space output templates](references/output-templates.md)
- [PatSnap Advanced Patent Search MCP server](https://open.patsnap.com/marketplace/mcp-servers/patent-search)
- [PatSnap Patent Briefing MCP server](https://open.patsnap.com/marketplace/mcp-servers/patent-briefing)

## Skill Output:

**Output Type(s):** [text, markdown, code, configuration, guidance, files]

**Output Format:** [Markdown analysis with tables, confirmation prompts, and a self-contained HTML report file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires explicit user confirmation at candidate selection and problem-value checkpoints; final HTML report is named like whitespace-[topic-keyword]-report.html.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
