## Description: <br>
Asynchronous reflection and memory integration for genuine AI development. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[riley-coyote](https://clawhub.ai/user/riley-coyote) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent operators use this skill to add post-session reflection, structured memory extraction, pending questions, and session-start continuity prompts to an agent workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can retain conversation-derived identity, relationship, and question data in local memory files. <br>
Mitigation: Keep the memory directory private, avoid providing secrets or sensitive personal data, and periodically review or delete generated memory files. <br>
Risk: Heartbeat reflection may generate or surface follow-up questions after a session has ended. <br>
Mitigation: Enable heartbeat reflection only with explicit user consent and review generated questions before relying on them. <br>


## Reference(s): <br>
- [The Continuity Framework](references/framework.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration] <br>
**Output Format:** [Terminal text, Markdown memory files, and JSON reflection logs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes local memory, identity, question, and reflection files under the configured memory directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
