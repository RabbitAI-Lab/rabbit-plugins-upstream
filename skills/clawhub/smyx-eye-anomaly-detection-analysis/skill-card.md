## Description: <br>
AI-powered pet eye anomaly detection from close-up pet images or videos identifies redness, tearing, tear staining, and pupil or cornea opacity, then returns structured visual anomaly alerts and report links. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External pet owners, boarding centers, and veterinary triage users can submit close-up pet face images or videos for visual screening of eye redness, tearing, opacity, and asymmetry. The skill is a monitoring and triage aid, not a substitute for professional veterinary diagnosis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Pet images, videos, or provided media URLs are sent to the publisher's cloud analysis service. <br>
Mitigation: Use only media appropriate for third-party processing, avoid sensitive household footage, and confirm the publisher's retention and deletion policy before deployment. <br>
Risk: The skill can automatically create or reuse a remote identity and store authentication tokens locally for report history access. <br>
Mitigation: Run the skill in a dedicated workspace, protect or periodically clear local skill data, and review credential-storage and account-linking behavior before use. <br>
Risk: Visual anomaly results may be mistaken for veterinary diagnosis. <br>
Mitigation: Present results as screening guidance only and direct users to professional veterinary care for abnormal, severe, or persistent symptoms. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-eye-anomaly-detection-analysis) <br>
- [Publisher profile](https://clawhub.ai/user/smyx-sunjinhui) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [API documentation](references/api_doc.md) <br>
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and JSON-style structured analysis text with report links; optional file output when requested.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include cloud report history and export links associated with the resolved user identity.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata; artifact frontmatter reports 1.0.5) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
