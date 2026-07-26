## Description: <br>
Crisp enables agents to inspect Crisp websites and conversations through an OOMOL-connected account and send operator text replies when confirmed by the user. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Support teams, operators, and their agents use this skill to retrieve Crisp website and conversation data, list messages, and send confirmed operator replies through OOMOL-mediated Crisp access. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Read actions can expose Crisp customer conversations and messages. <br>
Mitigation: Install only when OOMOL-mediated Crisp access is intended and limit use to authorized connected accounts. <br>
Risk: The send_text_message action can post operator replies to live conversations. <br>
Mitigation: Confirm the target conversation, message payload, and expected effect with the user before running write actions. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-crisp) <br>
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [Crisp Homepage](https://crisp.chat/) <br>
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON connector results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live oo connector schemas before constructing action payloads.] <br>

## Skill Version(s): <br>
1.0.1 (source: server evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
