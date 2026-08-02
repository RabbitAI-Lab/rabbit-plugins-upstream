## Description: <br>
Triggers when a user provides images or videos of crop leaves, buds, or fruits for pest identification, then calls server-side APIs to detect common agricultural pests and return pest types with confidence scores. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agricultural operators use this skill to analyze crop images or videos for likely pest type, count estimates, confidence scores, and report links. It supports early pest observation for crops such as tomato, corn, peanut, and cotton, but does not provide pesticide or treatment recommendations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Crop images or videos are uploaded to lifeemergence.com services for analysis. <br>
Mitigation: Avoid using sensitive farm, location, business, or personally identifying media unless the service's retention, deletion, and account practices are acceptable. <br>
Risk: The skill can automatically create or reuse a local/cloud identity and persist account tokens or history state. <br>
Mitigation: Use a dedicated workspace or account context, restrict access to persisted workspace data, and clear local state when the skill is no longer needed. <br>
Risk: Historical reports may be retrieved through the stored identity. <br>
Mitigation: Confirm the identity and report-access boundaries before using the history feature in shared or sensitive environments. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-crop-pest-identification-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [Crop pest identification API documentation](references/api_doc.md) <br>
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, files] <br>
**Output Format:** [Markdown or JSON analysis report with optional file output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include pest names, count estimates, confidence scores, report links, and history tables.] <br>

## Skill Version(s): <br>
1.0.5 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
