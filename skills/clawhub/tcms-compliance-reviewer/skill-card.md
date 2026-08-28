## Description:

Pre-publication compliance and quality reviewer. Checks factual citations, customer redaction, product naming, competitor rules, internal information, formatting, and AI traces; outputs a pre-review report and fix suggestions without modifying the original.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

Content, marketing, and product teams use this skill to review finished tech blogs, customer cases, product updates, and press releases before publication. It checks compliance and quality concerns, reports issues, and suggests fixes without modifying the original draft.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may read unpublished drafts, private compliance profiles, and knowledge-base content.

Mitigation: Review workspace access before installation and ensure users understand which private materials may be read during a compliance review.

Risk: Broad trigger phrases may route unrelated review workflows to this skill.

Mitigation: Narrow trigger phrases or routing rules when the workspace contains multiple review workflows.

Risk: Compliance findings and fix suggestions may be incomplete or incorrect.

Mitigation: Require human confirmation before marking the review complete or using the report for publication approval.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/haiyangchenbj/skills/tcms-compliance-reviewer)
- [Publisher profile](https://clawhub.ai/user/haiyangchenbj)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown pre-review report with summary tables, issue lists, citation verification, approval recommendation, and execution summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Saves a separate compliance review report and does not modify the reviewed draft.]

## Skill Version(s):

1.1.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
