## Description: <br>
Plant Tracker helps gardeners manage plant inventories, care schedules, growth records, search, and Markdown exports for indoor plants, gardens, and harvest tracking. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[johstracke](https://clawhub.ai/user/johstracke) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External gardeners and home growers use this skill to maintain a local plant inventory, record watering, fertilizing, pruning, harvest, and observation notes, search records, and export summaries. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Plant locations and care notes are stored on disk and can be included in exports. <br>
Mitigation: Treat records and exports as personal data and choose storage and sharing locations intentionally. <br>
Risk: A selected export filename may overwrite an existing local file. <br>
Mitigation: Review export paths before running the export command and keep backups of important files. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/johstracke/skills/plant-tracker) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Files] <br>
**Output Format:** [Plain text CLI output, local JSON data files, and Markdown exports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Stores plant records locally under ~/.openclaw/workspace/plants_db.json and exports Markdown only when requested.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
