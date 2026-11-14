## Description:

Drafts tests, selector repair suggestions, flaky test diagnoses, and coverage guidance for QA engineers and developers to review and run in their own environment.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gechengling](https://clawhub.ai/user/gechengling)

### License/Terms of Use:

MIT-0

## Use Case:

QA engineers and developers use the skill to draft unit, integration, API, and end-to-end tests; diagnose flaky failures; suggest selector updates; and prioritize coverage gaps. Its outputs are advisory drafts for human review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review was partial because three local references could not be resolved.

Mitigation: Resolve and review those references before relying on the security verdict.

Risk: Generated tests or selector suggestions may encode incorrect expectations or target the wrong element.

Mitigation: Check suggestions against the requirements and current interface, then have a reviewer approve them before merging.

Risk: Visual testing services may receive screenshots, DOM snapshots, or test data containing sensitive information.

Mitigation: Use synthetic data, minimize and redact captures, and confirm vendor retention and access controls before upload; keep visual testing self-hosted if those controls are unclear.

## Reference(s):

- [Agentic Test Engineer on ClawHub](https://clawhub.ai/gechengling/skills/agentic-test-engineer)
- [Publisher profile: gechengling](https://clawhub.ai/user/gechengling)

## Skill Output:

**Output Type(s):** [Code, Analysis, Guidance, Configuration instructions]

**Output Format:** [Markdown with structured tables and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Advisory drafts for human review; does not execute tests or modify repositories.]

## Skill Version(s):

1.0.3 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
