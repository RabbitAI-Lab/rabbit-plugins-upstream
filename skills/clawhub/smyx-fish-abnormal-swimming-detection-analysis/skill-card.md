## Description: <br>
Analyzes fixed-camera aquarium images or videos to identify abnormal fish swimming posture, quantify abnormal-duration ratios, and produce structured monitoring reports with suggested next actions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Aquarium keepers, aquarium operators, and developers use this skill to analyze fixed-camera fish media for side-swim, upside-down posture, axial rotation, floating or sinking behavior, and abnormal-duration ratios. The skill supports visual posture monitoring and report generation, not fish disease diagnosis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Local or URL-based aquarium media may be sent to lifeemergence.com services for cloud analysis. <br>
Mitigation: Use only authorized aquarium media and confirm that users understand remote processing before execution. <br>
Risk: The skill may create or reuse an internal identity and store service tokens in the workspace data database. <br>
Mitigation: Run in a controlled workspace, review stored credentials after use, and rotate or remove service tokens when access is no longer needed. <br>
Risk: History queries can retrieve cloud-stored report records automatically. <br>
Mitigation: Limit history-query use to authorized users and review report links before sharing outputs. <br>
Risk: Visual posture findings can be mistaken for veterinary diagnosis. <br>
Mitigation: Present outputs as posture monitoring only and direct significant or persistent abnormalities to aquarium professionals or ornamental fish veterinarians. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-fish-abnormal-swimming-detection-analysis) <br>
- [API documentation](artifact/references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown or JSON report with posture classifications, abnormal-duration metrics, recommended actions, and report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May save analysis output to a user-specified file and may query historical cloud reports.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata; artifact frontmatter reports 1.0.5) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
