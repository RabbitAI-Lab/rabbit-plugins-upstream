## Description: <br>
Analyzes elderly-home monitoring images or videos for prolonged periods without interaction or visitors and returns structured monitoring reports, suggestions, and report links. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External caregivers, family-care platforms, and care-operations teams can use this skill to submit monitoring media or URLs, review unattended/visitor activity analysis, and query prior reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive elderly-home monitoring images, videos, or URLs may be sent to configured Life Emergence remote services. <br>
Mitigation: Install only in deployments approved to share this media with those services, and review data handling, retention, and access controls before use. <br>
Risk: The skill silently creates or reuses a user identity and stores tokens or report associations in the workspace data directory. <br>
Mitigation: Run it in a controlled workspace, protect stored credentials and report data, and clear workspace state when the identity should not persist. <br>
Risk: Family-reminder behavior is claimed by the release but is not proven by the local artifact alone. <br>
Mitigation: Verify the backend and deployment controls separately before relying on alerts for care response or safety-critical workflows. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-unaccompanied-monitoring-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [API interface documentation](artifact/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown or JSON analysis output with optional report links and saved output files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Accepts local image/video file paths or media URLs; history lookup returns prior report information from the configured remote service.] <br>

## Skill Version(s): <br>
1.0.6 (source: ClawHub release metadata; artifact frontmatter states 1.0.10) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
