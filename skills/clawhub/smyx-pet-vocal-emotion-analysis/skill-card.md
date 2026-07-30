## Description: <br>
Recognizes cat and dog barks through pet voiceprint AI and outputs likely emotions and behavioral intentions such as happiness, excitement, anger, anxiety, pain, vigilance, and attention-seeking. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to analyze pet audio or video files, call the configured cloud API, and receive structured emotion, intent, recommendation, and report-link output for human-pet interaction scenarios. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends pet media files or media URLs to configured lifeemergence.com cloud services for analysis. <br>
Mitigation: Install and run it only when users are comfortable with that transfer, and avoid submitting sensitive or unrelated media. <br>
Risk: The skill may create or reuse local identity state and maintain service tokens to associate analysis and history reports. <br>
Mitigation: Review the local workspace data and token handling before deployment, and restrict access to environments where report history should remain private. <br>
Risk: Cloud history queries can list prior reports tied to the resolved identity. <br>
Mitigation: Use the history feature only for the intended account or workspace identity and verify access expectations before sharing outputs. <br>
Risk: Emotion and intent results can be affected by noisy recordings or unclear vocalizations and are described as entertainment-oriented guidance. <br>
Mitigation: Treat outputs as advisory interaction cues rather than veterinary, safety, or diagnostic conclusions. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-pet-vocal-emotion-analysis) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>
- [API Documentation](references/api_doc.md) <br>
- [Shared Analysis API Documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown or JSON analysis text with optional saved output files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include structured report content, status text, recommendations, historical report tables, and report links.] <br>

## Skill Version(s): <br>
1.0.8 (source: server release metadata; SKILL.md frontmatter states 1.0.10) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
