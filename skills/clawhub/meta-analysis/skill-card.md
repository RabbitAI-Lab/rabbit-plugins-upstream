## Description: <br>
Comprehensive R-based meta-analysis skill covering RevMan 5.x and Stata-style workflows, effect-size conversion, robust variance estimation, Bayesian and network meta-analysis, survival and diagnostic meta-analysis, systematic-review workflow, reproducible R code, plots, heterogeneity, publication-bias checks, subgroup analysis, and meta-regression. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[medstatstar](https://clawhub.ai/user/medstatstar) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, researchers, analysts, and developers use this skill to prepare and run local R-based meta-analysis workflows, generate reproducible R scripts, summarize statistical outputs, and create publication-oriented figures for systematic reviews. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can execute local R analysis and write report, data, and figure files. <br>
Mitigation: Use it only in a working directory where local analysis artifacts are expected, and review generated R code before opting into execution. <br>
Risk: The skill reads `~/.workbuddy/MEMORY.md` for R-related configuration. <br>
Mitigation: Review that file before use and avoid storing unrelated sensitive information in configuration memory. <br>
Risk: Dependency-installation documentation is inconsistent and R packages may require manual verification. <br>
Mitigation: Install and verify R packages manually in a trusted R environment before running analyses. <br>
Risk: Pseudo-IPD or IPD-derived outputs may contain sensitive local data. <br>
Mitigation: Handle generated files as sensitive research data and avoid sharing outputs until disclosure risk has been reviewed. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/medstatstar/skills/meta-analysis) <br>
- [Publisher Profile](https://clawhub.ai/user/medstatstar) <br>
- [Project Homepage](https://github.com/medstatstar/meta-analysis) <br>
- [English User Guide](https://github.com/medstatstar/meta-analysis/blob/main/README.md) <br>
- [Chinese User Guide](https://github.com/medstatstar/meta-analysis/blob/main/README_zh-CN.md) <br>
- [Interactive Menu Reference](references/interactive_menu.md) <br>
- [Advanced API Reference](references/advanced_api.md) <br>
- [R Packages Reference](references/r_packages.md) <br>
- [Data Templates](references/data_templates.md) <br>
- [Report Template](references/report_template.md) <br>
- [Citations](references/citations.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with R code blocks, shell commands, generated R scripts, CSV tables, Markdown summaries, and SVG/PNG figures] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes local analysis artifacts such as analysis_complete.R, results_summary.md, data_backup.csv, and forest or funnel plots when the user opts into execution.] <br>

## Skill Version(s): <br>
1.8.4 (source: server release metadata; artifact frontmatter reports 1.8.3) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
