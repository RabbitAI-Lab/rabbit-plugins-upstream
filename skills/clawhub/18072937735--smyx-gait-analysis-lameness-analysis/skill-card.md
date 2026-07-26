## Description: <br>
Analyzes pet side-view walking videos or URLs to produce vision-based gait metrics, symmetry indicators, abnormal-gait flags, recommendations, and report links without providing a medical diagnosis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, pet owners, and veterinary or rehabilitation staff can use this skill to review pet gait from side-view walking videos for home monitoring, screening, clinic intake, or post-operative tracking. Results are vision-based analysis outputs and are not a veterinary diagnosis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Pet videos and related analysis data may be sent to a cloud-backed service. <br>
Mitigation: Use only with appropriate consent and review the publisher's retention, deletion, and data handling practices before installation. <br>
Risk: The skill may create or reuse a local identity, read workspace identity data, store service tokens locally, and retrieve prior cloud reports. <br>
Mitigation: Install in a controlled workspace, review credential storage behavior, and separate anonymous analysis from authenticated history access where possible. <br>


## Reference(s): <br>
- [Skill API documentation](references/api_doc.md) <br>
- [Common analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-gait-analysis-lameness-analysis) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, shell commands] <br>
**Output Format:** [Markdown report text and optional JSON-style structured analysis; history queries return Markdown tables with report links.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include cloud-hosted report links and analysis status messages.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata; artifact frontmatter lists 1.0.4) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
