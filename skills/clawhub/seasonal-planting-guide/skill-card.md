## Description: <br>
Provides monthly, zone-specific planting schedules, plant details, and custom entries to help gardeners plan seasonal crops year-round. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[johstracke](https://clawhub.ai/user/johstracke) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Home gardeners, small farmers, and container or indoor gardeners use this skill to get USDA-zone planting schedules, search plant details, add local varieties, and export planting calendars. <br>

### Deployment Geography for Use: <br>
Global; recommendations are organized around USDA hardiness zones. <br>

## Known Risks and Mitigations: <br>
Risk: Custom plant names and notes are saved locally under ~/.openclaw/workspace. <br>
Mitigation: Avoid entering sensitive personal or business information in custom plant notes unless local storage is acceptable. <br>
Risk: The --export option can create or overwrite a Markdown file at the user-selected path, including many locations inside the home directory. <br>
Mitigation: Review the export path before running the command and keep exports in the workspace or another intended folder. <br>


## Reference(s): <br>
- [Seasonal Planting Guide on ClawHub](https://clawhub.ai/johstracke/skills/seasonal-planting-guide) <br>
- [Skill definition](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Plain text CLI output and optional Markdown calendar exports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Stores custom plant data locally under ~/.openclaw/workspace and can export calendars to a user-selected Markdown file.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
