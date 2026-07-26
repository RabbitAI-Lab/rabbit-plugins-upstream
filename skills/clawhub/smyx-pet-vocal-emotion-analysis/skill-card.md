## Description: <br>
Recognizes cat and dog vocalizations through pet voiceprint AI and returns emotions and behavioral intentions such as happiness, excitement, anger, anxiety, pain, vigilance, and attention-seeking. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to analyze cat or dog audio/video files or public media URLs, generate structured pet vocal emotion reports, and retrieve cloud-hosted historical analysis reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: User pet audio/video or supplied media URLs are sent to Life Emergence cloud APIs for analysis. <br>
Mitigation: Use the skill only when cloud processing is acceptable, and avoid media that includes sensitive household, personal, or bystander information. <br>
Risk: The skill can create and reuse a local account identity, tokens, and cloud history without prompting the user. <br>
Mitigation: Review local identity and token persistence before installation or shared-machine use, and clear stored state when account continuity is not desired. <br>
Risk: Historical report retrieval depends on cloud-hosted data associated with the resolved local identity. <br>
Mitigation: Confirm that cloud history access matches the intended user context before using or sharing retrieved reports. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-pet-vocal-emotion-analysis) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>
- [API Documentation](references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown or JSON analysis reports, with optional saved text output.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can return structured recognition results, recommendations, report links, and cloud history lists.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release metadata; artifact frontmatter states 1.0.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
