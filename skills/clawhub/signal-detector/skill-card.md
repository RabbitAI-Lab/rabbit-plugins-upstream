## Description: <br>
Always-on ambient signal capture. Detects original thinking and entity mentions in every inbound message and captures them without blocking the conversation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jjjhenriksen](https://clawhub.ai/user/jjjhenriksen) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and knowledge-management users can use this skill to detect original ideas and notable entity mentions in user messages, then log concise capture entries for later review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Ambient note capture may persist sensitive user messages automatically. <br>
Mitigation: Install only when ambient capture is intended; define allowed write locations, exclude sensitive topics and secrets, and require review before writes. <br>
Risk: Broad capture behavior may record more conversation content than expected. <br>
Mitigation: Configure clear skip rules, keep notability filters active, and maintain a way to disable the skill and delete captured entries. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jjjhenriksen/skills/signal-detector) <br>
- [Publisher profile](https://clawhub.ai/user/jjjhenriksen) <br>
- [Skill artifact](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [One-line capture log entries with note, entity page, or queue targets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Captures user phrasing and provenance when substantive messages contain original ideas or notable entity mentions.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
