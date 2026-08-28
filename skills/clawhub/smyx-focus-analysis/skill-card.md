## Description:

Real-time detection of gaze direction and facial pose to quantify states of focus, distraction, or mind-wandering for classroom learning, office meetings, and driving attention monitoring.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to analyze classroom, office, or driving videos for gaze, head-pose, and focus indicators, then review structured attention reports and historical report records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive videos or video URLs and identity-linked metadata are sent to the configured remote service.

Mitigation: Use the skill only with consent from people shown in the media, review the configured service before installation, and avoid processing sensitive footage unless the destination and retention practices are acceptable.

Risk: The skill creates or reuses identity state and stores account tokens in a workspace SQLite database.

Mitigation: Run it in an isolated workspace, restrict file access to the workspace data directory, and provide a process to review or delete created identity data and report history.

Risk: The shipped configuration includes dev or private-network endpoints.

Mitigation: Replace and verify endpoint configuration before use, and block unintended private-network destinations in production environments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-focus-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Files]

**Output Format:** [Markdown text or JSON; optional saved result file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include report links and historical report records returned by the configured service.]

## Skill Version(s):

1.0.13 (source: server release metadata; artifact frontmatter states 1.0.15)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
