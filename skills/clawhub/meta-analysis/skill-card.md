## Description:

Comprehensive R-based meta-analysis skill for systematic review workflows, including RevMan-style analyses, Stata-equivalent methods, Bayesian network meta-analysis, survival meta-analysis, TSA, single-group and diagnostic meta-analysis, with bilingual output and reproducible R code.

This skill is ready for commercial/non-commercial use.

## Publisher:

[medstatstar](https://clawhub.ai/user/medstatstar)

### License/Terms of Use:

MIT

## Use Case:

External users, researchers, clinicians, and analysts use this skill to prepare and run meta-analyses, generate forest and funnel plots, assess heterogeneity and publication bias, and produce reproducible R code and report artifacts. It is intended to support statistical analysis workflows, not to replace professional clinical interpretation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Summary clinical analysis data is sent automatically to a cloud computation endpoint.

Mitigation: Use the skill only when cloud transfer of the planned summary statistics is approved, and avoid confidential, unpublished, regulated, or individual-patient data unless organizational approval covers that transfer.

Risk: The release includes reusable service tokens and shared-service endpoint dependencies.

Mitigation: Review endpoint trust, token exposure, and downstream logging or retention assumptions before installation or use in sensitive workflows.

Risk: PDF download behavior can retrieve external content when explicitly requested.

Mitigation: Use PDF download only for DOI or PMID targets the user is authorized to access and retrieve.

Risk: Meta-analysis outputs can influence clinical or research conclusions.

Mitigation: Require professional review of data extraction, model selection, quality gates, and final interpretation before relying on results.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/medstatstar/skills/meta-analysis)
- [Project homepage](https://github.com/medstatstar/meta-analysis)
- [English README](https://github.com/medstatstar/meta-analysis/blob/main/README.md)
- [Chinese README](https://github.com/medstatstar/meta-analysis/blob/main/README_zh-CN.md)
- [Advanced API reference](references/advanced_api.md)
- [Interactive menu and continuity guide](references/interactive_menu.md)
- [Data templates](references/data_templates.md)
- [Inline rendering standard](references/inline_rendering.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with reproducible R code, generated R scripts, SVG/PNG figures, CSV tables, and JSON status or gate outputs where applicable]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write analysis artifacts under output/ and meta_analysis/; numerical computation is performed through a configured cloud R endpoint when available.]

## Skill Version(s):

2.1.5 (source: SKILL.md frontmatter, parsed metadata, and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
