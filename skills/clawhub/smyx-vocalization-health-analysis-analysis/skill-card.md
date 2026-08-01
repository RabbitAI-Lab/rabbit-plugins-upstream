## Description: <br>
Analyzes livestock and poultry audio or sound-bearing video to identify abnormal vocalizations and produce respiratory health risk screening hints. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Farm operators and animal-health teams use this skill to screen flock or herd audio/video for abnormal vocalization patterns, review structured risk hints, and retrieve prior cloud reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Selected farm audio/video or URL is sent to a cloud service for analysis. <br>
Mitigation: Submit only approved media, avoid recordings with unrelated sensitive content, and confirm the deployment's data-handling requirements before use. <br>
Risk: The skill silently manages account identity, remote login, cloud history access, and local account/token data. <br>
Mitigation: Install only in a trusted workspace, protect the workspace data directory, and review identity and token handling before shared or regulated use. <br>
Risk: Cloud report history is associated with the current internal identity. <br>
Mitigation: Run the skill under the intended workspace identity and avoid shared identities when report history should remain separated. <br>
Risk: Respiratory health outputs are screening hints rather than veterinary diagnosis. <br>
Mitigation: Use qualified veterinary review and appropriate laboratory testing before diagnosis, treatment, or medication decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-vocalization-health-analysis-analysis) <br>
- [API interface documentation](references/api_doc.md) <br>
- [SMYX analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands] <br>
**Output Format:** [Markdown status and report text with structured JSON analysis content, report links, and optional saved text output.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Accepts local audio/video files or public URLs, can list cloud history reports, and limits local file inputs to 10 MB.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release metadata; artifact frontmatter says 1.0.5) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
