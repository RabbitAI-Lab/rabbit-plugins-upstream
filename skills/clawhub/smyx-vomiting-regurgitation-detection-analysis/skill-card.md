## Description: <br>
Detects pet vomiting or regurgitation behavior from fixed indoor camera video and returns structured observations about event timing, frequency, motion cues, vomitus characteristics, and report links. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External pet owners, multi-pet households, senior pet caregivers, and animal-hospital staff can use this skill to analyze indoor pet videos for visual vomiting or regurgitation indicators and retrieve historical structured reports. The outputs are behavior observations, not medical diagnoses. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Indoor pet videos may contain sensitive household imagery and are sent to external services for analysis. <br>
Mitigation: Use the skill only when cloud processing is acceptable, limit submissions to necessary footage, and avoid videos that reveal unrelated private spaces or people. <br>
Risk: Analysis activity is associated with an automatically managed local or cloud identity. <br>
Mitigation: Review the identity and account model before installation and use an environment where persisted identity data can be managed or removed. <br>
Risk: Historical reports may be stored and retrieved from cloud services. <br>
Mitigation: Confirm that report retention and deletion controls meet the deployment's privacy requirements before using history lookup features. <br>
Risk: The skill provides visual behavior observations that may be mistaken for veterinary diagnosis. <br>
Mitigation: Present results as observational support only and escalate frequent, bloody, or severe vomiting indicators to a qualified veterinarian. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-vomiting-regurgitation-detection-analysis) <br>
- [API documentation](references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, shell commands, guidance] <br>
**Output Format:** [Markdown or JSON structured analysis report with observations, risk prompts, recommendations, history tables, and report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include cloud-hosted report links and historical report query results.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release metadata; artifact frontmatter lists 1.0.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
