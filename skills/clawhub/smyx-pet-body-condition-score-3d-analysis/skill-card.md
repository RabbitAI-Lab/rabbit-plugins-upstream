## Description: <br>
Analyzes pet multi-angle videos or URLs through publisher cloud APIs to reconstruct 3D body shape and estimate Body Condition Score (BCS 1-9), classifying underweight, ideal, or overweight/obese without diagnosing disease or prescribing treatment. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers of pet health, feeder, camera, or health-management workflows use this skill to analyze pet body condition from video inputs and retrieve structured BCS observations and report links for weight-management support. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Pet videos or URLs and report-history requests are sent to publisher cloud services. <br>
Mitigation: Install only if cloud processing is acceptable; confirm publisher retention, deletion, and account-handling practices for sensitive media. <br>
Risk: The skill silently creates or reuses cloud identity context and stores authentication tokens locally. <br>
Mitigation: Review token storage and local workspace data before installation, and ask the publisher how to remove local SQLite or token data. <br>
Risk: BCS results are visual estimates and may differ from veterinary tactile assessment. <br>
Mitigation: Use outputs for weight-management reference and confirm health decisions with a veterinarian. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-pet-body-condition-score-3d-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [API documentation](references/api_doc.md) <br>
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, guidance] <br>
**Output Format:** [Markdown or JSON structured analysis reports with report links and command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call publisher cloud services with pet videos or URLs and internally generated user identity; outputs are weight-management observations, not medical diagnosis or treatment advice.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata; artifact frontmatter states 1.0.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
