## Description:

Identifies common pet behaviors and abnormal behavior patterns from video files or video URLs, then returns structured analysis, recommendations, and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and pet-care workflows use this skill to analyze pet monitoring videos for behaviors such as scratching, chewing, destructive behavior, jumping, digging, chasing, and separation anxiety. It can also retrieve cloud-hosted historical behavior reports associated with the account-linked identity used by the service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet videos or URLs may contain private home footage or people and are sent to lifeemergence.com services for analysis.

Mitigation: Use only content you are authorized to share, avoid sensitive footage, and review privacy requirements before upload.

Risk: The skill silently creates or reuses an account-linked identity and stores service tokens for report history.

Mitigation: Evaluate it in an isolated workspace and clear local databases or tokens according to local policy when access is no longer needed.

Risk: Behavior analysis is mixed with health-diagnosis language and may be mistaken for veterinary advice.

Mitigation: Treat the output as informational and consult a qualified veterinarian or pet behavior professional before acting on health or behavior concerns.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-pet-behavior-detection-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [API Documentation](references/api_doc.md)
- [Shared Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Files, Guidance]

**Output Format:** [Markdown reports and JSON analysis results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include report links and an optional saved output file when an output path is provided.]

## Skill Version(s):

1.0.9 (source: server release metadata; artifact frontmatter says 1.0.12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
