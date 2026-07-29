## Description: <br>
Detects potential elderly falls in home-monitoring images, videos, or media URLs and returns structured analysis, safety guidance, and report links. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and care-monitoring operators use this skill to check surveillance images or videos for possible falls by elderly people living alone. The skill can also retrieve account-linked historical fall-detection reports from the service. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Home-monitoring photos or videos and report lookup requests are sent to lifeemergence.com services. <br>
Mitigation: Install only in environments where sending this media and account-linked report requests to that service is approved. <br>
Risk: The skill may silently create or reuse a local identity and keep service tokens in a shared workspace SQLite database. <br>
Mitigation: Run it in a controlled workspace, restrict local database access, and clear stored identity or token data when no longer needed. <br>
Risk: Fall-detection results are safety alerts and may be incorrect or incomplete. <br>
Mitigation: Treat reports as warnings that require human confirmation and emergency follow-up when a fall is suspected. <br>


## Reference(s): <br>
- [API Interface Documentation](references/api_doc.md) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-elderly-fall-detection-analysis) <br>
- [Publisher Profile](https://clawhub.ai/user/18072937735) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, guidance] <br>
**Output Format:** [Markdown and structured JSON text with report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May save the rendered analysis output to a user-specified file path.] <br>

## Skill Version(s): <br>
1.0.9 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
