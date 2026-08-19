## Description:

Builds a company-level small RNA patent landscape from patent-number lists, producing local patent text, structured workbook analysis, technical tags, and an interactive timeline dashboard.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

Patent analysts, IP teams, and RNA therapeutics strategy teams use this skill to convert patent-number lists into company-level small RNA portfolio analysis, including strategy workbooks and exploratory HTML timeline dashboards.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Patent lists and fetched patent text may be sensitive project data.

Mitigation: Use a dedicated project directory and review sharing permissions before storing or exporting generated Markdown, workbook, and dashboard artifacts.

Risk: Rerunning the scaffold can replace landscape_config.json in the selected root.

Mitigation: Check the target root before rerunning the scaffold and preserve any customized configuration outside the generated project if needed.

Risk: Patent retrieval, family data, legal status, and claim substitution can be incomplete or tool-dependent.

Mitigation: Verify source patent records and legal-status fields before relying on the workbook or dashboard for IP strategy decisions.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/yuanzhian-patsnap/skills/small-rna-patent-landscape)
- [HTML Dashboard Specification](references/html-dashboard.md)
- [Small RNA Patent Tag Taxonomy](references/tag-taxonomy.md)
- [Workbook Schema](references/workbook-schema.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with generated local files such as Markdown patent texts, JSON or CSV intermediates, XLSX workbooks, and standalone HTML dashboards]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates project folders for patent_markdowns and outputs/patent_analysis; outputs may use Chinese customer-facing labels while preserving source patent text unless translation is requested.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
