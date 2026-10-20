## Description:

Reviews brand-side drafts before publication for citation traceability, customer redaction, product and competitor naming, internal information, formatting, and content quality without editing the draft.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

Content marketing teams use this skill to review tech blogs, customer cases, product updates, and press releases against their draft and compliance profile before human approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad activation phrases such as 'review' can invoke this skill for unrelated requests and expose private drafts or compliance profiles to an unnecessary review workflow.

Mitigation: Invoke it only for explicit pre-publication reviews with specified draft paths and compliance profiles; narrow activation phrases before deployment.

Risk: The review creates a report in content/drafts that may contain details from private drafts or compliance rules.

Mitigation: Restrict access to the draft, profile, and saved report, and have a person review the findings before publication.

## Reference(s):

- [Content Compliance Reviewer on ClawHub](https://clawhub.ai/haiyangchenbj/skills/tcms-compliance-reviewer)

## Skill Output:

**Output Type(s):** [Markdown, Guidance]

**Output Format:** [Markdown pre-review report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Saves a separate report under content/drafts with per-check results, citation status, suggested fixes, and an approval recommendation; does not edit the draft.]

## Skill Version(s):

1.1.7 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
