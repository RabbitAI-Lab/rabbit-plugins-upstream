## Description: <br>
Detects targets such as people, vehicles, non-motorized vehicles, and pets within target areas; supports batch image analysis for outdoor surveillance scenarios such as courtyards, orchards, and farms. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and operators use this skill to analyze outdoor monitoring images or videos for target detection, classification, counts, intrusion assessment, risk level, and historical report lookup. It is suited for outdoor security and care workflows around yards, orchards, farms, and similar monitored areas. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uploads local files or remote media URLs to external LifeEmergence/Open API services for processing. <br>
Mitigation: Use only media that is approved for cloud processing, and avoid submitting sensitive surveillance footage unless the external processing terms are acceptable. <br>
Risk: The skill can silently derive or create an internal user identity and query cloud report history for that identity. <br>
Mitigation: Review identity linkage behavior before installation and run history lookup only in workspaces where that account association is expected. <br>
Risk: The skill stores tokens in a workspace SQLite database. <br>
Mitigation: Limit workspace access, rotate credentials if the workspace is shared or exposed, and remove local token storage when uninstalling or transferring the skill. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-outdoor-monitoring-analysis) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>
- [Outdoor Monitoring API Documentation](references/api_doc.md) <br>
- [Common Analysis API Documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands] <br>
**Output Format:** [Markdown text containing structured analysis results, JSON-formatted report data, report links, and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can write analysis output to a file when an output path is supplied; history lookup returns cloud report records.] <br>

## Skill Version(s): <br>
1.0.11 (source: server release metadata; artifact frontmatter says 1.0.9) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
