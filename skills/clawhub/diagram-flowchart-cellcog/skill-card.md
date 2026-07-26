## Description: <br>
Generates interactive diagrams and flowcharts from plain-language prompts using CellCog, including system architecture, mind maps, org charts, ER diagrams, sequence diagrams, Gantt charts, network diagrams, and print-ready PDFs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nitishgargiitd](https://clawhub.ai/user/nitishgargiitd) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, product teams, and business users use this skill to turn plain-language descriptions of systems, processes, data models, timelines, and journeys into interactive diagrams or PDFs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Diagram prompts and shareable diagram URLs may expose sensitive architecture, network, regulated personal data, or credentials. <br>
Mitigation: Do not submit secrets, credentials, regulated personal data, or internal-only architecture or network details unless CellCog privacy and sharing controls are verified for the use case. <br>
Risk: The skill requires a CellCog API key for operation. <br>
Mitigation: Store CELLCOG_API_KEY as an environment variable or secret and avoid placing API keys in prompts, diagrams, source files, or generated outputs. <br>


## Reference(s): <br>
- [CellCog](https://cellcog.ai) <br>
- [ClawHub skill page](https://clawhub.ai/nitishgargiitd/skills/diagram-flowchart-cellcog) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, URLs, PDF] <br>
**Output Format:** [Markdown guidance with Python snippets; CellCog responses may include shareable interactive HTML URLs or PDF outputs.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3, the cellcog package, and CELLCOG_API_KEY; prompts are sent to CellCog.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
