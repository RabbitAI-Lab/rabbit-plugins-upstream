## Description: <br>
Side Peace provides a minimal zero-dependency secret handoff where a human submits a secret through a browser form and the agent receives it via a temporary file without printing the secret to stdout or logs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bitbrujo](https://clawhub.ai/user/bitbrujo) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent users use Side Peace to pass API keys, tokens, or other secrets to a local agent session without placing secret values in chat logs or command output. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The secret handoff uses an unauthenticated plain-HTTP server that is exposed to the local network by default. <br>
Mitigation: Use only the localhost URL on trusted machines and networks, and avoid sharing high-value credentials through the network URL unless the skill is changed to use localhost-only or authenticated transport. <br>
Risk: The submitted secret is written to a generated local file. <br>
Mitigation: Use short-lived scoped tokens when possible and delete the generated secret file immediately after use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/bitbrujo/skills/side-peace) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Files, Guidance] <br>
**Output Format:** [Markdown guidance with bash commands and terminal output describing a temporary secret file path] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Secrets are written to a local temporary file and should be deleted immediately after use.] <br>

## Skill Version(s): <br>
1.1.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
