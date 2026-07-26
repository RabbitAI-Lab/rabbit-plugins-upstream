## Description: <br>
Generate professional draw.io diagrams for flowcharts, ERDs, architecture diagrams, sequence diagrams, and class diagrams, with a required visual QA loop before delivery. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[spotlight-revenue](https://clawhub.ai/user/spotlight-revenue) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, architects, and operators use this skill to have an agent create or update editable draw.io diagrams and preview images for workflows, systems, databases, and UML-style designs. It is suited to diagram requests where layout quality, spacing, arrow routing, and visual review matter. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Vague visualization requests may cause the agent to create or export local diagram files that do not match the user's intent. <br>
Mitigation: Clarify ambiguous diagram scope and review generated diagrams or share links before distribution. <br>
Risk: Diagram layout is position-based, so generated diagrams can contain misleading routing, cramped text, or overlap if not inspected. <br>
Mitigation: Use the skill's required export, visual inspection, fix, and re-export loop before considering the diagram complete. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/spotlight-revenue/skills/drawio-diagrammer-skill) <br>
- [Publisher Profile](https://clawhub.ai/user/spotlight-revenue) <br>
- [Box Style Standards](references/box-style-standards.md) <br>
- [Visual Review Protocol](references/visual-review-protocol.md) <br>
- [Diagram Workflow SOP](references/workflow-sop.md) <br>
- [Flowchart / Process Flow / SOP](references/diagram-types/flowchart.md) <br>
- [ERD / Database Diagram](references/diagram-types/erd.md) <br>
- [UML Class Diagram](references/diagram-types/class.md) <br>
- [Sequence Diagram](references/diagram-types/sequence.md) <br>
- [Architecture / System Diagram](references/diagram-types/layout.md) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Code, Shell commands, Files, Guidance] <br>
**Output Format:** [Markdown delivery text with draw.io XML files, PNG previews, and optional SVG or PDF exports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a local drawio binary; Linux/headless exports may use xvfb-run.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
