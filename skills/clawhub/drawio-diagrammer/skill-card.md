## Description: <br>
Generate beautiful draw.io diagrams with a mandatory visual QA loop. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[spotlight-revenue](https://clawhub.ai/user/spotlight-revenue) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and business users use this skill to have an agent create or update draw.io diagrams for workflows, ERDs, architecture, UML classes, and sequences, then visually inspect exported diagrams before delivery. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may invoke for broad visualization requests and create local diagram files. <br>
Mitigation: Review the requested diagram scope and generated files before accepting, moving, or sharing them. <br>
Risk: The workflow depends on a local draw.io CLI export path that may differ across operating systems. <br>
Mitigation: Confirm draw.io or xvfb-run drawio is installed and adjust export commands for the local environment before running them. <br>
Risk: Cloud or share-link delivery can expose finished diagrams outside the local workspace. <br>
Mitigation: Review destination URLs and permissions before asking the agent to move or share exported diagrams. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/spotlight-revenue/skills/drawio-diagrammer) <br>
- [Box Style Standards](artifact/references/box-style-standards.md) <br>
- [Visual Review Protocol](artifact/references/visual-review-protocol.md) <br>
- [Diagram Workflow SOP](artifact/references/workflow-sop.md) <br>
- [ERD / Database Diagram](artifact/references/diagram-types/erd.md) <br>
- [UML Class Diagram](artifact/references/diagram-types/class.md) <br>
- [Sequence Diagram](artifact/references/diagram-types/sequence.md) <br>
- [Flowchart / Process Flow / SOP](artifact/references/diagram-types/flowchart.md) <br>
- [Architecture / System Diagram](artifact/references/diagram-types/layout.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with draw.io XML, shell commands, and generated diagram files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces local .drawio diagrams and exported image or document formats when the required draw.io CLI is available.] <br>

## Skill Version(s): <br>
0.1.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
