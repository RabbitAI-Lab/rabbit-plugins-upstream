## Description: <br>
Identifies acquaintances in videos or images through face photo comparison, supports face-database enrollment, and returns structured recognition results with locations and report links. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to analyze supplied images or videos for known-person face recognition in home or office monitoring workflows, after the relevant faces have been enrolled in the service database. It can also return cloud-hosted historical recognition reports for the current internal identity. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Face images or videos and related identity/report metadata are sent to the configured cloud service. <br>
Mitigation: Use the skill only when users have consent and legal authority for biometric recognition and cloud processing. <br>
Risk: The local workspace database can contain persistent identity and token data. <br>
Mitigation: Treat the workspace data directory as sensitive, restrict access, and rotate or remove stored tokens and identities when they are no longer needed. <br>
Risk: Historical report queries retrieve cloud-hosted recognition records with limited user control. <br>
Mitigation: Review the service account, report access scope, and retention expectations before using the report-list workflow. <br>


## Reference(s): <br>
- [API interface documentation](references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-familiar-person-recognition-analysis) <br>
- [Publisher profile](https://clawhub.ai/user/18072937735) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Files] <br>
**Output Format:** [Markdown or JSON structured analysis text with optional saved output file and report-link URLs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Results may include recognized identities, locations in the media, analysis status, historical report records, and report export links.] <br>

## Skill Version(s): <br>
1.0.9 (source: server release metadata; artifact frontmatter says 1.0.10) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
