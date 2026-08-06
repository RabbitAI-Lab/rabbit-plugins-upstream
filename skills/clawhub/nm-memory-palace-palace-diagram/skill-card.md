## Description: <br>
Generates Mermaid and ASCII diagrams of palace structure, knowledge topology, and synapse connectivity. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and knowledge-work agents use this skill to inspect memory-palace structure, entity relationships, synapse strength, and topology through Mermaid diagrams or inline ASCII overviews. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad triggers such as memory, diagram, and graph may activate the skill more often than intended. <br>
Mitigation: Review activation context before using the generated diagram guidance, and route non-memory-palace diagramming tasks to a more specific skill. <br>
Risk: The skill documentation says command wiring is pending, so users may expect a direct slash-command workflow that is not available in the artifact. <br>
Mitigation: Use the documented PalaceRenderer or palace_manager.py workflow until command integration is confirmed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-memory-palace-palace-diagram) <br>
- [Memory Palace plugin homepage](https://github.com/athola/claude-night-market/tree/master/plugins/memory-palace) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code] <br>
**Output Format:** [Mermaid diagram code or ASCII text, usually presented in Markdown] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use Mermaid Chart MCP rendering for Mermaid output; ASCII output is displayed inline.] <br>

## Skill Version(s): <br>
1.9.17 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
