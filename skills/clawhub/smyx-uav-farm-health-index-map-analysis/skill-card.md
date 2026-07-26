## Description: <br>
Submits UAV farm imagery for vegetation-index analysis and returns a structured farm health-index report with heatmap output, abnormal-zone details, coverage metrics, and report links. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External agricultural users, drone service providers, and developers can use this skill to analyze UAV orthophotos, mosaics, or supported videos for crop vigor monitoring. It helps identify low-health field zones and produce structured reports for precision-agriculture review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Farm imagery or remote media URLs may be sent to an external analysis service. <br>
Mitigation: Use only approved imagery and URLs, confirm that remote processing is acceptable for the data owner, and avoid submitting sensitive geospatial or operational data unless the service terms and retention policy are acceptable. <br>
Risk: The skill may automatically create or reuse an internal account identity and query cloud report history. <br>
Mitigation: Run it in a controlled workspace, review identity and history-query behavior before deployment, and restrict use to contexts where automatic account association is permitted. <br>
Risk: Service tokens or profile data may be stored locally. <br>
Mitigation: Limit filesystem access to trusted users, rotate any exposed credentials, and clear local state after use when persistent identity or token storage is not desired. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-uav-farm-health-index-map-analysis) <br>
- [API Documentation](references/api_doc.md) <br>
- [Analysis API Documentation](skills/smyx_analysis/references/api_doc.md) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, shell commands, files] <br>
**Output Format:** [Markdown report text or JSON, with optional local output file when an output path is supplied.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include health-index heatmap links, vegetation-index summaries, abnormal-zone coordinates or areas, cloud history listings, and report export links.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata; artifact frontmatter states 1.0.6) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
