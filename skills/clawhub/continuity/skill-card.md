## Description: <br>
Continuity Framework helps agents reflect on recent sessions, extract structured memories, generate follow-up questions, and surface pending questions when the user returns. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[riley-coyote](https://clawhub.ai/user/riley-coyote) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent operators use this skill to add local cross-session reflection, memory extraction, identity notes, and follow-up question surfacing to an agent workflow. It is intended for environments where retaining local memory between sessions is acceptable. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill intentionally stores cross-session memory, reflection questions, and identity notes on local disk, which may retain sensitive conversation details. <br>
Mitigation: Review the configured CONTINUITY_MEMORY_DIR, avoid using the skill for conversations that should not be retained, and periodically inspect or delete stored memory files. <br>
Risk: Heartbeat reflection can process prior session content after a conversation becomes idle. <br>
Mitigation: Enable heartbeat reflection only when background post-session processing is acceptable for the user and environment. <br>
Risk: Extracted memories and surfaced questions may include inferred or speculative conclusions. <br>
Mitigation: Treat confidence scores and surfaced questions as reviewable prompts, and confirm important facts with the user before relying on them. <br>


## Reference(s): <br>
- [Continuity Framework Reference](references/framework.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/riley-coyote/skills/continuity) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Plain text and Markdown with shell command examples and local memory files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes local questions, identity notes, and reflection logs under the configured continuity memory directory.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
