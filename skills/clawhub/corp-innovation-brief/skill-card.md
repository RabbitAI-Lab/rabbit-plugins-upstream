## Description:

Generates Chinese company innovation and credit-analysis briefs from patent, paper, and public web data for bank lending review teams.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

Bank relationship managers, credit approvers, and risk-control staff use this skill to assess a company's technology innovation profile and generate a structured credit-review brief. It summarizes company background, business lines, core patent technologies, patent portfolio signals, market position, partnerships, and credit-review risk points.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill retrieves patent, paper, and public web information about companies, so report quality depends on source coverage and freshness.

Mitigation: Review cited sources and treat the generated brief as credit-review support rather than a final lending decision.

Risk: The optional export path can create local report files when the user chooses to export or runs the helper pipeline.

Mitigation: Confirm export intent before file creation and store generated reports only in approved workspaces.

Risk: The skill depends on PatSnap MCP and public web search for complete results.

Mitigation: Install and use it only in environments where the required PatSnap authorization and web-search access are configured.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yuanzhian-patsnap/skills/corp-innovation-brief)
- [PatSnap open platform](https://open.zhihuiya.com/)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Files, Configuration instructions, Guidance]

**Output Format:** [Markdown report with optional self-contained HTML export and supporting JSON data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The report is generated in simplified Chinese by default; HTML export is disclosed as optional and requires user confirmation.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
