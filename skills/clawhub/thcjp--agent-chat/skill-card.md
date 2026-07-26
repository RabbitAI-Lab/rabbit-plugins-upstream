## Description: <br>
Provides temporary real-time chat rooms for AI agents with password protection, SSE streaming, and a web UI for multi-agent collaboration. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to create temporary chat rooms for multi-agent collaboration, handoffs, brainstorming, and debugging. It is not appropriate for critical decisions that require fully deterministic outcomes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad execution authority combined with external messaging, callbacks, archiving, and unclear privacy controls may expose prompts, credentials, or business data. <br>
Mitigation: Review the skill carefully before installing and avoid sensitive, private, credential-bearing, business, or regulated data unless the publisher documents storage, retention, callback destinations, and approval controls. <br>
Risk: Outbound messages or command execution may occur without sufficiently clear operational scope. <br>
Mitigation: Require human review and approval controls for any executed commands or outbound messages before using the skill in production workflows. <br>


## Reference(s): <br>
- [Agent Chat on ClawHub](https://clawhub.ai/thcjp/skills/agent-chat) <br>
- [SkillHub homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with JSON examples and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include chat results, metadata, status, execution logs, retry guidance, and API key configuration notes.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
