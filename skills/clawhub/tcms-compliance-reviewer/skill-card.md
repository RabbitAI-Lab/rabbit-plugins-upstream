## Description:

Pre-publication compliance and quality reviewer. Checks factual citations, customer redaction, product naming, competitor rules, internal information, formatting, and AI traces; outputs a pre-review report and fix suggestions without modifying the original.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

Content, marketing, and product teams use this skill to review finished technology blogs, customer cases, product updates, or press releases before publication. It checks citations, naming, redaction, competitor mentions, internal information, formatting, and quality, then returns a pre-review report with suggested fixes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may read private compliance profiles, customer-redaction rules, and internal knowledge-base material while reviewing drafts.

Mitigation: Use it only with drafts and configurations the agent is authorized to access, and scope compliance profiles and knowledge-base access to the relevant publication workflow.

Risk: Broad review trigger phrases could activate the skill for generic review tasks where private compliance checks are not intended.

Mitigation: Narrow invocation phrases or routing rules when accidental activation on generic review tasks would be a problem.

Risk: Missing approved sources or unavailable knowledge-base sections can make data claims unverifiable.

Mitigation: Require the report to mark unverifiable data items explicitly and keep human confirmation before publication handoff.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/haiyangchenbj/skills/tcms-compliance-reviewer)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, files]

**Output Format:** [Markdown report with summary tables, issue lists, citation verification, approval recommendation, and execution summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Saves a review report without modifying the original draft.]

## Skill Version(s):

1.1.5 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
