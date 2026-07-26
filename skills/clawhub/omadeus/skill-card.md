## Description: <br>
Interact with the Maestro task management system to create tasks, list recent tasks, and send messages to Maestro rooms. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mohammadsheikhian](https://clawhub.ai/user/mohammadsheikhian) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Users with a configured Maestro workspace use this skill to create and review task records and post concise updates to Maestro rooms from an agent session. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can use a configured Maestro API key to create tasks, list tasks, and send messages to Maestro rooms. <br>
Mitigation: Install it only for agents that should access Maestro, and review requests that create tasks or send room messages before execution. <br>
Risk: A room ID already present in context could make a send or post request target a specific Maestro room. <br>
Mitigation: Confirm the target room and message content for send or post requests, especially in shared or production workspaces. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/mohammadsheikhian/skills/omadeus) <br>
- [Publisher profile](https://clawhub.ai/user/mohammadsheikhian) <br>


## Skill Output: <br>
**Output Type(s):** [Text, API calls, Guidance] <br>
**Output Format:** [Concise text or Markdown responses with structured API request details when needed.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses configured Maestro credentials and environment mapping; responses should not expose API keys.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
