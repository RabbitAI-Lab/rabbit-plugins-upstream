## Description: <br>
Analyzes fixed-camera office-area video to produce anonymous zone-level workplace stress indices, heatmap colors, trends, and manager-facing suggestions for organizational health monitoring. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and workplace health platform operators use this skill to analyze office-area video or image inputs through an external API and return anonymous, zone-level stress heatmaps and structured reports for organizational health monitoring. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive workplace camera analysis may affect employee privacy and workplace trust. <br>
Mitigation: Deploy only after employee notice and consent or another documented lawful basis, and verify that the skill is used for organization-level health monitoring rather than individual evaluation. <br>
Risk: Video, report links, identifiers, and tokens are processed through external cloud APIs and may be retained outside the local environment. <br>
Mitigation: Confirm storage locations, retention periods, access controls, and report retrieval permissions with the external service before installation. <br>
Risk: Persistent local or remote identity linkage can associate historical report queries with a user or organization. <br>
Mitigation: Limit access to approved operators, review identity handling, and ensure historical reports are available only to authorized personnel. <br>
Risk: Small group sizes can make zone-level outputs effectively identifying. <br>
Mitigation: Enforce the documented minimum sample rule so zones with fewer than three people return insufficient_sample rather than stress scores. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-workplace-stress-heatmap-analysis) <br>
- [API Documentation](references/api_doc.md) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, guidance] <br>
**Output Format:** [Markdown or JSON report content with optional report links and heatmap result fields] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include zone-level stress indices, heatmap colors, trend comparisons, alert levels, manager suggestions, and historical report listings.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata; artifact frontmatter reports 1.0.7) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
