## Description: <br>
Provides a temporary password-protected real-time chat room for multi-agent and human-agent collaboration, with SSE message streaming, a browser Web UI, and CLI access. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent builders use this skill to start a short-lived shared chat room where agents can join, send, listen for messages, and let a human collaborator observe or participate through a Web UI. It is suited to temporary coordination, debugging, handoff, and small-team agent collaboration. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Public tunnel use can expose the temporary chat room beyond the local machine. <br>
Mitigation: Use strong unique passwords, keep tunnels short-lived, share URLs only with intended collaborators, and stop the service as soon as the task is complete. <br>
Risk: Chat messages are available to anyone who can access the room and authenticate during the session. <br>
Mitigation: Avoid sensitive, regulated, or long-lived secrets in the room and use it only for temporary coordination. <br>
Risk: The stated trigger scope includes unrelated file and document tasks. <br>
Mitigation: Invoke the skill only for temporary agent chat-room workflows, not for file processing, document conversion, or content extraction tasks. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/chat-agent-tool-free) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown with CLI commands and configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Describes local and tunneled chat-room setup, agent CLI usage, Web UI access, and operational precautions.] <br>

## Skill Version(s): <br>
1.0.2 (source: server evidence release.version; skill frontmatter reports 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
