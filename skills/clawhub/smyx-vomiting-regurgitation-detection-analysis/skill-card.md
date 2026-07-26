## Description: <br>
Analyzes indoor fixed-camera pet video to detect vomiting or regurgitation behavior, vomitus appearance, event timing, frequency, and report history. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and pet-care operators use this skill to review indoor pet camera footage for visual signs of vomiting or regurgitation and to retrieve prior cloud reports. Results are behavioral observations and should not be treated as veterinary diagnosis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive indoor pet camera footage and report data may be sent to a remote service for analysis and history lookup. <br>
Mitigation: Install only after confirming user consent, service trust, data retention expectations, and whether the uploaded media is appropriate for cloud processing. <br>
Risk: The skill can silently create or reuse cloud identity state and persist local tokens. <br>
Mitigation: Review account creation, token storage, and cleanup behavior before deployment; restrict execution to environments where that identity behavior is acceptable. <br>
Risk: Broad automatic triggers can initiate remote analysis or report retrieval when users provide pet footage or ask for historical reports. <br>
Mitigation: Require clear operator confirmation for sensitive media workflows and document when remote calls occur. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-vomiting-regurgitation-detection-analysis) <br>
- [API Documentation](references/api_doc.md) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown or JSON structured analysis report with report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write the analysis result to a user-selected output file.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata; artifact frontmatter states 1.0.7) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
