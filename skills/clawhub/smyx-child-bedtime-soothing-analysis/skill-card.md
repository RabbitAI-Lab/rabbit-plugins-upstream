## Description: <br>
Analyzes nighttime child-bedroom audio and video to detect bedtime unrest, fear-of-the-dark behaviors, nightmare awakenings, and out-of-bed safety events, then returns structured soothing actions and report links. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to analyze authorized nighttime bedroom camera and microphone inputs for child bedtime unrest, then generate structured event labels, soothing actions, safety prompts, and historical report links. It is intended for parenting and smart-home assistance, not medical diagnosis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may send child-bedroom audio, video, or media URLs to external cloud services. <br>
Mitigation: Install only with clear caregiver consent, device-scope controls, retention and deletion policies, and explicit limits on sharing or secondary use. <br>
Risk: Silent identity or token flows may create or reuse local identity records without obvious user control. <br>
Mitigation: Review account-binding behavior before deployment and provide transparent controls for consent, revocation, and token storage. <br>
Risk: The skill processes sensitive children's sleep behavior and could be mistaken for medical assessment. <br>
Mitigation: Present outputs as behavioral detection and soothing guidance only, and require professional consultation for recurring or concerning sleep events. <br>
Risk: Automated soothing actions could be inappropriate for safety-critical events such as out-of-bed detection or strong distress. <br>
Mitigation: Require parent notification or urgent escalation for out-of-bed events, strong distress, and infant-mode thresholds. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-child-bedtime-soothing-analysis) <br>
- [API Documentation](artifact/references/api_doc.md) <br>
- [SMYX Analysis API Documentation](artifact/skills/smyx_analysis/references/api_doc.md) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON-compatible structured analysis reports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include event labels, audio/video signal summaries, recommended soothing actions, safety prompts, report links, and historical report tables.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release evidence; artifact frontmatter reports 1.0.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
