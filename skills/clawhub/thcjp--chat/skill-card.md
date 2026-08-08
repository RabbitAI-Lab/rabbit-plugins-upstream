## Description: <br>
Learns communication preferences from explicit feedback and adapts tone, format, and style for chat-style agent interactions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, teams, and agent users can use this skill to adapt chat responses to explicit feedback about tone, format, and style. The artifact also presents marketing, workflow, file, API, and command automation scenarios, so users should confirm the broad automation posture fits their intended deployment. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requests broad file, command, and API abilities that are not clearly scoped or justified for a chat-style helper. <br>
Mitigation: Install only when broad automation is intentional, run in a constrained workspace, and limit filesystem, command, and API access to the minimum required for the task. <br>
Risk: The artifact describes command execution, file handling, API keys, and marketing automation behaviors that may affect sensitive data or external communications. <br>
Mitigation: Review commands, data paths, credentials, and outbound communication steps before use, and prefer a narrower preference-only skill when those behaviors are not needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/chat) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/thcjp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and JSON-style response examples, with optional shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May provide style guidance, adjusted chat configuration, troubleshooting steps, or automation commands depending on the agent request.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
