## Description: <br>
Generate beautiful draw.io diagrams with a mandatory visual QA loop. Covers flowcharts, ERD, architecture, sequence, and class diagrams. Use when user requests any diagram or visualization. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[samaustin222](https://clawhub.ai/user/samaustin222) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and other agent users use this skill to create or update draw.io diagrams for workflows, databases, systems, UML classes, and sequences. The skill guides the agent through type selection, XML generation, export, and visual review before delivery. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill creates local diagram files and runs draw.io export commands, so unclear output folders, filenames, or custom storage locations can cause files to be written or exported somewhere unintended. <br>
Mitigation: Confirm the output folder, filenames, and export command before execution, especially when names or storage locations come from untrusted input. <br>
Risk: Generated diagrams can contain visual defects such as text overflow, cramped spacing, or arrow collisions that make the result hard to understand. <br>
Mitigation: Run the documented export, crop, inspect, fix, and re-export visual review loop before delivering diagram outputs. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/samaustin222/skills/drawio-diagrammer-skill) <br>
- [Box Style Standards](references/box-style-standards.md) <br>
- [Visual Review Protocol](references/visual-review-protocol.md) <br>
- [Diagram Workflow SOP](references/workflow-sop.md) <br>
- [Flowchart / Process Flow / SOP](references/diagram-types/flowchart.md) <br>
- [ERD / Database Diagram](references/diagram-types/erd.md) <br>
- [Architecture / System Diagram](references/diagram-types/layout.md) <br>
- [UML Class Diagram](references/diagram-types/class.md) <br>
- [Sequence Diagram](references/diagram-types/sequence.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration instructions, Files, Guidance] <br>
**Output Format:** [Markdown guidance with XML snippets, shell commands, and generated diagram files such as .drawio, PNG, SVG, or PDF] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a local draw.io installation or Linux/headless drawio export tooling for rendered exports.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
