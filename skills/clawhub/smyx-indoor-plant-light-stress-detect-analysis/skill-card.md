## Description: <br>
Detects indoor plant light stress from images or video and optional lux data, classifying insufficient, excessive, or normal light and returning adjustment suggestions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to analyze indoor plant images, videos, or URLs for signs of low-light or excessive-light stress. It returns structured findings, care suggestions, report links, and historical report listings for indoor plant care workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Plant images, video URLs, and history-report requests are sent to Lifeemergence cloud APIs. <br>
Mitigation: Use the skill only with media and URLs that are appropriate to send to that cloud service, and avoid private or sensitive imagery unless the user has authorized that transfer. <br>
Risk: The skill silently creates or reuses a local identity and stores or reuses cloud API tokens in a workspace SQLite database. <br>
Mitigation: Run it in a controlled workspace, review the workspace data directory for identity and token storage, and remove or rotate stored tokens when they are no longer needed. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-indoor-plant-light-stress-detect-analysis) <br>
- [Publisher Profile](https://clawhub.ai/user/smyx-sunjinhui) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>
- [API Documentation](references/api_doc.md) <br>
- [Analysis API Documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, files, guidance] <br>
**Output Format:** [Markdown text with structured JSON analysis content, report links, and optional saved output files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can analyze local media files or public media URLs and can list historical cloud reports associated with the resolved local identity.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata; artifact frontmatter reports 1.0.6) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
