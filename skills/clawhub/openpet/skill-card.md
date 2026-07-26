## Description: <br>
OpenPet adds a Tamagotchi-style virtual pet game to OpenClaw chat channels, where each user can feed, play with, name, rest, and track an evolving pet across platforms such as Discord, WhatsApp, and Telegram. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mdealiaga](https://clawhub.ai/user/mdealiaga) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and chat-platform operators use OpenPet to add a multi-user virtual pet game to OpenClaw channels, where users care for pets through chat commands and receive status, evolution, and alert messages. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill keeps local per-user pet records tied to platform identifiers and user names. <br>
Mitigation: Operators should document what identifiers are stored, where pet files live, and how users can delete or reset their data. <br>
Risk: The scheduled decay and reminder behavior may send proactive alerts to users. <br>
Mitigation: Operators should disclose the recurring job and provide controls to disable or rate-limit alerts. <br>


## Reference(s): <br>
- [OpenPet Skill Page](https://clawhub.ai/mdealiaga/skills/openpet) <br>
- [OpenClaw](https://github.com/openclaw/openclaw) <br>
- [OpenPet README](artifact/README.md) <br>
- [Configuration Reference](artifact/references/config.json) <br>
- [Sprite Reference](artifact/references/sprites.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Chat text and Markdown-style status displays with local JSON pet records and configuration references.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Pet state is tracked per platform and user identifier; stats decay on a scheduled interval and alerts may be sent to the user's origin platform.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
