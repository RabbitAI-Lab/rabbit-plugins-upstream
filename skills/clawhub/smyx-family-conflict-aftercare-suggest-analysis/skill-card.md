## Description: <br>
This skill analyzes household public-area audio-video to detect family conflict signals and produce structured reports with calm-window aftercare suggestions or safety-resource escalation when redline conditions appear. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to process family living-room, kitchen, or dining-area video inputs, query prior reports, and receive structured conflict-level, calm-window, aftercare, and safety-resource guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Household microphone-enabled video and family conflict reports are highly sensitive and may be processed or retained in cloud services. <br>
Mitigation: Install only with explicit household consent, restrict use to public household areas, protect report links and local files, and confirm retention and deletion controls before use. <br>
Risk: Hidden identity handling, local token persistence, and cloud history access can make it hard for users to understand or control identity-linked report history. <br>
Mitigation: Prefer deployments with visible identity selection, clear opt-out or local-only options, and documented history deletion and retention behavior. <br>
Risk: Conflict detection and aftercare suggestions may be incorrect or inappropriate during safety-critical family situations. <br>
Mitigation: Review outputs before acting on them, do not treat the skill as counseling or relationship scoring, and route suspected violence, minors in danger, injuries, or dangerous objects to safety resources rather than aftercare prompts. <br>


## Reference(s): <br>
- [API interface documentation](artifact/references/api_doc.md) <br>
- [Shared analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown and JSON-style structured analysis reports with optional report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can output current analysis results, saved report files, or Markdown tables for cloud history queries.] <br>

## Skill Version(s): <br>
1.0.3 (source: ClawHub release metadata; artifact frontmatter states 1.0.9) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
