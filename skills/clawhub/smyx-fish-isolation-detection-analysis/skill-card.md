## Description: <br>
Analyzes aquarium or aquaculture video to track fish positions, estimate schooling behavior, and flag persistent isolation from the school centroid. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, aquarists, aquarium operators, and aquaculture teams use this skill to analyze fixed-camera footage for schooling patterns, prolonged isolation, and alert-oriented behavior reports. It supports review of isolation events, historical report lookup, and non-diagnostic guidance such as visual inspection, water-quality checks, and escalation to aquatic professionals. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Analysis inputs, tank URLs, account-linked history, and report data may be sent to LifeEmergence services. <br>
Mitigation: Use the skill only when that provider relationship is acceptable and avoid submitting sensitive footage or URLs without appropriate consent. <br>
Risk: The skill can create or reuse a persistent local user identity and store reusable user or token data in the workspace. <br>
Mitigation: Review local persistence before shared or regulated deployments, and remove stored identity or token data when the workspace is retired. <br>
Risk: Behavior alerts can be misleading when tracking quality is low, visibility is obstructed, or naturally solitary species are judged with generic schooling thresholds. <br>
Mitigation: Require adequate camera coverage and ReID quality, apply species-specific baselines, and treat unreliable signals as requests to reshoot or adjust the camera rather than as alerts. <br>
Risk: Fish isolation signals may be mistaken for medical diagnosis or automated treatment instructions. <br>
Mitigation: Keep outputs non-diagnostic, avoid drug names or dosages, and require user or professional confirmation before isolation, water changes, medication, or device actions. <br>


## Reference(s): <br>
- [Fish isolation API documentation](artifact/references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-fish-isolation-detection-analysis) <br>
- [Publisher profile](https://clawhub.ai/user/smyx-sunjinhui) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown or JSON analysis reports with command-line status text and report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include isolated-fish lists, distance and duration metrics, alert levels, recommended actions, disclaimers, and historical report tables.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata; artifact frontmatter reports 1.0.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
