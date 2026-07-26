## Description: <br>
Comprehensive R-based meta-analysis skill covering RevMan 5.x equivalents, Stata-style meta-analysis workflows, effect-size conversion, robust variance estimation, Bayesian and network meta-analysis, survival meta-analysis, trial sequential analysis, diagnostic meta-analysis, systematic-review workflow support, and reproducible R outputs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[medstatstar](https://clawhub.ai/user/medstatstar) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Clinical researchers, evidence reviewers, and analysts use this skill to turn natural-language meta-analysis requests into reproducible local R workflows, including model selection, effect-size handling, visualization, and structured result summaries. It is intended to assist statistical analysis and reporting, not to replace clinical or statistical judgment. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill runs local R analysis code and may generate R files and output artifacts in the workspace. <br>
Mitigation: Review the generated scripts and run the skill only in the intended working directory before executing analyses. <br>
Risk: Manual R package installation can use external package repositories and write to the user's R library. <br>
Mitigation: Install packages from trusted sources in a controlled R environment and review package installation prompts. <br>
Risk: PDF batch download uses external services when explicitly requested and may retrieve copyrighted full text. <br>
Mitigation: Use PDF retrieval only for DOI or PMID lists the user is authorized to access. <br>
Risk: The skill may read local R configuration from ~/.workbuddy/MEMORY.md. <br>
Mitigation: Keep that memory file free of unrelated sensitive information before using the skill. <br>
Risk: Statistical outputs can be misleading if interpreted without study context or domain expertise. <br>
Mitigation: Have qualified statistical or clinical reviewers interpret model assumptions, heterogeneity, bias, and conclusions. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/medstatstar/skills/meta-analysis) <br>
- [Project Homepage](https://github.com/medstatstar/meta-analysis) <br>
- [Interactive Menu](references/interactive_menu.md) <br>
- [Advanced API](references/advanced_api.md) <br>
- [RevMan Complete](references/revman_complete.md) <br>
- [Stata to R Mapping](references/stata_to_r_mapping.md) <br>
- [R Packages](references/r_packages.md) <br>
- [Citations](references/citations.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown guidance with inline shell and R code; generated workspace artifacts may include R scripts, SVG/PNG plots, CSV tables, Markdown summaries, and optional reports.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Runs locally in the user's R environment and writes analysis artifacts to workspace directories.] <br>

## Skill Version(s): <br>
1.7.0 (source: server release metadata; skill frontmatter reports 1.7) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
