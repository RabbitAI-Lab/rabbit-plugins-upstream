## Description: <br>
Analyzes frontal face images or short videos of elderly people with AI facial-landmark detection to compare mouth-corner height, nasolabial-fold symmetry, eyebrow-lift asymmetry, and related features, then returns a facial asymmetry index from 0 to 100%. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, caregivers, and developers use this skill to assess facial asymmetry in elderly-care settings from a provided image, video, or URL. The output is intended as auxiliary screening information and does not replace professional medical diagnosis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill processes sensitive face and health-related media through a vendor service. <br>
Mitigation: Use only with informed consent from the person or caregiver and limit inputs to images or videos that are necessary for the requested screening. <br>
Risk: The skill can create or reuse an account identity and store local identity/auth tokens or cloud report history. <br>
Mitigation: Review the configured storage location and access controls before deployment, and avoid shared workspaces for sensitive caregiver or patient workflows. <br>
Risk: Automatic history lookup or biometric analysis can expose sensitive reports if triggered too broadly. <br>
Mitigation: Keep triggers explicit for report lookup and facial analysis, and review outputs before sharing them beyond the care team. <br>
Risk: Facial asymmetry output may be mistaken for a clinical diagnosis. <br>
Mitigation: Present results as auxiliary screening information and direct suspected urgent symptoms to professional medical review. <br>


## Reference(s): <br>
- [Skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-elderly-facial-asymmetry-analysis) <br>
- [API interface documentation](references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown or JSON analysis report with risk level, asymmetry metrics, report links, and optional saved output file.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can query cloud-hosted history reports and can save analysis results to a user-specified output path.] <br>

## Skill Version(s): <br>
1.0.4 (source: release metadata; artifact frontmatter reports 1.0.7) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
