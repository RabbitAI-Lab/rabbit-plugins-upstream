## Description: <br>
Creates, edits, repairs, analyzes, and converts spreadsheet files, including .xlsx, .xlsm, .csv, and .tsv outputs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[legionspace-hackathon](https://clawhub.ai/user/legionspace-hackathon) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and spreadsheet users use this skill to generate, clean, edit, repair, analyze, format, chart, and convert spreadsheet files. It is intended for tasks where the deliverable is a spreadsheet file rather than a document, standalone script, or database pipeline. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The formula recalculation helper may modify an input workbook by writing cached formula results. <br>
Mitigation: Run the skill on a copy when the original workbook must remain byte-for-byte unchanged. <br>
Risk: Formula recalculation can fall back to static analysis when the formula engine cannot handle some functions. <br>
Mitigation: Review any warning returned by the helper and verify critical formulas in a spreadsheet application before relying on the result. <br>
Risk: Spreadsheet edits can accidentally change user data or formatting if the task intent is misunderstood. <br>
Mitigation: Preserve original sheets, write analysis or derived results to new sheets when editing existing workbooks, and inspect the output before distribution. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/legionspace-hackathon/skills/wps-xlsx) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/legionspace-hackathon) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, files] <br>
**Output Format:** [Markdown guidance with Python code snippets and generated spreadsheet files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use a local formula recalculation helper to validate formulas and write cached formula results into workbook files.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and artifact _meta.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
