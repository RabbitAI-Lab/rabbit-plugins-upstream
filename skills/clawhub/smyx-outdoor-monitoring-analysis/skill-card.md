## Description: <br>
Detects people, vehicles, non-motorized vehicles, and pets in outdoor images or video, then returns structured monitoring reports for areas such as courtyards, orchards, and farms. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to analyze outdoor monitoring images, videos, or media URLs for target detection, intrusion assessment, risk levels, and history report lookup. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Media files or URLs are sent to a remote analysis service and report history is retrieved from a cloud API. <br>
Mitigation: Use only media that is appropriate to share with the remote service, review the configured service endpoints before installation, and confirm retention and deletion options for generated reports. <br>
Risk: The skill can silently resolve or create an account-linked identity and reuse it for analysis and history lookup. <br>
Mitigation: Review identity resolution behavior before use, avoid sharing internal identity values in prompts or outputs, and confirm how locally stored identity or token state can be removed. <br>
Risk: Local persistence and token handling may retain account or report-access state on the host. <br>
Mitigation: Inspect local storage paths and token caches before deployment, restrict filesystem access where possible, and rotate or clear credentials after testing. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-outdoor-monitoring-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [API interface documentation](references/api_doc.md) <br>
- [Analysis API error code documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, shell commands] <br>
**Output Format:** [Markdown text with structured JSON results and report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May save results to a user-specified output file and may include links to remotely stored reports.] <br>

## Skill Version(s): <br>
1.0.10 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
