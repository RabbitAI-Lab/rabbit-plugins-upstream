## Description:

Analyzes pet race start and finish media to identify start timing, lane assignment, finish order, false starts, and lane-crossing fouls, returning objective judgment results for referee review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External event organizers, referees, and trainers use this skill to analyze pet racing videos or URLs for false starts, lane crossing, finish order, and supporting evidence. The results are intended to assist race officials, with final decisions remaining with the event referee.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Race media and report history are processed by the publisher's cloud service.

Mitigation: Use the skill only with media and report data approved for third-party cloud processing.

Risk: The skill creates or reuses a local identity and stores account tokens in a workspace SQLite database.

Mitigation: Install only in workspaces where local identity and token storage are acceptable, and review local storage handling before use.

Risk: Cloud report history can be retrieved without clear user control.

Mitigation: Limit use to intended accounts and review report-history access expectations before enabling history lookup.

Risk: Race foul analysis is an automated referee aid and may not match event rules or on-site judgment.

Mitigation: Treat outputs as supporting evidence and keep final race decisions with qualified event officials.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-race-foul-detection-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API interface documentation](references/api_doc.md)
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON-style structured analysis reports with report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include historical report tables and cloud report URLs when history lookup is requested.]

## Skill Version(s):

1.0.8 (source: server release metadata; artifact frontmatter says 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
