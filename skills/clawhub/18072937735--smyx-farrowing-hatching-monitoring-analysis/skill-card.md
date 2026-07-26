## Description: <br>
Monitors farrowing and poultry hatching events from continuous video, detects milestones such as water breaking, straining, piglet delivery, egg pipping, and chick emergence, and returns event reminders and reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Farm operations teams and developers use this skill to analyze fixed-camera farrowing pen or hatchery video from local files or URLs. It helps monitor reproduction milestones, produce structured event reports, and list prior cloud-hosted analysis reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Farm or hatchery media and account-linked report metadata are sent to the LifeEmergence cloud service. <br>
Mitigation: Review data handling expectations and obtain approval for sending this media and metadata to the cloud before enabling the skill. <br>
Risk: The skill can silently create or reuse account identity and store local tokens. <br>
Mitigation: Review identity sourcing, local token storage, and workspace access controls before deployment. <br>
Risk: History queries can retrieve cloud report records without clear user control. <br>
Mitigation: Limit use to workspaces where automatic history lookup is acceptable and verify that report access aligns with the intended account identity. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-farrowing-hatching-monitoring-analysis) <br>
- [Publisher profile](https://clawhub.ai/user/18072937735) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [API documentation](references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown and structured JSON with event details, timestamps, reminder levels, report links, and optional saved output files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Accepts local mp4, avi, and mov video files up to 10 MB or public video URLs; history queries return cloud report records for the current account identity.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
