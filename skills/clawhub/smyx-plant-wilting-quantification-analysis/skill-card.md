## Description: <br>
Quantifies plant wilting from full-plant images or video by estimating wilting severity and likely underwatering or overwatering causes, with optional soil-moisture context for smart pots, home gardens, greenhouses, and plant factories. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to analyze plant images or videos, generate structured wilting reports, and distinguish likely dehydration from possible waterlogging. It is aimed at smart-pot, home gardening, greenhouse, and plant-factory monitoring workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Plant images, video URLs, and identity-linked analysis data are sent to remote cloud services. <br>
Mitigation: Use the skill only when that data sharing is acceptable, and avoid submitting private home images or private URLs. <br>
Risk: The skill creates or reuses a persistent identity, stores session tokens locally, and can query cloud history automatically. <br>
Mitigation: Review the backend trust relationship and token storage behavior before installation, especially in shared workspaces. <br>
Risk: Wilting-cause classification can be uncertain without soil-moisture context or clear side-view imagery. <br>
Mitigation: Confirm soil condition manually or with sensor data before acting on underwatering or overwatering guidance. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-plant-wilting-quantification-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [API interface documentation](artifact/references/api_doc.md) <br>
- [Analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, guidance] <br>
**Output Format:** [Markdown or JSON structured analysis report with optional report links and saved output files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports local media files or media URLs, optional basic/standard/json detail levels, and cloud-backed history listing.] <br>

## Skill Version(s): <br>
1.0.9 (source: server release evidence; artifact frontmatter says 1.0.7) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
