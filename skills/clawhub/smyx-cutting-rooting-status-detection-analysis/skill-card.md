## Description: <br>
AI-powered non-invasive rooting-stage detection for plant cuttings in transparent containers, using image or video inputs to identify root primordia, estimate rooting stage, and suggest transplant timing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, growers, propagation operators, and agricultural researchers use this skill to analyze images or videos of cuttings in transparent containers, monitor visible root development, and decide when continued observation or transplanting is appropriate. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Media files or remote media URLs are sent to a remote Life Emergence service for analysis. <br>
Mitigation: Use only media appropriate for that service and review organizational data-sharing requirements before deployment. <br>
Risk: The skill may silently create or reuse an account identity and read workspace identity data. <br>
Mitigation: Run it in a controlled workspace and verify identity-linkage behavior before using it with sensitive accounts or shared environments. <br>
Risk: Cloud API tokens may be persisted in a local SQLite database. <br>
Mitigation: Limit filesystem access, inspect local token storage after use, and remove stored credentials or data when no longer needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-cutting-rooting-status-detection-analysis) <br>
- [Publisher profile](https://clawhub.ai/user/smyx-sunjinhui) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [API documentation](artifact/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown or JSON-style structured analysis report with status, observations, recommendations, and report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Accepts local image or video paths, remote media URLs, and a history-list mode; documented media limit is 10 MB.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata; artifact frontmatter says 1.0.6) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
