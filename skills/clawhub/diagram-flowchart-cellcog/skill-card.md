## Description:

Flowchart helps agents use CellCog to generate flowcharts, system architecture diagrams, mind maps, org charts, ER diagrams, sequence diagrams, Gantt charts, and network diagrams from plain-English prompts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cellcog](https://clawhub.ai/user/cellcog)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, product teams, and other external users use this skill to ask an agent to create shareable interactive diagrams or print-ready PDFs from natural-language descriptions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, uploaded files, and generated diagrams are processed by CellCog and may be exposed through shareable URLs.

Mitigation: Avoid secrets, credentials, regulated data, and sensitive internal architecture unless organizational approval covers that use.

Risk: Generated diagrams can misrepresent a process, system architecture, or data model if the prompt is incomplete or incorrect.

Mitigation: Review diagram content before using it in documentation, operations, or stakeholder communications.

## Reference(s):

- [CellCog](https://cellcog.ai)
- [ClawHub skill page](https://clawhub.ai/cellcog/skills/diagram-flowchart-cellcog)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with Python and shell command examples; CellCog may produce shareable interactive HTML diagrams or PDF outputs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires python3, the cellcog dependency, and CELLCOG_API_KEY; generated diagrams may be exposed through shareable URLs.]

## Skill Version(s):

1.0.10 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
