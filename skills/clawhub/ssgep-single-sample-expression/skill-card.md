## Description:

SSGEP guides agents through RNA-seq expression profiling for single-sample/no-replicate and replicated studies, including QC, quantification, DEG analysis, GO/KEGG enrichment, WGCNA, SNP differentiation, publication-ready outputs, and Shiny app generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bsk-drs](https://clawhub.ai/user/bsk-drs)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, bioinformatics analysts, and researchers use this skill to run or plan plant RNA-seq expression workflows, especially single-sample/no-replicate studies and replicated DEG analysis. It helps produce analysis outputs, publication drafts, figures, tables, and Shiny app guidance from RNA-seq project inputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests Read, Bash, and Write permissions and may propose package installation, local workflow execution, or cloud processing commands.

Mitigation: Confirm dataset paths, execution environment, package installs, and whether cloud processing is acceptable before allowing commands to run.

Risk: Single-sample/no-replicate DEG mode uses fixed dispersion and fold-change thresholds, so statistical p-values are not robust significance evidence.

Mitigation: Treat mode A p-values as ranking signals, disclose the limitation in analysis outputs, and validate key genes with qRT-PCR or independent datasets.

Risk: RNA-seq datasets may include unpublished or sensitive research data.

Mitigation: Keep analysis local unless cloud use is explicitly approved, and verify that generated reports do not expose data beyond the intended audience.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/bsk-drs/skills/ssgep-single-sample-expression)
- [R for Windows](https://cloud.r-project.org/bin/windows/base/)
- [RStudio Desktop](https://posit.co/download/rstudio-desktop/)
- [Rtools for Windows](https://cloud.r-project.org/bin/windows/Rtools/)
- [Python for Windows](https://www.python.org/downloads/windows/)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with command and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide generation of analysis plans, scripts, installation commands, tables, figures, HTML/DOCX/PPTX drafts, and Shiny app artifacts.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
