## Description: <br>
Analyzes pet vocalization audio or video to extract acoustic features, classify likely emotion categories with confidence scores, and return structured results without providing medical or behavior-modification advice. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External pet owners, caretakers, boarding centers, veterinary teams, and agent operators use this skill to classify emotions from dog or cat vocalization media, review confidence-bearing analysis results, and retrieve prior cloud reports. The results are intended as audio-based emotional context rather than medical, training, or behavior-correction advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Pet audio/video files or provided URLs are processed by an external cloud service. <br>
Mitigation: Use the skill only where users approve remote processing and the deployment has reviewed retention, authentication, and report access controls. <br>
Risk: The skill may create or reuse an internal user identity and store account tokens. <br>
Mitigation: Review local token storage and identity behavior before installation, and restrict execution to environments where account-linked operations are expected. <br>
Risk: History and report retrieval can expose prior cloud reports linked to the resolved user identity. <br>
Mitigation: Require clear user intent before history queries and confirm that report access controls match the deployment's privacy requirements. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-vocal-emotion-classification-analysis) <br>
- [Pet Vocal Emotion API Documentation](references/api_doc.md) <br>
- [Shared Analysis API Documentation](skills/smyx_analysis/references/api_doc.md) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown text with structured JSON content, report links, and command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can write the rendered analysis to a user-specified output file; history queries return cloud report lists.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata; artifact frontmatter lists 1.0.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
