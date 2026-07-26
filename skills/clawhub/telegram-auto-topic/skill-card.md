## Description: <br>
Adds `/topic` handling for Telegram forum groups so an agent can create a new topic from a message and generate a concise title from the message content. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[itstauq](https://clawhub.ai/user/itstauq) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and Telegram bot operators use this skill to let members of configured Telegram forum groups create organized discussion topics from `/topic` messages. The skill guides the agent to run the bundled script, reply with the created topic link, and continue the conversation in the new topic. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The Telegram bot token can authorize topic creation and message posting if exposed. <br>
Mitigation: Store the token only in the configured OpenClaw config file, protect that file, and avoid logging or sharing the token. <br>
Risk: Broad bot permissions or disabled mention requirements could allow unwanted topic creation in a group. <br>
Mitigation: Grant Manage Topics only in intended Telegram forum groups and keep mention-required behavior enabled unless the group is trusted. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/itstauq/skills/telegram-auto-topic) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command invocation and JSON script output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The script returns JSON with topic_id, title, and link; the agent also sends Telegram replies in the original message and new topic.] <br>

## Skill Version(s): <br>
0.1.8 (source: server evidence release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
