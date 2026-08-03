## Description: <br>
Analyzes cat litter box images, video files, or video URLs through LifeEmergence cloud APIs to produce structured observations about feces morphology, urine clump size, related health risk alerts, and historical report links without diagnosing disease. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to submit cat litter box media or URLs for waste characteristic recognition and to retrieve cloud-hosted historical analysis reports. It is intended for health monitoring and risk alerts, not disease diagnosis or treatment advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Litter-box media or URLs and report metadata are sent to LifeEmergence cloud services. <br>
Mitigation: Use the skill only when that transfer is acceptable, and avoid submitting sensitive local files or private URLs. <br>
Risk: The skill may create or reuse a workspace identity and store service tokens in a local SQLite database. <br>
Mitigation: Avoid shared workspaces unless this identity and token retention behavior is acceptable, and review local data retention before installation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-pet-litter-box-waste-analysis) <br>
- [API interface reference](references/api_doc.md) <br>
- [Analysis API reference](skills/smyx_analysis/references/api_doc.md) <br>
- [Skill usage demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown or JSON analysis report with structured observations, risk alerts, suggestions, and report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Accepts local mp4, avi, or mov files up to 10MB or public video URLs; historical reports are retrieved from cloud APIs.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release evidence; artifact SKILL.md frontmatter reports 1.0.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
