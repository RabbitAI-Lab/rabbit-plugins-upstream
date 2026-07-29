## Description: <br>
Helps agents generate and validate basic RFC 4180 CSV with comma-separated fields, double-quote escaping, empty-field distinctions, and column-count checks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and data workflow users use this skill to prepare simple CSV exports and basic cross-tool data exchange when standard comma-separated RFC 4180 quoting is sufficient. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Callback results could expose data if sent to an untrusted URL. <br>
Mitigation: Use callback_url only with trusted endpoints and avoid sending sensitive CSV content to unknown destinations. <br>
Risk: CSV values opened in spreadsheet tools can trigger formula-injection or formatting issues that this free version does not defend against. <br>
Mitigation: Sanitize untrusted values before spreadsheet use, especially fields beginning with =, +, -, or @, and handle Excel-specific BOM or formatting needs separately. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/csv-free) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown guidance with CSV text examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Focused on comma-separated RFC 4180 CSV; does not provide BOM handling, alternate delimiters, or spreadsheet formula-injection defenses.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
