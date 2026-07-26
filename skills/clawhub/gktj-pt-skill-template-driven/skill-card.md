## Description: <br>
Use when generating patient-facing questionnaire analysis reports from uploaded survey spreadsheets or questionnaire tables, especially when the output must include fixed sections, consistent charts, controlled Word typography, and restrained patient-facing wording. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lee-luogen](https://clawhub.ai/user/lee-luogen) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to turn patient questionnaire spreadsheets or copied survey tables into fixed-structure patient-facing analysis reports with markdown, DOCX, charts, and summary outputs. It is intended for questionnaire reporting, not doctor reports, clinical trial manuscripts, or clinical recommendations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Patient survey data may contain unnecessary identifiable health information. <br>
Mitigation: Use the minimum necessary data, remove unnecessary identifiers before processing, and review generated report files before sharing. <br>
Risk: The artifact references scripts and template resources that are not included in this package version. <br>
Mitigation: Verify required scripts and template resources are available in the execution environment before using the workflow. <br>
Risk: Questionnaire feedback could be overstated as efficacy proof or clinical advice. <br>
Mitigation: Keep the report in patient-facing questionnaire language and review outputs to ensure they avoid efficacy, safety, or clinical recommendation claims. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/lee-luogen/skills/gktj-pt-skill-template-driven) <br>
- [Server-resolved GitHub provenance](https://github.com/LEE-luogen/GKTJ-Pt-skill-template-driven) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Files] <br>
**Output Format:** [Markdown guidance with file artifacts including JSON intermediates, chart images, and DOCX reports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Expected artifacts include report_draft.md, report_final.md, report_summary.json, questionnaire/report payload JSON files, chart PNGs in the legacy flow, and template-driven DOCX reports.] <br>

## Skill Version(s): <br>
0.1.1 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
