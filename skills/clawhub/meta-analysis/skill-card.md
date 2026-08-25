## Description:

A bilingual R-based meta-analysis agent skill for clinical research workflows, including pairwise and network meta-analysis, effect-size conversion, heterogeneity and bias checks, systematic-review support, visualizations, and reproducible R code outputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[medstatstar](https://clawhub.ai/user/medstatstar)

### License/Terms of Use:

MIT

## Use Case:

Clinical researchers, biostatisticians, systematic-review authors, and medical evidence teams use this skill to plan and run meta-analysis workflows from natural-language requests, produce pooled estimates and plots, and receive reproducible R code and report artifacts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may transmit study data, summary statistics, analysis parameters, and selected IPD inputs to a Coze cloud service for computation.

Mitigation: Install and use it only when cloud processing is allowed for the data; avoid confidential clinical or sponsor data unless the organization approves the endpoint and data flow.

Risk: The release ships reusable service credentials and uses external service endpoints.

Mitigation: Treat bundled tokens as exposed shared credentials and review endpoint usage before deployment.

Risk: Optional PDF download, bug-report submission, and analysis output generation can create extra network calls or local files.

Mitigation: Use PDF fetch and bug-report submission only with user approval, and review generated workspace files before sharing or retaining them.

Risk: Meta-analysis outputs can affect clinical or regulatory interpretation if used without expert review.

Mitigation: Require qualified human review of pooled estimates, heterogeneity, bias checks, and generated reports before relying on the results.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/medstatstar/skills/meta-analysis)
- [Publisher Profile](https://clawhub.ai/user/medstatstar)
- [Project Homepage](https://github.com/medstatstar/meta-analysis)
- [README](README.md)
- [Chinese README](README_zh-CN.md)
- [Advanced API](references/advanced_api.md)
- [Data Templates](references/data_templates.md)
- [Interactive Menu](references/interactive_menu.md)
- [Language Policy](references/language_policy.md)
- [Complete References](references/references.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Files]

**Output Format:** [Markdown responses with reproducible R code, inline SVG figures, CSV tables, and report files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write analysis artifacts such as R scripts, SVG or PNG figures, CSV data backups, and Markdown summaries to workspace output folders.]

## Skill Version(s):

2.0.5 (source: frontmatter, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
