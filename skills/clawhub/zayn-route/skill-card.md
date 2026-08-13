## Description:

Routes complex workplace tasks to the appropriate WorkFn skill, reuses existing evidence, and plans skill order, parameter passing, stop conditions, and next business actions across customer, quoting, order, support, collaboration, market, and business intelligence scenarios.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zaynpeng](https://clawhub.ai/user/zaynpeng)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and business operators use this skill when a request may require one or more WorkFn skills and they need a clear routing decision, parameter status table, execution order, stop condition, and handoff plan. It is especially useful when task boundaries, company identity, market scope, or downstream skill dependencies are unclear.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may treat routing advice as permission to automatically run downstream skills or business actions.

Mitigation: Keep downstream skill execution, scraping, outreach, deletion, and material changes behind explicit user approval and scoped data access.

Risk: Weak or incomplete business evidence may be passed forward as a firm conclusion.

Mitigation: Preserve source, date, fact-versus-inference status, conflicts, and missing information; stop when required identifiers, market scope, or evidence quality are insufficient.

Risk: A simple task may be over-routed into an unnecessary multi-skill chain.

Mitigation: Apply the single-skill-first rule and only recommend multi-skill chains when the task has real stage dependencies and clear handoff requirements.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zaynpeng/skills/zayn-route)
- [README](artifact/README.md)
- [Examples](artifact/examples.md)
- [Tests](artifact/tests.md)
- [Changelog](artifact/changelog.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, configuration]

**Output Format:** [Markdown guidance with parameter status tables and routing-chain tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Advisory output only; it recommends next steps and stop conditions but does not execute downstream skills.]

## Skill Version(s):

1.0.7 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
