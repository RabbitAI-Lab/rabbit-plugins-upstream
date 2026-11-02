## Description:

Monitors staff presence in defined areas using images or video, identifies absence and leaving-post events, and produces structured monitoring reports with configurable thresholds.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Operations and security teams use the skill to review workplace camera images or video for staff presence and absence events, adjust absence thresholds, and retrieve monitoring reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Monitoring reports may be mixed across users.

Mitigation: Require reliable per-user report isolation and avoid shared workspaces until identity isolation is fixed.

Risk: Uploads may run despite a no-analysis option.

Mitigation: Verify that the option prevents all processing before relying on it; avoid sending sensitive footage until confirmed.

Risk: Credentials may be retained with limited user control.

Mitigation: Restrict credential destinations and confirm account and token cleanup controls.

Risk: The provider's upload, retention, access, and charging terms may affect footage use.

Mitigation: Confirm those terms before sending footage.

Risk: Advertised instant alerts have not been validated.

Mitigation: Validate alert timing and delivery before relying on alerts for supervision.

## Reference(s):

- [API documentation](artifact/references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, Text, JSON, Markdown]

**Output Format:** [Structured monitoring reports with JSON data and Markdown report lists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include findings, recommendations, and report links.]

## Skill Version(s):

1.0.17 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
