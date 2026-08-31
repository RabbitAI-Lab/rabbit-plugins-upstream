## Description:

This skill helps agents review AI-generated test cases for six recurring QA blind spots: sequencing dependencies, concurrency conflicts, resource contention, state accumulation, data consistency, and third-party integration differences.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kokxi](https://clawhub.ai/user/kokxi)

### License/Terms of Use:

MIT-0

## Use Case:

QA engineers, test engineers, and development teams use this skill after reviewing AI-generated test cases to identify missing scenarios across known blind spot categories and add traceable supplemental tests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can expand test scope when invoked by broad missing-coverage prompts.

Mitigation: Use it after initial test-case review and require each added scenario to remain traceable to provided requirements, risks, or original test-case IDs.

Risk: Supplemental QA scenarios may be irrelevant or overstate coverage if the source requirements are incomplete.

Mitigation: Review generated additions before adoption and avoid absolute coverage claims unless the input evidence supports them.

## Reference(s):

- [Blindspot Details](references/blindspot-details.md)
- [ClawHub Skill Page](https://clawhub.ai/kokxi/skills/qa-ai-blindspot-compensation)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Markdown report with coverage tables and supplemental test-case entries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs include blindspot IDs, related requirement IDs, related original test-case IDs, blindspot type, risk level, and supplemental test cases.]

## Skill Version(s):

1.7.5 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
