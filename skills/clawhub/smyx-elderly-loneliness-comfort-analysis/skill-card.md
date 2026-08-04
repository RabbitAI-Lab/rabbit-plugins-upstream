## Description: <br>
Using a fixed camera in the home of a solitary-living elderly person or in a private nursing-home room, the system analyzes daily activity video and detects loneliness-related behaviors: prolonged solitude, static gazing, sighing, and talking-to-self. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and elderly-care service teams use this skill to analyze fixed-camera video or video URLs, compute a loneliness index, summarize behavior signals, and suggest warm companionship actions or caregiver follow-up. It is intended for smart-aging workflows where consent, privacy controls, and human review are in place. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill processes private elderly-care video or optional audio and can use cloud report storage and export links. <br>
Mitigation: Use only with informed consent from the elder and caregivers, verify the backend account scope, minimize retained media, and prefer aggregate metrics or privacy-preserving modes where available. <br>
Risk: The workflow can trigger caregiver notifications or device-based companionship actions and uses persistent local account/session data. <br>
Mitigation: Require explicit confirmation or opt-in before history lookup, outreach, or device actions; disable automatic interventions when the deployment cannot provide clear user-directed control. <br>
Risk: Loneliness-related behavior analysis could be mistaken for a medical or mental-health diagnosis. <br>
Mitigation: Present results as behavioral statistics and companionship suggestions only, and route serious or persistent concerns to qualified local elder-care or mental-health professionals. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-elderly-loneliness-comfort-analysis) <br>
- [API Documentation](artifact/references/api_doc.md) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown text with structured JSON report content, report links, and command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include loneliness index, behavior metrics, companionship action recommendations, caregiver summaries, historical report lists, and export links.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata; artifact frontmatter reports 1.0.6) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
