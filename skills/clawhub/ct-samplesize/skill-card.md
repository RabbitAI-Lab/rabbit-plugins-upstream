## Description: <br>
Easy-to-use sample size and power calculation tool for clinical trial practitioners, backed by R and Python workflows and supporting 49 test types. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[medstatstar](https://clawhub.ai/user/medstatstar) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Clinical trial researchers, statisticians, and developers use this skill to choose trial-design calculations, estimate sample size or power across supported scenarios, preview reproducible R/Python code, and optionally execute local computations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can run generated R/Python code locally when execution is explicitly requested. <br>
Mitigation: Keep the default preview workflow, review generated code, and use execution flags only when local computation is intended. <br>
Risk: The optional package-install workflow can download and install CRAN packages. <br>
Mitigation: Use --run-install only in a trusted environment after reviewing the printed install commands. <br>
Risk: Clinical-trial sample-size and power results may affect protocol or regulatory decisions. <br>
Mitigation: Independently validate calculations, assumptions, and outputs before relying on them for protocol or regulatory use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/medstatstar/skills/ct-samplesize) <br>
- [Project homepage](https://github.com/medstatstar/ct-samplesize) <br>
- [README](README.md) <br>
- [Advanced Reference](ADVANCED.md) <br>
- [CLI Examples](references/cli_examples.md) <br>
- [Menu](references/menu.md) <br>
- [Formulas](references/formulas.md) <br>
- [Data Format Guide](references/data_format_guide.md) <br>
- [Adaptive Simulator](references/adaptive_simulator.md) <br>
- [R Packages](references/r_packages.md) <br>
- [Operation SOP](references/operation_sop.md) <br>
- [Language Policy](references/language_policy.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, files, guidance] <br>
**Output Format:** [Markdown responses with tables, reproducible R/Python code blocks, optional shell commands, and optional PNG/data-table outputs for curve reports.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Default workflow previews generated code without executing it; local execution requires explicit opt-in such as --yes, and optional package installation requires --run-install.] <br>

## Skill Version(s): <br>
3.8.0 (source: frontmatter, release evidence, CHANGELOG) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
