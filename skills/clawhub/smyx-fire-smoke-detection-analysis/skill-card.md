## Description: <br>
Detects fire and smoke in images and video streams for fire early warning scenarios such as security surveillance, forest fire prevention, and industrial parks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and safety-monitoring operators use this skill to analyze uploaded images, local media files, or media URLs for flame and smoke indicators, then receive a structured fire-smoke detection report. It can also query cloud-hosted historical reports for the publisher-managed account context. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Uploaded media, supplied URLs, report history, and identity data may be processed by the publisher's cloud service. <br>
Mitigation: Use the skill only with media appropriate for that service, and confirm the publisher's retention, authorization, and account-handling practices before using sensitive facility or security footage. <br>
Risk: The skill may create or reuse a user identity and store returned tokens locally. <br>
Mitigation: Run it in an isolated workspace or account, restrict access to local state files, and rotate or revoke credentials when they are no longer needed. <br>
Risk: Fire and smoke detection output is advisory and may miss events or produce false alarms. <br>
Mitigation: Treat detections as prompts for human confirmation and follow established emergency response procedures for any suspected fire. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-fire-smoke-detection-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [API doc](references/api_doc.md) <br>
- [Smyx analysis API doc](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, configuration] <br>
**Output Format:** [Markdown summaries and tables, JSON analysis output, shell command examples, and optional saved result files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes detected fire/smoke indicators, risk notes, recommendations, cloud history tables, and report links when returned by the API.] <br>

## Skill Version(s): <br>
1.0.9 (source: server release metadata; artifact frontmatter declares 1.0.11) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
