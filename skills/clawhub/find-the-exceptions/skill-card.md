## Description:

Find the Exceptions helps agents pressure-test a rule, decision table, SOP, requirement, or business process by identifying material edge cases and alternative branches that would break a happy-path specification before automation or formalization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[raguets](https://clawhub.ai/user/raguets)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operations teams, and process owners use this skill before automation or formalization to expose material non-happy paths in business rules, SOPs, decision tables, requirements, and workflows. The skill guides the agent to convert resolved exceptions into decision-table or state-model branches while marking unresolved policy branches as UNKNOWN.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent may identify exception branches from incomplete or stale process materials.

Mitigation: Review the output against authoritative process documentation before automation, and keep unsupported branches marked UNKNOWN until an owner resolves them.

Risk: The skill may prompt inspection of process materials provided by the user.

Mitigation: Provide only materials appropriate for the agent session and rely on the disclosed scope: exception analysis without added executable capabilities.

## Reference(s):

- [Exception Lenses](references/exception-lenses.md)
- [Overpowered skill suite](https://github.com/raguets/overpowered)
- [ClawHub skill page](https://clawhub.ai/raguets/skills/find-the-exceptions)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown table plus concise bullet lists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The expected table columns are Condition, Expected path, Exception path, Status, and Evidence / decision needed; outputs also summarize discovered rules, unresolved branches, and edge cases safe to defer.]

## Skill Version(s):

1.0.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
