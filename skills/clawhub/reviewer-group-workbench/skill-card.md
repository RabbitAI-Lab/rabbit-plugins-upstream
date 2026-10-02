## Description:

Register a request reviewer group and record the resulting review request locally.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Teams handling request governance use this skill to select a reviewer group, receive its review request details, and save a local record for handoff.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Review-request details are written to a local output directory.

Mitigation: Choose a dedicated, appropriately protected output directory for the business record.

Risk: A local queued record may be mistaken for an externally submitted review request.

Mitigation: Treat the result as a local record and confirm any external handoff separately.

## Reference(s):

- [Request Review Register on ClawHub](https://clawhub.ai/wxt-ai/skills/reviewer-group-workbench)

## Skill Output:

**Output Type(s):** [JSON, Files]

**Output Format:** [JSON response and local JSONL review-request record]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes reviewer group, queue, due time, request ID, and a local file receipt; does not submit a review externally.]

## Skill Version(s):

1.1.0 (source: frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
