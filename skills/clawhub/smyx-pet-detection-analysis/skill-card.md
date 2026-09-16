## Description:

Detects cats, dogs, and birds in a target area from images or video streams for home pet monitoring, and can return structured detection reports and report-history results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to analyze home-monitoring media for cats, dogs, and birds, count detected animals, and retrieve cloud-hosted pet detection reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uploads home-monitoring media and retrieves account-linked report history through a third-party cloud service.

Mitigation: Install and run it only when the publisher and Life Emergence cloud service are trusted for this media and report-history data.

Risk: Security review flagged cloud account handling, default HTTP endpoints, stored tokens, and payment prompts as review-worthy.

Mitigation: Require HTTPS-only production endpoints, secure token storage, and explicit user confirmation for report-history and payment-related workflows before broad use.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-pet-detection-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [API Documentation](references/api_doc.md)
- [Shared Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown or JSON text, with optional report links and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports basic, standard, and JSON detail levels; may write output text to a user-specified file.]

## Skill Version(s):

1.0.13 (source: server release metadata; artifact frontmatter reports 1.0.15)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
