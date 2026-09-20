## Description:

Pre-publication compliance and quality reviewer. Checks factual citations, customer redaction, product naming, competitor rules, internal information, formatting, and AI traces; outputs a pre-review report and fix suggestions without modifying the original.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

Brand-side tech-product marketing teams use this skill to review finished blogs, case studies, product updates, and press releases before publication. It checks compliance and quality issues, then produces a separate pre-review report with issue locations, suggested fixes, citation verification, and an approval recommendation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generic review and fact-check triggers may route private drafts, compliance profiles, or knowledge-base material into this workflow.

Mitigation: Install and invoke the skill only for intended brand-side pre-publication review, and confirm that access to private compliance profiles is appropriate for the review request.

Risk: Reviews can be incomplete when the compliance profile, product policy, or knowledge-base section is missing or outdated.

Mitigation: Treat missing sources as incomplete or unverifiable, request updated profile material, and require human confirmation before handoff.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/haiyangchenbj/skills/tcms-compliance-reviewer)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown pre-review report saved as a separate file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Does not modify the source draft; report includes pass, needs-fix, or fail results for each check and an execution summary.]

## Skill Version(s):

1.1.6 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
