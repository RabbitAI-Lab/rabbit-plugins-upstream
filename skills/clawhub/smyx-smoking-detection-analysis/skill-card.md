## Description: <br>
Automatically detects smoking behavior in images, video files, and video streams, then returns structured detection results, alerts, recommendations, and report links for smoking-control management. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Facility, community, park, and workplace operators can use this skill to analyze submitted public-space images, videos, or video URLs for suspected smoking behavior and review generated management reports. Agents can also query cloud-hosted historical smoking-detection reports for the current managed identity. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Submitted images, videos, or media URLs are processed by the publisher's remote service. <br>
Mitigation: Use only media you are authorized to send to that service, and review publisher service terms before using workplace, public-space, or personally identifiable footage. <br>
Risk: Report history is associated with an automatically managed identity. <br>
Mitigation: Treat report history as account-linked data and avoid using the skill where silent identity creation or association conflicts with your privacy or compliance requirements. <br>
Risk: The skill stores generated user records and session tokens locally. <br>
Mitigation: Run it in a controlled workspace, protect local data directories, and remove stored records or tokens when they are no longer needed. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/smyx-sunjinhui/skills/smyx-smoking-detection-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [API documentation](references/api_doc.md) <br>
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, guidance] <br>
**Output Format:** [Markdown or JSON-style structured analysis reports with optional saved output files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include report links, historical report tables, alerts, confidence details, and management recommendations.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release metadata; artifact frontmatter declares 1.0.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
