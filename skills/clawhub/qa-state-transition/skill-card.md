## Description:

QA State Transition helps agents design state-machine tests that cover valid, invalid, boundary, and concurrent transitions with trigger conditions, pre-states, post-states, and validation points.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kokxi](https://clawhub.ai/user/kokxi)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, QA engineers, and test-focused agents use this skill to turn business objects with multi-state workflows into state diagrams, legal and illegal transition coverage, boundary checks, concurrency scenarios, and traceable test cases.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated test plans may be incomplete or misleading if applied directly to payment, refund, or concurrent-operation workflows without review.

Mitigation: Review generated state-transition plans against the real requirements and data-consistency rules before using them against live or production-like systems.

Risk: Example state names in the skill could be mistaken for instructions to mutate a target system.

Mitigation: Treat examples as test-design terminology only and avoid changing system state unless a reviewed test procedure explicitly requires it.

## Reference(s):

- [qa-state-transition ClawHub release](https://clawhub.ai/kokxi/skills/qa-state-transition)
- [kokxi publisher profile](https://clawhub.ai/user/kokxi)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown or structured text containing state diagrams, transition lists, and test scenarios]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs can include ST-XXXX transition IDs, SC-XXXX scenario links, valid and invalid transition lists, boundary cases, and concurrency checks.]

## Skill Version(s):

1.7.0 (source: release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
