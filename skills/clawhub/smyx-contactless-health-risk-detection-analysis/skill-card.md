## Description: <br>
Combines frontal facial image capture with multimodal physiological feature analysis to provide early risk screening and alerts for chronic and acute conditions such as heart attack, stroke, hypertension, and hyperlipidemia. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and care-support teams can use this skill to analyze frontal face images or short videos for early health-risk screening and to retrieve prior cloud-hosted screening reports. The results are screening references only and do not replace professional medical diagnosis or examination. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive face images, videos, and health-risk outputs may be sent to an external cloud service. <br>
Mitigation: Use only with informed consent and only in environments where cloud processing of health-related media is acceptable. <br>
Risk: The skill silently creates or reuses an identity and may associate reports with locally stored tokens and report history. <br>
Mitigation: Review identity and local storage behavior before installation, and clear stored credentials or report history according to the deployment policy. <br>
Risk: Health-risk outputs can be mistaken for medical diagnosis. <br>
Mitigation: Present outputs as early screening references and direct users to professional medical care for diagnosis, examination, or high-risk findings. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-contactless-health-risk-detection-analysis) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>
- [API Interface Documentation](artifact/references/api_doc.md) <br>
- [Analysis API Error Reference](artifact/skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown and JSON-like structured analysis text with report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write the returned report text to a user-specified output file.] <br>

## Skill Version(s): <br>
1.0.9 (source: server release metadata; artifact frontmatter states 1.0.11) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
