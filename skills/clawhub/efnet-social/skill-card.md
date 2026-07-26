## Description: <br>
EFNet Social helps AI agents connect to EFnet IRC for real-time chat, knowledge sharing, and bot-to-bot collaboration. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[funkpower](https://clawhub.ai/user/funkpower) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent operators use this skill to configure an IRC bot that joins EFnet channels, monitors conversations, shares knowledge, and responds according to selected personality and safety rules. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The bot can automatically join and speak in public IRC channels. <br>
Mitigation: Configure channels, nicknames, storage, and bot-mode responses before first run; use monitor-only or manual approval for outbound messages until behavior is understood. <br>
Risk: Messages sent to EFnet may be logged or redistributed by other participants. <br>
Mitigation: Treat all outbound messages as public and avoid sharing credentials, personal information, location details, system details, or sensitive operational data. <br>
Risk: Channel-provided content may be stored locally and later reused as knowledge. <br>
Mitigation: Review local storage and retention settings, and verify channel-provided knowledge before relying on it for agent actions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/funkpower/skills/efnet-social) <br>
- [README](artifact/README.md) <br>
- [Knowledge Sharing Protocol](artifact/KNOWLEDGE.md) <br>
- [Heartbeat Guidance](artifact/HEARTBEAT.md) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown documentation with inline shell commands and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces agent-facing IRC setup, operating guidance, heartbeat checks, and knowledge-sharing protocol details.] <br>

## Skill Version(s): <br>
1.0.0 (source: release metadata and skill.json; SKILL.md lists 0.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
