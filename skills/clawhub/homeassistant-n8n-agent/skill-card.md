## Description: <br>
Bridge OpenClaw with your n8n instance for Home Assistant automation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[enchantedmotorcycle](https://clawhub.ai/user/enchantedmotorcycle) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and smart-home operators use this skill to route OpenClaw requests to a trusted n8n workflow for Home Assistant state, action, historical, and calendar requests. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad smart-home and calendar workflow authority through raw curl commands. <br>
Mitigation: Use only with an n8n workflow you control and trust, require explicit confirmation for action requests, and restrict allowed devices and actions in n8n. <br>
Risk: Unsafe construction of POST bodies can expose raw user text to shell or JSON injection mistakes. <br>
Mitigation: Construct JSON request bodies safely instead of pasting user text into raw shell JSON. <br>
Risk: Home activity and calendar prompts may be retained in n8n execution logs. <br>
Mitigation: Review n8n logging, retention, and access controls before using the skill with sensitive household or calendar data. <br>


## Reference(s): <br>
- [n8n](https://n8n.io/) <br>
- [ClawHub Skill Page](https://clawhub.ai/enchantedmotorcycle/skills/homeassistant-n8n-agent) <br>
- [Publisher Profile](https://clawhub.ai/user/enchantedmotorcycle) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown guidance with inline curl commands and JSON POST bodies] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires curl and a user-controlled n8n webhook workflow.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
