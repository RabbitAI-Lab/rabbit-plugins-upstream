## Description:

Generate valid Mermaid diagrams such as flowcharts, architecture diagrams, sequence diagrams, mind maps, ER diagrams, user journeys, state machines, and timelines from text or product descriptions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pupujanet-eng](https://clawhub.ai/user/pupujanet-eng)

### License/Terms of Use:

MIT-0

## Use Case:

Product managers, developers, and other external users use this skill to turn text, PRDs, workflows, system interactions, and data models into Mermaid diagram code.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad diagram-related Chinese keywords may activate the skill in general diagram requests.

Mitigation: Confirm the user wants Mermaid diagram code before applying the skill to ambiguous diagram requests.

Risk: Generated Mermaid syntax can be incorrect or misleading for complex diagrams.

Mitigation: Review the generated Mermaid code and preview it in a Mermaid renderer before relying on the diagram.

## Reference(s):

- [Mermaid Diagram Skill Page](https://clawhub.ai/pupujanet-eng/skills/mermaid-diagram)
- [diagram-patterns.md](references/diagram-patterns.md)

## Skill Output:

**Output Type(s):** [Markdown, Code, Guidance]

**Output Format:** [Markdown with Mermaid code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses Mermaid syntax and may use Chinese labels when the user writes in Chinese.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
