## Description: <br>
Using a fixed bedroom camera, the skill analyzes an elderly person's resting chest or abdominal motion in video or images, estimates respiratory rate, and reports tachypnea risk when the rate exceeds the configured threshold. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers can use this skill to submit fixed-camera elder-care media for respiratory-rate analysis, structured tachypnea risk reporting, and cloud-backed history lookup. It is intended as assistive monitoring and not as a medical diagnosis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive bedroom video or report data may be processed by external cloud services. <br>
Mitigation: Deploy only after obtaining consent from the monitored person or legal caregiver and confirming the service provider, retention policy, deletion process, and storage controls. <br>
Risk: The skill links requests to local or cloud identities and may persist tokens. <br>
Mitigation: Run in an isolated environment, review local credential storage before deployment, and rotate or remove stored tokens when access is no longer needed. <br>
Risk: User-supplied video URLs may cause external services to fetch arbitrary media. <br>
Mitigation: Restrict inputs to trusted media locations and validate that URL-based analysis is allowed by organizational policy. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-elderly-tachypnea-detection-analysis) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>
- [Elderly Tachypnea API Documentation](references/api_doc.md) <br>
- [Shared Analysis API Documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and JSON-style structured analysis text with report links when available] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include respiratory-rate fields, signal quality, risk level, alert text, historical report records, and export links.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release metadata; artifact frontmatter states 1.0.7) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
