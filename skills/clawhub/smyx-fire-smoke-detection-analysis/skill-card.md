## Description: <br>
Detects fire and smoke in video scenes, including video streams and images, for early warning scenarios such as security surveillance, forest fire prevention, and industrial parks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to submit images, video files, or media URLs for cloud-backed fire and smoke detection, then receive structured risk results, report links, or historical report listings. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Media files or URLs may be sent to a LifeEmergence cloud backend for analysis. <br>
Mitigation: Use the skill only with media that is approved for cloud processing and avoid submitting sensitive footage unless the backend terms and data handling are acceptable. <br>
Risk: Report history is associated with an internally resolved identity. <br>
Mitigation: Confirm that identity-linked report retention is acceptable before using historical report listing or report export features. <br>
Risk: Tokens may be cached in a workspace SQLite database. <br>
Mitigation: Install and run the skill only in workspaces where local credential persistence is allowed, and clear the workspace database when deprovisioning access. <br>
Risk: Fire and smoke analysis is an early-warning aid rather than an emergency determination. <br>
Mitigation: Treat alerts as prompts for human confirmation and follow the applicable emergency response plan. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-fire-smoke-detection-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [API documentation](references/api_doc.md) <br>
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, files] <br>
**Output Format:** [Markdown report, Markdown table, or JSON depending on the selected detail level; optional output file when requested.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports may include detection status, risk level, sensitivity, region details, alerts, and cloud report links.] <br>

## Skill Version(s): <br>
1.0.10 (source: server release metadata; artifact frontmatter says 1.0.11) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
