## Description: <br>
Beeper Desktop CLI for chats, messages, contacts, connect info, websocket events, search, and reminders. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[johntheyoung](https://clawhub.ai/user/johntheyoung) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent operators use Roadrunner to work with Beeper Desktop through the local rr CLI for chat lookup, message search, contacts, reminders, app focus, and explicitly requested message actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The rr CLI can read Beeper chats, messages, contacts, and account state. <br>
Mitigation: Use readonly or agent mode for lookups, keep searches narrow, and summarize only the information the user needs. <br>
Risk: The rr CLI can send, edit, react to messages, create chats, upload assets, and modify reminders when mutation commands are used. <br>
Mitigation: Only perform mutations after an explicit user request with a clear recipient and content; use dry-run validation when appropriate. <br>
Risk: Beeper authentication tokens and raw command output may expose private account or conversation data. <br>
Mitigation: Ask users to configure authentication locally, never request or store raw tokens, and do not paste raw rr JSON dumps into outgoing messages. <br>


## Reference(s): <br>
- [Roadrunner ClawHub Skill Page](https://clawhub.ai/johntheyoung/skills/roadrunner) <br>
- [Roadrunner Project Homepage](https://github.com/johntheyoung/roadrunner) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON or JSONL command-output expectations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guidance emphasizes readonly defaults, explicit user approval for mutations, and private handling of raw Beeper output.] <br>

## Skill Version(s): <br>
0.17.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
