## Description:

Meta Analysis / 医学Meta分析 helps agents guide clinical researchers through R-based meta-analysis and systematic-review workflows, producing reproducible analyses, figures, heterogeneity and bias checks, subgroup and meta-regression, network meta-analysis, and bilingual reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[medstatstar](https://clawhub.ai/user/medstatstar)

### License/Terms of Use:

MIT

## Use Case:

External clinical researchers, biostatisticians, clinicians, and medical students use this skill to plan, run, and interpret meta-analysis and systematic-review workflows in chat, including topic selection, data checks, statistical analysis, figures, and reproducible R output.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Confidential clinical, unpublished study, or patient-level data may be sent to the default Coze endpoint, with possible server-side logging or retention.

Mitigation: Review outbound-data disclosures before installing; use de-identified aggregate inputs for cloud mode, and require a verified local-only setup for confidential or patient-level workflows.

Risk: The security evidence reports embedded shared service credentials for external services.

Mitigation: Review packaged credentials and endpoints before deployment; replace, rotate, or disable shared credentials in controlled environments.

Risk: The packaged local fallback may not be dependable unless the R engine files and required packages are present and configured.

Mitigation: Verify the local R engine path, R installation, and package set before relying on local-only or offline execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/medstatstar/skills/meta-analysis)
- [Project homepage](https://github.com/medstatstar/meta-analysis)
- [README](README.md)
- [Chinese README](README_zh-CN.md)
- [Advanced API](references/advanced_api.md)
- [Interactive Menu](references/interactive_menu.md)
- [Topic Selection](references/topic-selection.md)
- [Data Templates](references/data_templates.md)
- [Language Policy](references/language_policy.md)
- [Inline Rendering](references/inline_rendering.md)
- [Bug Report Endpoint](references/bug_report_endpoint.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with reproducible R code, structured analysis results, generated report files, and SVG or PNG figures.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes analysis artifacts such as R scripts, Markdown summaries, CSV tables, and figures to workspace output folders when analyses are run.]

## Skill Version(s):

2.0.0 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
