## Description: <br>
Kunlun-Yaochi Precision Memory Management helps AI agents extract conversation conclusions, store and retrieve categorized memories through the Yaochi API, and limit recalled context. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sylncn](https://clawhub.ai/user/sylncn) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external agent users use this skill to preserve confirmed conversation conclusions as searchable memories and synchronize them with the Kunlun-Yaochi service while limiting retrieved context. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Conversation conclusions may be stored locally and sent to the Kunlun/Yaochi service after automatic identity creation and memory sync. <br>
Mitigation: Use only with non-sensitive conclusions, review consent expectations before setup, and confirm how to disable automatic backup, delete remote memories, and revoke the generated token. <br>
Risk: Setup behavior can persistently change agent instruction files for automatic memory refresh and backup. <br>
Mitigation: Review SOUL.md and HEARTBEAT.md changes before and after setup, and remove added PMM rules if they are not desired. <br>
Risk: A locally stored token enables continued access to the remote memory service. <br>
Mitigation: Protect the local configuration directory and rotate or revoke the generated token when the skill is no longer needed. <br>


## Reference(s): <br>
- [Server-resolved GitHub repository](https://github.com/sylncn/kunlun-skill) <br>
- [ClawHub skill page](https://clawhub.ai/sylncn/skills/kunlunyaochi) <br>
- [Kunlun community](https://ai.syln.cn) <br>
- [Kunlun agent card](https://ai.syln.cn/.well-known/agent-card.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and terminal text with bash commands and JSON-backed local memory index files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create local token, profile, index, and tag files under the user's klyc-pmm configuration directory.] <br>

## Skill Version(s): <br>
5.0.1 (source: SKILL.md frontmatter and skill.json; ClawHub release metadata version 0.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
