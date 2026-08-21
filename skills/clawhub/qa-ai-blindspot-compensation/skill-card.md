## Description:

Helps QA reviewers find missed test scenarios after AI-generated test cases by checking six recurring blind spots: sequencing, concurrency, resource contention, state accumulation, data consistency, and third-party integration differences.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kokxi](https://clawhub.ai/user/kokxi)

### License/Terms of Use:

MIT-0

## Use Case:

QA engineers, test designers, and software teams use this skill after reviewing AI-generated test cases to add blind-spot coverage for sequence changes, concurrent use, resource exhaustion, long-running state, distributed data consistency, and real third-party behavior.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may be invoked broadly during QA review and can add 12-18 extra scenarios, increasing review scope.

Mitigation: Use it when expanded test coverage analysis is desired and review the generated scenarios for relevance and priority before adding them to the test plan.

Risk: Generated supplemental test scenarios may be incorrect, low priority, or hard to execute for a specific system.

Mitigation: Validate each proposed scenario against requirements, existing test cases, and the system architecture before implementation.

## Reference(s):

- [Six Blind Spots Details](references/blindspot-details.md)
- [ClawHub Skill Page](https://clawhub.ai/kokxi/skills/qa-ai-blindspot-compensation)
- [Publisher Profile](https://clawhub.ai/user/kokxi)

## Skill Output:

**Output Type(s):** [analysis, markdown, guidance]

**Output Format:** [Markdown blind-spot coverage report with tables and test-case lists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces supplemental test scenarios with blindspot IDs, related requirement IDs, original test case IDs, blindspot type, risk level, test difficulty, and suggested test depth.]

## Skill Version(s):

1.7.0 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
