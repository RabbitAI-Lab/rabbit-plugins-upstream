## Description: <br>
Analyzes pet home-camera videos or URLs for separation-anxiety behaviors, returns structured monitoring results, and recommends comfort actions such as voice playback, treat dispensing, or interactive toys without providing a medical diagnosis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Pet owners, boarding centers, and agents supporting pet-care workflows use this skill to review owner-away video evidence, identify likely separation-anxiety behaviors, quantify severity, query prior reports, and provide behavior-observation guidance. It is intended for monitoring and recommendations, not veterinary diagnosis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Pet or home-camera videos and video URLs may be sent to external cloud analysis services. <br>
Mitigation: Use only media the user is authorized to share, avoid sensitive scenes where possible, and review the provider's handling and retention expectations before installation. <br>
Risk: The skill can silently create or reuse a local account identity and store authentication tokens in a workspace SQLite database. <br>
Mitigation: Run it in an isolated workspace, restrict access to the workspace data directory, and clear local tokens or generated identities when the workflow is no longer needed. <br>
Risk: Behavior analysis may be mistaken for professional medical or veterinary advice. <br>
Mitigation: Present results as behavior observations and recommendations only, and direct severe or persistent cases to a veterinarian or qualified behavior specialist. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-separation-anxiety-relief-analysis) <br>
- [Publisher profile](https://clawhub.ai/user/smyx-sunjinhui) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [Pet separation anxiety API documentation](references/api_doc.md) <br>
- [Common AI analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, API calls, files] <br>
**Output Format:** [Markdown or JSON structured analysis report with report links; optional file output when requested] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include severity labels, behavior observations, intervention suggestions, history-list results, and exported report URLs.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata; artifact frontmatter reports 1.0.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
