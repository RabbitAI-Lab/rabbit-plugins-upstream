## Description: <br>
Analyzes fixed-camera and optional microphone inputs for pregnancy-related emotion fluctuation signals, then returns structured reports and soothing-action guidance such as music, mindfulness audio, caregiver alerts, or escalation suggestions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and operators use this skill to analyze pregnancy activity-area audio/video or query cloud history for emotion fluctuation events, soothing actions, recommendations, and report links. It is intended for consented monitoring workflows in homes, prenatal waiting rooms, or prenatal classes, not for medical diagnosis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles sensitive pregnancy-related audio/video, cloud reports, and persistent identity linkage. <br>
Mitigation: Install and run it only after explicit consent from the monitored pregnant person, with notice to anyone likely to be recorded and clear controls for disabling uploads. <br>
Risk: Audio/video and identifiers may be sent to the LifeEmergence cloud for analysis and report storage. <br>
Mitigation: Require operators to provide deletion controls for cloud reports and local identity records before deployment. <br>
Risk: Spouse or emergency-contact notifications can disclose sensitive emotional state information or trigger without current consent. <br>
Mitigation: Configure alert recipients and escalation behavior with the pregnant person's consent, and provide a way to pause or disable alerts. <br>
Risk: Emotion analysis could be mistaken for clinical diagnosis. <br>
Mitigation: Present outputs as behavioral observations and support suggestions only, and route recurring or urgent concerns to qualified prenatal mental-health or medical resources. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-pregnancy-emotion-soothing-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [API documentation](artifact/references/api_doc.md) <br>
- [Analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown and JSON-oriented structured reports with inline shell commands and report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include analysis progress, emotion-event summaries, soothing-action recommendations, history tables, and cloud report URLs.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release metadata; artifact frontmatter lists 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
