## Description:

Analyzes fixed smart-home living-room camera footage from the first 30 minutes after a commuter arrives home to estimate fatigue-related posture, facial, and sighing signals, then produces structured fatigue-care results and gentle care suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External smart-home users and developers use this skill to analyze home-arrival video or video URLs for fatigue indicators, produce a fatigue index and care recommendations, and list historical care reports. It is intended for personal wellness support, not medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private home camera footage and optional audio may expose sensitive household behavior.

Mitigation: Require clear user consent before uploads or history queries, minimize retained data, and provide controls to disable automatic triggers and actions.

Risk: Unsafe unencrypted service settings could expose requests or data in non-production configurations.

Mitigation: Use HTTPS-only production configuration and restrict API destinations before deployment.

Risk: Silent identity/account storage and local service tokens can reduce user control over account binding and retention.

Mitigation: Provide visible controls for account binding, token deletion, retention limits, and report-history deletion.

Risk: Fatigue-care outputs could be misused as medical or workplace performance conclusions.

Mitigation: Present results only as personal wellness support, avoid medical diagnosis, and do not share fatigue data with employers, insurers, or other third parties.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-commuter-fatigue-care-analysis)
- [API documentation](artifact/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance]

**Output Format:** [Markdown or JSON analysis report with optional report links and saved text output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports local video input, video URL input, detail level selection, and history listing.]

## Skill Version(s):

1.0.9 (source: server release metadata; artifact frontmatter reports 1.0.13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
