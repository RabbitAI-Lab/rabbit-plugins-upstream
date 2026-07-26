## Description: <br>
Track vehicle expenses (gas, maintenance, parts) in Google Sheets and save related photos. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[huchengtw](https://clawhub.ai/user/huchengtw) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users use this skill to record vehicle expenses, mileage, cost, category, and related receipt photos into Google Sheets or local Excel files. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Dry-run can still update category defaults in the skill configuration. <br>
Mitigation: Review runs before installing and avoid relying on dry-run as fully no-write until the config-save behavior is fixed. <br>
Risk: Photo and local storage paths may not be safely contained when vehicle or category values include path-like input. <br>
Mitigation: Use a dedicated storage directory and avoid vehicle or category names containing slashes, absolute paths, or '..'. <br>
Risk: Google Sheets writes depend on service account access to the configured spreadsheet. <br>
Mitigation: Use a dedicated Google service account limited to the intended spreadsheet. <br>


## Reference(s): <br>
- [Vehicle Expense Tracker on ClawHub](https://clawhub.ai/huchengtw/skills/vehicle-tracker) <br>
- [Publisher profile: huchengtw](https://clawhub.ai/user/huchengtw) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown instructions with shell commands and JSON previews from the tracker script] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write expense rows to Google Sheets or local Excel files and may copy photo files when executed without dry-run.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
