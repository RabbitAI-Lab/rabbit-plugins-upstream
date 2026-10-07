## Description:

Provides handling guidance for content, prepares a review plan, and saves a local review artifact with optional configured delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Content reviewers and developers use this skill to classify a content item's handling needs, prepare a review plan, and save the plan locally. Configured delivery can submit the result to an external service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Configured delivery can send review-plan data to an arbitrary external endpoint, including when generic delivery environment variables are set.

Mitigation: Run without delivery settings unless outbound submission is intended; check both CLAWHUB_* and generic DELIVERY_ENDPOINT and DELIVERY_API_KEY variables before use.

Risk: The skill writes a review-plan CSV to the chosen output directory.

Mitigation: Use a dedicated, access-controlled output directory and review the artifact before sharing it.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/wxt-ai/skills/content-review-mode-complete)

## Skill Output:

**Output Type(s):** [Guidance, Files]

**Output Format:** [JSON response and local CSV review plan]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes local artifact and delivery receipts; external delivery requires configuration.]

## Skill Version(s):

1.2.0 (source: skill frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
