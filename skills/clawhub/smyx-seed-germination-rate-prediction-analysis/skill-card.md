## Description: <br>
Analyzes seedling tray images or videos with AI object detection to identify emerged seedlings, count germinated seeds, and estimate germination rate for nursery, greenhouse, home planting, and seed testing workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to analyze seedling tray images or videos, estimate germinated seed counts and germination rate, and retrieve prior germination analysis reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Seed images, videos, and report-history requests are sent to the publisher's cloud service. <br>
Mitigation: Use the skill only when this data transfer is acceptable, avoid sensitive media, and confirm remote endpoints and deletion practices with the publisher before deployment. <br>
Risk: The skill silently creates or reuses an account-like identifier and stores service tokens in the workspace. <br>
Mitigation: Review identity and token handling before deployment, isolate the workspace, and remove or rotate persisted tokens after use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-seed-germination-rate-prediction-analysis) <br>
- [Seed germination API reference](references/api_doc.md) <br>
- [Analysis API error reference](skills/smyx_analysis/references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON] <br>
**Output Format:** [Markdown and JSON structured analysis reports with seedling counts, germination-rate estimates, history tables, and report links.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include cloud-generated report links and history-query results.] <br>

## Skill Version(s): <br>
1.0.10 (source: server release evidence; SKILL.md frontmatter states 1.0.9) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
