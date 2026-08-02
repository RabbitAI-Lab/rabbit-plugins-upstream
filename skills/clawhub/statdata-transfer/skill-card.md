## Description: <br>
Reads and converts 50+ statistical software and clinical-trial data formats while preserving variable labels, value labels, and missing-value metadata where the target format supports it. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[medstatstar](https://clawhub.ai/user/medstatstar) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, data engineers, statisticians, and clinical data teams use this skill to inspect statistical datasets, convert files between SPSS, Stata, SAS, R, Excel, Parquet, JSON, and related formats, and understand metadata loss before export. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security scan flags a vulnerable XML dependency path involving lxml while processing user-supplied XML, HTML, ODM, WDX, or Origin inputs. <br>
Mitigation: Pin lxml to a patched release such as >=6.1.0 or avoid untrusted XML-like inputs until the dependency is reviewed. <br>
Risk: Some conversions may call a local R interpreter for selected R, Minitab, or EpiData formats when explicitly enabled. <br>
Mitigation: Keep allow_r_exec disabled for untrusted files and use the pure-Python paths where available. <br>
Risk: Converted statistical outputs can lose metadata when the destination format cannot preserve labels or special missing values. <br>
Mitigation: Review the skill's preservation warnings and prefer metadata-capable outputs such as Parquet, Stata, or supported binary statistics formats for lossless workflows. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/medstatstar/skills/statdata-transfer) <br>
- [Project homepage](https://github.com/medstatstar/statdata-transfer) <br>
- [English README](https://github.com/medstatstar/statdata-transfer/blob/main/README.md) <br>
- [Chinese README](https://github.com/medstatstar/statdata-transfer/blob/main/README_zh-CN.md) <br>
- [Usage examples](references/usage_examples.py) <br>
- [v1.4 implementation summary](references/v1.4_implementation_summary.json) <br>
- [New formats architecture analysis](references/new_formats_architecture_analysis.json) <br>
- [CRAN](https://cran.r-project.org/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, files] <br>
**Output Format:** [Markdown guidance with Python and shell snippets; optional local converted data files and metadata sidecars when the user explicitly requests execution.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Bilingual user-facing guidance; previews by default and writes outputs only after explicit user confirmation.] <br>

## Skill Version(s): <br>
2.2.0 (source: SKILL.md frontmatter, CHANGELOG, and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
