## Description: <br>
Ct Samplesize helps clinical trial practitioners calculate sample size and statistical power across 37 test types using natural-language prompts backed by R packages, with safe-preview generated R code available for review. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[medstatstar](https://clawhub.ai/user/medstatstar) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Clinical trial researchers, statisticians, and developers use this skill to estimate sample size, statistical power, and sensitivity curves for clinical trial designs. It can also produce reproducible R code for review, execution, or protocol documentation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated local R code may be executed when the user opts in with --yes. <br>
Mitigation: Review the generated code in safe-preview mode before execution and run it only in a trusted local environment. <br>
Risk: Optional CRAN package installation can download and install third-party R packages when --run-install is used. <br>
Mitigation: Review package-install commands first and use trusted repositories and environment controls. <br>
Risk: Clinical trial calculations can influence protocol or regulatory decisions if accepted without review. <br>
Mitigation: Independently validate outputs and assumptions before using results for regulatory, clinical, or commercial decisions. <br>
Risk: Curve and report generation can write files to user-selected output paths. <br>
Mitigation: Use trusted output paths and review generated files before sharing or relying on them. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/medstatstar/skills/ct-samplesize) <br>
- [Project Homepage](https://github.com/medstatstar/ct-samplesize) <br>
- [README](artifact/README.md) <br>
- [CLI Examples](artifact/references/cli_examples.md) <br>
- [Data Format Guide](artifact/references/data_format_guide.md) <br>
- [Adaptive Simulator](artifact/references/adaptive_simulator.md) <br>
- [Report Template](artifact/references/report_template.md) <br>
- [Language Policy](artifact/references/language_policy.md) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, Code, Shell commands, Configuration guidance, Files] <br>
**Output Format:** [Markdown with numeric results, CLI commands, generated R or Python code snippets, and optional PNG or JSON artifacts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generated R code is previewed by default; execution and CRAN package installation require explicit user opt-in.] <br>

## Skill Version(s): <br>
3.4.5 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
