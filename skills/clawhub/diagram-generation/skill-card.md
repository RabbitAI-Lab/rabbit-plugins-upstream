## Description:

Turns natural-language descriptions of processes, systems, states, and data relationships into editable diagrams and exportable files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youteacher](https://clawhub.ai/user/youteacher)

### License/Terms of Use:

MIT-0

## Use Case:

OpenClaw users can plan and review flowcharts, sequence diagrams, state diagrams, entity-relationship diagrams, and architecture diagrams before exporting them for private use.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Diagram descriptions are sent to a hosted service and may contain sensitive internal designs.

Mitigation: Avoid submitting sensitive designs unless the service's privacy and billing terms meet your requirements.

Risk: An exposed API key could allow unauthorized service use.

Mitigation: Store the key in OpenClaw configuration; do not paste, log, or disclose the full key.

Risk: Generated diagrams can omit exceptions or misrepresent relationships.

Mitigation: Have someone familiar with the process or system review the nodes and relationships before export.

Risk: Private diagram exports could reveal information if shared beyond the requesting user.

Mitigation: Only deliver private artifacts to the requesting user and seek separate approval before external sharing.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/youteacher/skills/diagram-generation)
- [AI Skills platform](https://ai-skills.open-idea.net)
- [API key setup and pricing](https://ai-skills.open-idea.net/skill-docs/diagram-generation/API-KEY.md)
- [Diagram operations and export formats](https://ai-skills.open-idea.net/skill-docs/diagram-generation/OPERATIONS.md)
- [HTTP requests and task handling](https://ai-skills.open-idea.net/skill-docs/diagram-generation/HTTP-REQUESTS.md)
- [Review and delivery boundaries](https://ai-skills.open-idea.net/skill-docs/diagram-generation/BEHAVIOR-RULES.md)

## Skill Output:

**Output Type(s):** [Text, Diagram files]

**Output Format:** [Diagram plan as structured JSON; private SVG, PNG, PDF, or JSON exports on request]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Users review the proposed diagram before export; exported artifacts remain private to the requesting user.]

## Skill Version(s):

1.2.0 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
