## Description:

Turns descriptions of processes, system interactions, states, and data relationships into editable diagrams with export options.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youteacher](https://clawhub.ai/user/youteacher)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can plan, review, edit, and export flowcharts, sequence diagrams, state diagrams, entity-relationship diagrams, and architecture diagrams from natural-language descriptions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Diagram prompts and structure are sent to the configured AI Skills API.

Mitigation: Avoid secrets in prompts and protect the API key.

Risk: Generated diagrams can omit details or misrepresent relationships.

Mitigation: Have a knowledgeable user review the plan before rendering or sharing exports.

Risk: Successful operations incur charges, and uncertain task results may be billed.

Mitigation: Confirm exports with the user; reuse the original request key and input when retrying uncertain results.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/youteacher/skills/diagram-generation)
- [AI Skills platform](https://ai-skills.open-idea.net)
- [API key and pricing](https://ai-skills.open-idea.net/skill-docs/diagram-generation/API-KEY.md)
- [Diagram operations and exports](https://ai-skills.open-idea.net/skill-docs/diagram-generation/OPERATIONS.md)
- [HTTP requests and task polling](https://ai-skills.open-idea.net/skill-docs/diagram-generation/HTTP-REQUESTS.md)
- [Review and delivery boundaries](https://ai-skills.open-idea.net/skill-docs/diagram-generation/BEHAVIOR-RULES.md)

## Skill Output:

**Output Type(s):** [JSON, Files]

**Output Format:** [Structured diagram plan; SVG, PNG, PDF, or JSON exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Plans require user review before export; exported artifacts are private to the requesting user.]

## Skill Version(s):

1.0.1 (source: ClawHub release and packageVersion metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
