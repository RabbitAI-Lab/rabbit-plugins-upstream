## Description: <br>
Track garden pests and diseases with treatments, identify problems, track treatments, and monitor effectiveness for home gardeners and small farmers managing plant health. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[johstracke](https://clawhub.ai/user/johstracke) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users, especially home gardeners and small farmers, use this skill to record pest and disease issues, log treatment history, monitor effectiveness, and export garden health notes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Treatment recommendations can be incomplete, outdated, or unsuitable for a crop, product label, local regulation, or household safety context. <br>
Mitigation: Verify current product labels, crop suitability, local regulations, protective equipment, child and pet precautions, and edible-crop or pre-harvest restrictions before applying any pesticide or fungicide. <br>
Risk: Garden issue notes, affected plants, severity, treatments, and effectiveness history are stored locally. <br>
Mitigation: Install only when local storage at ~/.openclaw/workspace/pest_tracker_db.json is acceptable, and avoid entering sensitive personal information in notes. <br>
Risk: Markdown export writes user-entered garden records to a file. <br>
Mitigation: Use the export path validation behavior and choose trusted workspace, home, or temporary output locations for generated reports. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance, files] <br>
**Output Format:** [Command-line text output and optional Markdown export] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Stores local JSON records under ~/.openclaw/workspace and can export a Markdown report to validated safe paths.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
