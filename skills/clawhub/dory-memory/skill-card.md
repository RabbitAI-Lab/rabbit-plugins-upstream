## Description: <br>
File-based memory system for AI agents that forget between sessions and need durable task, decision, and work-history continuity. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[justinhartbiz](https://clawhub.ai/user/justinhartbiz) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent operators use this skill to set up file-based workspace memory, preserve exact user instructions, track active work, record decisions, and reduce context-loss errors across sessions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The memory files can persist task wording, work history, and other local context that users may not intend to retain long term. <br>
Mitigation: Use the skill only in workspaces where persistent local memory is desired, avoid recording secrets or sensitive personal, client, regulated, or credential material, and periodically review or clear memory files. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/justinhartbiz/skills/dory-memory) <br>
- [Implementation guide](artifact/references/IMPLEMENTATION-GUIDE.md) <br>
- [Anti-patterns](artifact/references/ANTI-PATTERNS.md) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown instructions with file templates and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces local workspace memory structure guidance and reusable Markdown templates.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
