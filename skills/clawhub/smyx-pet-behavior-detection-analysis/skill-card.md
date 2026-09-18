## Description:

Identifies common abnormal pet behaviors such as scratching, biting, destructive chewing, jumping, digging, chasing, and separation anxiety, helping owners understand their pet's habits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners and developers use this skill to analyze pet monitoring videos or URLs, recognize common abnormal behaviors, and return structured behavior reports, recommendations, report links, or historical report summaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet-monitoring videos or URLs and an internal user identifier are sent to the publisher's cloud service.

Mitigation: Use the skill only with media that is appropriate to share with the publisher's service, and review the service's data handling expectations before installation.

Risk: The release is flagged as suspicious because it silently manages identity, stores tokens locally, and appears configured for development HTTP endpoints.

Mitigation: Review configuration and token storage before use, and restrict deployment to environments where those behaviors are acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-pet-behavior-detection-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API documentation](references/api_doc.md)
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, files, guidance]

**Output Format:** [Markdown and JSON analysis reports, with optional file output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can query cloud-hosted historical reports and return report links.]

## Skill Version(s):

1.0.13 (source: server release metadata; artifact frontmatter reports 1.0.18)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
