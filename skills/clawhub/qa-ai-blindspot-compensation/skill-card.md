## Description:

Reviews AI-generated QA test cases against six common blind spots and proposes traceable scenarios to address gaps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kokxi](https://clawhub.ai/user/kokxi)

### License/Terms of Use:

MIT-0

## Use Case:

QA engineers and developers use this Chinese-language checklist after reviewing AI-generated test cases to find missing scenarios involving ordering, concurrency, resource limits, accumulated state, data consistency, and external integrations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad coverage questions may activate the skill outside a test-case review.

Mitigation: Use it when reviewing test cases or requirements, and confirm the requested scope before generating additions.

Risk: Suggested scenarios may be irrelevant or create a misleading impression of complete coverage.

Mitigation: Check proposals against requirements and existing cases, retain traceability, and state the basis and limits of any coverage claim.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/kokxi/skills/qa-ai-blindspot-compensation)
- [Six blind spots reference](artifact/references/blindspot-details.md)

## Skill Output:

**Output Type(s):** [Analysis, Test case guidance]

**Output Format:** [Chinese-language Markdown report and test-case tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Identifies blind-spot categories, proposed cases, risk levels, and links to original cases and requirements.]

## Skill Version(s):

1.7.7 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
