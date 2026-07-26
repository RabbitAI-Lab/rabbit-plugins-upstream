## Description: <br>
Excel大师 helps agents choose pandas or openpyxl workflows for batch Excel and CSV processing, including merging, splitting, filtering, aggregation, validation, format preservation, and troubleshooting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and spreadsheet-heavy teams use this skill to automate local Excel and CSV transformations while choosing memory-safe and format-preserving approaches for different workbook sizes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Spreadsheet automation may overwrite source workbooks or produce unintended bulk changes. <br>
Mitigation: Use explicit input and output paths, keep backups of original workbooks, and prefer separate output files unless overwrite behavior is intentionally requested. <br>
Risk: Generated Python commands may process sensitive spreadsheet contents or large file sets. <br>
Mitigation: Review commands before running them, limit processing to intended files, and avoid exposing sensitive workbook data outside the local environment. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [guidance, code, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with Python and shell code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May read local spreadsheet inputs and write Excel, CSV, JSON, or error-report files at user-specified paths.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
