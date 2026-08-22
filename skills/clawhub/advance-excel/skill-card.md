## Description:

Xlsx helps agents inspect, read, edit, create, convert, and recalculate spreadsheet files such as XLSX, XLSM, CSV, and TSV.

This skill is ready for commercial/non-commercial use.

## Publisher:

[berkgungor](https://clawhub.ai/user/berkgungor)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill when a spreadsheet is the primary input or output: inspecting workbook structure, cleaning or reshaping tabular data, editing existing spreadsheets, creating new workbooks, converting tabular formats, and recalculating formulas.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Workbook edits can overwrite or damage important spreadsheets.

Mitigation: Use copies or explicit output filenames for important workbooks.

Risk: LibreOffice recalculation on spreadsheets from untrusted sources may expose the execution environment to document-level risk.

Mitigation: Run LibreOffice recalculation on untrusted spreadsheets only when the environment is appropriately isolated.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with inline Python and bash examples; helper scripts return JSON and may create or modify spreadsheet files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Workbook inspection reports include sheet names, ranges, formula counts, detected headers, named ranges, and recommendations; recalculation reports include formula totals and Excel error summaries.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
