## Description:

Analyzes video for gaze direction, head pose, and facial landmarks to report focus, distraction, and mind-wandering signals for classrooms, meetings, and driving scenarios.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to analyze classroom, office, or driving videos for focus scores, distraction counts, trend summaries, and report links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uploads sensitive video through a cloud API.

Mitigation: Use only with clear consent and disclose where video is sent, how reports are stored, and what retention and access controls apply.

Risk: Security evidence reports plaintext HTTP defaults and plaintext bearer-token storage in the workspace.

Mitigation: Install only after the publisher requires HTTPS-only production endpoints and avoids plaintext bearer-token storage.

Risk: Security evidence reports silent account creation and token handling.

Mitigation: Require explicit account linkage or consent before enabling analysis or history lookup.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-focus-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API interface documentation](references/api_doc.md)
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, guidance]

**Output Format:** [Markdown or JSON analysis report with structured results and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include focus scores, distraction counts, trend summaries, improvement suggestions, and cloud report export links.]

## Skill Version(s):

1.0.14 (source: server-resolved release metadata; artifact frontmatter says 1.0.18)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
