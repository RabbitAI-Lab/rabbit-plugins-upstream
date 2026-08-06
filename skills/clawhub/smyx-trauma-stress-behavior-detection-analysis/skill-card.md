## Description: <br>
Analyzes fixed-camera emergency shelter video to detect acute stress-related behavior signals and produce psychological crisis alerts for authorized response teams. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Authorized emergency response teams and field mental-health responders use this skill to analyze shelter or temporary resettlement video, locate people who may need psychological first aid, and retrieve prior cloud reports for incident review. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: Highly sensitive shelter video or video URLs may be sent to the vendor service. <br>
Mitigation: Install only in an authorized emergency-response environment, require explicit consent or legal authorization, and restrict inputs to approved cameras or domains. <br>
Risk: Cloud history reports may expose sensitive emergency-response records. <br>
Mitigation: Limit report access to authorized responders and define report retention and access-review procedures before use. <br>
Risk: Local identity or token persistence may occur with limited user control. <br>
Mitigation: Use a managed workspace with documented token cleanup, storage controls, and operator accountability. <br>
Risk: Behavior alerts may be incorrect or mistaken for clinical findings. <br>
Mitigation: Require human review by qualified responders before dispatch escalation and present results as visual behavior observations, not ASD, PTSD, or other diagnoses. <br>


## Reference(s): <br>
- [API documentation](references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-trauma-stress-behavior-detection-analysis) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, guidance] <br>
**Output Format:** [Structured Markdown or JSON text with report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes behavior-observation alerts, zone or subject tracking cues, responder dispatch suggestions, PFA guidance, and report export links; outputs are not clinical diagnoses.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release metadata; artifact frontmatter: 1.0.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
