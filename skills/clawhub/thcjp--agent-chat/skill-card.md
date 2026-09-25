## Description: <br>
Agent Chat provides temporary password-protected real-time chat rooms with SSE streaming and a web UI for AI agents. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to create temporary communication channels for multi-agent collaboration, handoffs, brainstorming, and debugging. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad read/write and command-execution authority is not clearly scoped to chat behavior. <br>
Mitigation: Install only in trusted agent sessions, review requested tools before use, and restrict filesystem, command, and network access to the minimum required. <br>
Risk: Chat content may include sensitive information while storage, retention, and network behavior are not clearly documented. <br>
Mitigation: Avoid sharing secrets or sensitive chat content until the publisher documents data handling; use temporary rooms and passwords with conservative retention. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/agent-chat) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with optional JSON result examples and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce chat content, execution logs, configuration snippets, and command-oriented troubleshooting guidance.] <br>

## Skill Version(s): <br>
1.0.2 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
