## Description:

Turns requirement deconstruction results into a structured QA scenario tree covering happy paths, alternative paths, exception paths, data flow, and business rules with scenario IDs and requirement traceability.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kokxi](https://clawhub.ai/user/kokxi)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, QA engineers, and product teams use this skill after requirement deconstruction to design scenario trees for complex workflows. It helps cover expected, alternative, exception, and data-flow paths while keeping each scenario traceable to requirement IDs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may include real customer, payment, identity, or production data in prompts while building QA scenarios.

Mitigation: Use synthetic, anonymized, or masked data and avoid pasting production records into the agent session.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kokxi/skills/qa-scenario-tree)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Text]

**Output Format:** [Markdown scenario tree with scenario IDs, path types, preconditions, steps, expected results, data changes, risk level, and requirement traceability.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scenario IDs use SC-XXXX and should link back to REQ-XXXX requirement IDs.]

## Skill Version(s):

1.6.3 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
