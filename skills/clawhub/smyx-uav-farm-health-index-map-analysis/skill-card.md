## Description: <br>
Uses UAV multispectral or high-resolution RGB imagery to compute vegetation indices such as NDVI and NDRE, generate farm health-index heatmaps, and identify abnormal crop-health zones. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External agricultural analysts, UAV service providers, farm operators, and developers use this skill to submit drone orthomosaic, image, or video inputs and review index-based crop-health maps, abnormal-zone coordinates, area estimates, coverage statistics, and report links. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Farm imagery, videos, or supplied URLs may be sent to external lifeemergence/open API services. <br>
Mitigation: Use non-sensitive test data first and confirm external-service handling is acceptable before submitting production imagery. <br>
Risk: The skill can create or reuse a local account identity, query cloud-stored history, and store service tokens in the workspace data directory. <br>
Mitigation: Review this behavior before installation and remove local identity or token files such as data/smyx-api-key.txt when persistence is not desired. <br>
Risk: The authoritative security verdict is suspicious because of cloud upload, hidden identity handling, token persistence, and implementation mismatches. <br>
Mitigation: Review and scan the skill before deployment, and restrict use to environments where those behaviors are approved. <br>


## Reference(s): <br>
- [UAV Farm Health Index API Documentation](references/api_doc.md) <br>
- [Analysis API Documentation](skills/smyx_analysis/references/api_doc.md) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-uav-farm-health-index-map-analysis) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown text with JSON-like structured analysis results and report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include health-index map URLs, vegetation-index statistics, abnormal-zone coordinates and area estimates, crop coverage, health-class statistics, and exported report image links.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release metadata; artifact frontmatter says 1.0.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
