## Description: <br>
Analyzes privacy-conscious bathroom doorway or silhouette video to detect elderly toilet entry and exit events, estimate continuous occupancy time, and alert when the stay exceeds a configured threshold such as 30 minutes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External caregivers, family members, nursing-home operators, and home-safety integrators use this skill to monitor toilet occupancy duration from approved camera feeds and surface abnormal-stay alerts for human follow-up. It provides safety monitoring support and does not provide medical diagnosis or emergency-response instructions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Bathroom monitoring video and history are highly sensitive and are processed through configured cloud services. <br>
Mitigation: Deploy only with monitored-person or legal-guardian consent, confirm cloud processing is acceptable, prefer doorway placement or silhouette-only capture, and apply blur or pixelation where internal bathroom capture is unavoidable. <br>
Risk: Local identity, account, token, and monitoring-history linkage can be stored in the workspace SQLite database. <br>
Mitigation: Treat the local data directory as sensitive, restrict filesystem access, avoid shared default identities in real deployments, and scope each household or user identity separately. <br>
Risk: URL-based inputs can cause configured services to retrieve monitoring media from external locations. <br>
Mitigation: Accept only trusted video URLs and approved media sources, and verify that the configured lifeemergence.com service endpoints are appropriate for the deployment environment. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-elderly-toilet-time-abnormal-analysis) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>
- [API Documentation](artifact/references/api_doc.md) <br>
- [Common Analysis API Documentation](artifact/skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Files] <br>
**Output Format:** [Markdown status text with structured JSON analysis content, alert details, history-list output, report links, and optional saved output files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Local video inputs are validated for supported formats and size before cloud submission; URL inputs are passed to the configured service for retrieval.] <br>

## Skill Version(s): <br>
1.0.6 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
