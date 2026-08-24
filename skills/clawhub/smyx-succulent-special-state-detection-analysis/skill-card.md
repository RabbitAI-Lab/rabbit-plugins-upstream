## Description:

Detects black rot, water-soaked leaf melting, and stretching in succulent plant images or videos, then returns the detected condition, severity, confidence, and report output.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users, growers, greenhouse operators, and flower shop staff can use this skill to analyze succulent photos or videos for black rot, melting, and stretching. The skill supports image or video submissions, URL-based inputs, and cloud history lookups for previous reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Plant images, videos, or media URLs may be sent to a configured cloud analysis service.

Mitigation: Use non-sensitive media, avoid private URLs, and confirm endpoint configuration and retention expectations before deployment.

Risk: Cloud history is associated with an internal identity and local workspace data may retain user or token information.

Mitigation: Run only in trusted workspaces, restrict shared access, and protect or clear local data stores according to policy.

Risk: The authoritative security scan verdict is suspicious due to silent identity use, local token storage, media transfer to a cloud API, and automatic cloud history queries.

Mitigation: Install only after reviewing the publisher, service configuration, token handling, and whether automatic history lookup is acceptable for the target environment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-succulent-special-state-detection-analysis)
- [Succulent special-state detection API documentation](artifact/references/api_doc.md)
- [Shared AI analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, json]

**Output Format:** [Markdown text with structured JSON analysis content and optional report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save the returned report text to a user-specified output file.]

## Skill Version(s):

1.0.9 (source: server release metadata; artifact frontmatter reports 1.0.10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
