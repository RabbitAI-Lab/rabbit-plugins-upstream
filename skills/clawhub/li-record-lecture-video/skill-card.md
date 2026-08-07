## Description: <br>
Generates day-by-day Excel study plans from user-provided recorded-course video titles and durations, with built-in or custom Excel template support. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[43622283](https://clawhub.ai/user/43622283) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, training coordinators, and agent operators use this skill to turn recorded-course video inventories into daily study schedule Excel workbooks for certification and training courses. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The helper scripts execute locally and can create the output directory for the generated workbook. <br>
Mitigation: Confirm the config, template file, and non-system .xlsx output path before execution. <br>
Risk: User-provided video titles and Excel templates influence generated workbook content. <br>
Mitigation: Use only files explicitly provided by the user, keep formula-injection sanitization enabled for titles, and review the generated workbook before sharing. <br>
Risk: Large or malformed video lists can produce unusable plans or excessive local processing. <br>
Mitigation: Keep daily_hours, video count, and title lengths within the documented limits before running the generator. <br>


## Reference(s): <br>
- [Template Specification](artifact/references/template-spec.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/43622283/skills/li-record-lecture-video) <br>
- [Publisher Profile](https://clawhub.ai/user/43622283) <br>


## Skill Output: <br>
**Output Type(s):** [Configuration, Shell commands, Guidance, Files] <br>
**Output Format:** [Excel .xlsx workbook with JSON configuration and shell command guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces a local workbook; can preserve user-provided Excel template styles and layouts when a template is supplied.] <br>

## Skill Version(s): <br>
2.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
