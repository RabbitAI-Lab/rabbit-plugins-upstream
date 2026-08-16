## Description:

Identifies common abnormal pet behaviors in pet media, including scratching, biting, destructive chewing, jumping, digging, chasing, and separation anxiety, and returns a structured report for pet owners.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to analyze pet monitoring videos or video URLs, identify common behavior patterns, and retrieve current or historical behavior-analysis reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet videos, image or video URLs, account-linked identifiers, cloud history, and API tokens may be sent to or managed by the configured cloud service.

Mitigation: Install only after reviewing the publisher's data-retention claims, restrict access to the workspace data directory, and avoid using private home-monitoring media unless this data handling is acceptable.

Risk: Health or medical-style report content may be mistaken for professional veterinary diagnosis.

Mitigation: Treat analysis output as informational and consult a qualified veterinarian or pet behavior professional before making care decisions.

Risk: The skill can create or reuse a local identity database and cache account tokens for cloud API calls.

Mitigation: Review and rotate stored credentials when appropriate, remove local identity data before sharing the workspace, and run the skill in an isolated environment for sensitive media.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-pet-behavior-detection-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [Pet analysis API documentation](artifact/references/api_doc.md)
- [Shared analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands]

**Output Format:** [Markdown report text or JSON, with optional file output when requested.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include report export links; local uploads are limited to mp4, avi, or mov files up to 10 MB.]

## Skill Version(s):

1.0.10 (source: server release metadata; artifact frontmatter says 1.0.12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
