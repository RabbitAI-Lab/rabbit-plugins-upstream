## Description: <br>
Generates Mermaid and ASCII diagrams of palace structure, knowledge topology, and synapse connectivity. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents working with memory-palace data use this skill to visualize palace structure, entity relationships, synapse strength, and knowledge topology. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generic trigger words such as memory, visualization, mermaid, diagram, and graph may invoke the skill unintentionally. <br>
Mitigation: Install and enable it only when memory-palace visualization is desired, and review invocation context before using generated diagrams. <br>
Risk: Mermaid rendering can expose generated diagram contents to the configured rendering tool or service. <br>
Mitigation: Use a trusted local or approved private Mermaid renderer for sensitive palace data, or remove sensitive contents before rendering. <br>
Risk: The artifact states the skill contract is unwired and may not be invoked by a palace command. <br>
Mitigation: Use the documented PalaceRenderer or palace_manager.py path directly until command integration is available. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-memory-palace-palace-diagram) <br>
- [Memory palace plugin homepage](https://github.com/athola/claude-night-market/tree/master/plugins/memory-palace) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, guidance] <br>
**Output Format:** [Mermaid diagram text, ASCII diagrams, and Markdown guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May require configured memory-palace data and a trusted Mermaid rendering tool for rendered diagrams.] <br>

## Skill Version(s): <br>
1.9.16 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
