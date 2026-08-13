## Description:

A Chinese-language QA review skill that helps testers challenge assumptions, uncover hidden constraints, and identify missed test scenarios through critical-thinking prompts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kokxi](https://clawhub.ai/user/kokxi)

### License/Terms of Use:

MIT-0

## Use Case:

QA engineers, testers, and developers use this skill to review requirements and test cases for hidden assumptions, abnormal flows, boundary cases, concurrency issues, state transitions, and cross-system contract risks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User prompts may include real production identifiers, payment details, screenshots, phone numbers, customer records, or other sensitive QA data.

Mitigation: Mask or remove production and customer data before using the skill, consistent with the release security guidance and artifact warning.

Risk: Generated QA critiques and scenario suggestions may be incomplete or misleading if accepted without review.

Mitigation: Review outputs against the source requirements, system behavior, and risk model before adding or changing test coverage.

## Reference(s):


## Skill Output:

**Output Type(s):** [guidance, markdown, text]

**Output Format:** [Markdown or structured text with assumption gaps, assumption challenges, alternative scenarios, and risk reevaluation notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces review guidance and scenario suggestions; does not execute commands or persist data.]

## Skill Version(s):

1.6.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
