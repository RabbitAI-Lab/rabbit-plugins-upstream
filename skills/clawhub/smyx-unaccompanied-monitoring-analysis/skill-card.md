## Description:

Determines when elderly people living alone have no interaction or visitors for extended periods, and pushes care reminders to family members for remote elder-care scenarios.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External caregivers, family members, and elder-care operators use this skill to analyze home monitoring images or video for prolonged lack of interaction or visitors and to retrieve historical monitoring reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Home monitoring footage and report history are processed through cloud APIs.

Mitigation: Install and run the skill only with authorization from the monitored person or legal guardian, and confirm that cloud processing is acceptable for the care setting.

Risk: The skill can create or reuse an identity and store service tokens in the workspace data directory.

Mitigation: Review workspace data storage before deployment, restrict access to the workspace, and rotate or remove stored tokens if the skill is no longer used.

Risk: Automated unattended-monitoring alerts can miss events or produce misleading care status.

Mitigation: Use the reports as care reminders only and keep human check-ins or professional care procedures as the primary safety mechanism.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-unaccompanied-monitoring-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [Unattended monitoring API documentation](artifact/references/api_doc.md)
- [Shared analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or JSON-like text with report links; optional saved output file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports local image/video files, public media URLs, historical report listing, detail-level selection, and optional output file paths.]

## Skill Version(s):

1.0.12 (source: server release metadata; artifact frontmatter says 1.0.17)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
