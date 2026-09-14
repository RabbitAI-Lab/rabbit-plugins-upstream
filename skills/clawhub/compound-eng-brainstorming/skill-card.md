## Description:

ia-brainstorming guides pre-implementation exploration through deep interview, approach comparison, and design-doc capture for vague feature ideas or ambiguous requirements.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this workflow to clarify ambiguous feature ideas, compare implementation approaches, and produce a design handoff before planning or coding.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow may read project context and create design guidance that influences later implementation decisions.

Mitigation: Review generated summaries and design documents before using them for planning or implementation.

Risk: Design work involving auth, payments, external APIs, or multi-tenant data can miss important security or trust-boundary concerns.

Mitigation: Run an appropriate security threat-model review before planning sensitive changes.

Risk: Headless use can turn unresolved assumptions into design direction if the caller does not provide a clear decision scope.

Mitigation: Use headless mode only with explicit delegation and record unresolved assumptions for review.

## Reference(s):

- [Deep Interview Layer](references/deep-interview.md)
- [Design capture and handoff](references/design-and-handoff.md)
- [Interview and approach selection](references/interview-and-approaches.md)
- [Pre-write scope synthesis](references/scope-synthesis.md)
- [ClawHub skill page](https://clawhub.ai/iliaal/skills/compound-eng-brainstorming)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown guidance and design documentation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create a docs/brainstorms design file when a durable artifact is warranted.]

## Skill Version(s):

4.5.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
