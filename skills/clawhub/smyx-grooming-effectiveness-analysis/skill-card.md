## Description: <br>
Analyzes pet grooming images or videos with server-side APIs to report coat condition, matting, shed-hair volume, grooming effectiveness, hairball risk, and related care guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agent operators use this skill to analyze pet grooming area images, videos, local files, or media URLs and receive structured coat-condition, matting, shed-hair, grooming-effectiveness, and hairball-risk reports. It can also query cloud-hosted historical grooming reports associated with the skill's internal account identity. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Pet images, videos, or supplied media URLs are sent to lifeemergence.com/open.lifeemergence.com services for analysis. <br>
Mitigation: Use only media the user is authorized to submit, and install the skill only when remote processing by those services is acceptable. <br>
Risk: The skill automatically creates or reuses a remote-linked identity, stores API tokens in a local workspace database, and uses that identity to retrieve cloud history reports. <br>
Mitigation: Install only in workspaces where local token storage and cloud history retrieval are acceptable, and remove the local workspace state when the skill is decommissioned. <br>
Risk: The security scan verdict is suspicious because of remote identity handling and local token storage. <br>
Mitigation: Review the security summary and guidance before installation, and limit deployment to environments where those behaviors are approved. <br>


## Reference(s): <br>
- [API 接口文档](references/api_doc.md) <br>
- [API接口文档](skills/smyx_analysis/references/api_doc.md) <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-grooming-effectiveness-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, guidance] <br>
**Output Format:** [Markdown reports and JSON-formatted analysis results, optionally written to a file] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include report links and Markdown tables for cloud history queries.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
