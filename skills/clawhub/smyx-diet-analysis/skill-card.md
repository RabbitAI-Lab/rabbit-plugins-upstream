## Description: <br>
Analyzes meal videos or video URLs for eating behavior, dietary patterns, unhealthy habit indicators, and nutrition improvement recommendations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Users and agents use this skill to submit meal videos or video URLs to the Life Emergence cloud service for dietary behavior assessment, structured nutrition guidance, and historical diet report retrieval. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Uploaded meal videos, URLs, and historical report requests are processed by a remote Life Emergence cloud service. <br>
Mitigation: Use only with media appropriate for that service, review the service's privacy and retention claims, and avoid sensitive personal or health-related videos unless the deployment has approved the data handling. <br>
Risk: The security scan reports that the skill silently creates or reuses a local identity and stores service tokens locally. <br>
Mitigation: Review local workspace data files and token storage before installation, isolate the skill in a controlled workspace, and rotate or remove stored tokens when no longer needed. <br>
Risk: The scanner verdict is suspicious because remote login, token storage, and historical report retrieval happen with limited user control or disclosure. <br>
Mitigation: Require operator review before deployment and clearly disclose remote processing and historical report access to end users. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/smyx-sunjinhui/skills/smyx-diet-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [API interface documentation](references/api_doc.md) <br>
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, shell commands, configuration] <br>
**Output Format:** [Markdown and JSON-formatted analysis reports, Markdown tables for historical reports, report links, and shell commands for invoking the skill scripts.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports mp4, avi, and mov inputs up to 10 MB; accepts local file paths or public video URLs; output detail can be basic, standard, or json.] <br>

## Skill Version(s): <br>
1.0.8 (source: evidence.release.version and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
