## Description: <br>
Detects people, vehicles, non-motorized vehicles, pets, and parcels appearing in a target area from video streams or images for general security surveillance scenarios. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and security operations teams use this skill to run object detection on uploaded or URL-based surveillance media, review structured detection results, and query cloud-hosted historical reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends media files or media URL references to a configured cloud analysis service. <br>
Mitigation: Install only where users are comfortable with those media inputs being processed by the configured cloud service, and ask the publisher for explicit data-flow, retention, and deletion details before broad deployment. <br>
Risk: The skill silently creates or reuses identity and token material and can retrieve cloud report history. <br>
Mitigation: Review workspace data storage and identity behavior before deployment, restrict access to generated report history, and confirm the publisher's permission model. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-basic-object-detection-analysis) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>
- [API Documentation](references/api_doc.md) <br>
- [Analysis API Documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and JSON-formatted analysis results with optional saved output files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include report links and cloud report-history listings when requested.] <br>

## Skill Version(s): <br>
1.0.10 (source: ClawHub release metadata; artifact frontmatter states 1.0.11) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
