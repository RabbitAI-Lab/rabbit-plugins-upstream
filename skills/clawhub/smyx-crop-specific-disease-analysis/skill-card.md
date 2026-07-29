## Description: <br>
Analyzes images, videos, or URLs of economic-crop leaves to identify crop-specific diseases such as corn leaf blights, potato late blight, peanut leaf spot, and tomato viral disease, returning structured visual findings. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to submit crop leaf images, short videos, local files, or URLs for visual disease screening and to retrieve cloud-hosted history for prior analysis reports. It is intended for crop-disease identification support, not treatment or disease-control recommendations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends crop images, videos, URLs, and report-history queries to an external service. <br>
Mitigation: Install only where external processing is acceptable, avoid submitting unrelated or sensitive imagery, and review service and data-handling requirements before use. <br>
Risk: The skill silently creates or reuses an internal user identity and can store returned service tokens locally. <br>
Mitigation: Review identity and token storage behavior before installation, isolate the workspace for this skill, and clear local identity or token state when it is no longer needed. <br>
Risk: Visual crop-disease recognition can be inaccurate or incomplete, and the artifact states that outputs are for initial screening rather than final diagnosis. <br>
Mitigation: Use the report as decision support only and confirm findings with field observations or an agronomy expert before acting on treatment or disease-control decisions. <br>


## Reference(s): <br>
- [Crop-Specific Disease API Documentation](artifact/references/api_doc.md) <br>
- [Shared Analysis API Documentation](artifact/skills/smyx_analysis/references/api_doc.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-crop-specific-disease-analysis) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Files] <br>
**Output Format:** [Markdown text with JSON-formatted structured analysis, disease labels, confidence information, symptom descriptions, report links, and optional saved output files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [History queries return cloud report records for the current internal identity; analysis results are visual screening outputs and may include report export links.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release metadata; artifact frontmatter shows 1.0.4) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
