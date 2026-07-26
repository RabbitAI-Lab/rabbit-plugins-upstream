## Description: <br>
Detects fire and smoke in video scenes, supporting video stream and image analysis for fire early warning scenarios such as security surveillance, forest fire prevention, and industrial parks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and operations teams use this skill to analyze video streams, images, local files, or media URLs for fire and smoke indicators and receive structured detection reports, alerts, recommendations, and report links. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Surveillance or facility media may be uploaded to the lifeemergence.com cloud service for analysis. <br>
Mitigation: Use only media that is approved for that provider, and confirm retention, access, and data handling expectations before processing sensitive footage. <br>
Risk: The skill silently creates or reuses cloud-linked identity state and stores local user or token data. <br>
Mitigation: Review local identity and token storage, use scoped accounts, and clear stored state on shared or decommissioned environments. <br>
Risk: Cloud history retrieval and exported report links may expose operational detection history. <br>
Mitigation: Verify account separation and access controls before querying history, and avoid sharing exported report links outside approved channels. <br>


## Reference(s): <br>
- [API documentation](references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-fire-smoke-detection-analysis) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, files] <br>
**Output Format:** [Markdown or JSON analysis report with optional saved output file and cloud report link] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports may include fire and smoke detection status, risk level, sensitivity, region details, alert messages, history tables, and exported report links.] <br>

## Skill Version(s): <br>
1.0.8 (source: server release metadata; artifact frontmatter states 1.0.9) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
