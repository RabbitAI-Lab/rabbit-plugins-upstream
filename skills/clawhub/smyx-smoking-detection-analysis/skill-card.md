## Description:

Detects smoking behavior in target areas from image, video, or stream inputs, then returns structured detection results, violation alerts, management suggestions, and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users, safety teams, and facility managers use this skill to analyze public-area media for smoking behavior and retrieve structured reports for smoking-control and fire-safety workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill creates or reuses a cloud identity before analysis or history retrieval.

Mitigation: Require explicit user consent and document how cloud identity, report association, and account reuse are handled.

Risk: The skill uploads media and retrieves report history through third-party cloud APIs.

Mitigation: Review data handling, retention, and access controls before using sensitive video or image content.

Risk: The security evidence reports unsafe defaults for endpoints and token handling.

Mitigation: Use HTTPS production endpoints, remove development HTTP defaults from deployment, and store tokens securely.

Risk: The release has a suspicious security verdict.

Mitigation: Review the publisher, configuration, and runtime behavior before installation or deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-smoking-detection-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API documentation](references/api_doc.md)
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown and JSON-formatted structured reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include violation alerts, recommendations, history records, and report links; local media handling enforces a 10 MB file-size limit.]

## Skill Version(s):

1.0.13 (source: server release metadata; artifact frontmatter says 1.0.16)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
