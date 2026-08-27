## Description:

Meta Analysis / 医学Meta分析 helps clinical researchers run R-backed pairwise, network, Bayesian, diagnostic, survival, and systematic-review meta-analysis workflows with reproducible code, figures, and reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[medstatstar](https://clawhub.ai/user/medstatstar)

### License/Terms of Use:

MIT

## Use Case:

Clinical researchers, clinicians, pharmaceutical trial teams, and medical students use this skill to prepare datasets, choose meta-analysis methods, run cloud-backed R analyses, and produce bilingual reports with statistical outputs and visualizations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends analysis summary data and metadata such as a hostname hash to cloud services for computation.

Mitigation: Use only with datasets approved for cloud processing, avoid confidential or regulated patient-level data, and review the outbound disclosure before running analyses.

Risk: Bundled public credentials and pre-approved endpoints reduce the opportunity for per-run consent review.

Mitigation: Review configured endpoints and credentials before installation, restrict execution in sensitive environments, and monitor outbound network access.

Risk: Optional bug reporting can send user-reviewed diagnostic text to a separate Coze service.

Mitigation: Submit bug reports only after reviewing the sanitized preview and removing confidential study or operational details.

Risk: PDF full-text retrieval can access external content when explicitly requested.

Mitigation: Use PDF fetching only for approved DOI or PMID sources and confirm that license, privacy, and data-handling requirements permit retrieval.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/medstatstar/skills/meta-analysis)
- [Publisher profile](https://clawhub.ai/user/medstatstar)
- [Project homepage](https://github.com/medstatstar/meta-analysis)
- [Advanced usage](references/ADVANCED.md)
- [API reference](references/advanced_api.md)
- [Interactive menu](references/interactive_menu.md)
- [Data input templates](references/data_templates.md)
- [Complete references](references/references.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with generated analysis reports, reproducible R code, tables, and SVG/PNG figures.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Bilingual Chinese/English responses; analysis output is presented through generated HTML reports when computations run.]

## Skill Version(s):

2.2.16 (source: frontmatter, CHANGELOG, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
