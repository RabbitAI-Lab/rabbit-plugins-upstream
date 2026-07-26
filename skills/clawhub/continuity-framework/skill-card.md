## Description: <br>
Asynchronous reflection and memory integration for genuine AI development. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[riley-coyote](https://clawhub.ai/user/riley-coyote) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent operators use this skill to reflect on recent sessions, extract structured memories, generate follow-up questions, and surface continuity context when a user returns. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Session transcripts and generated memories may contain sensitive personal or project information retained in local continuity files. <br>
Mitigation: Avoid processing transcripts with secrets or highly sensitive content, and periodically inspect or delete the generated memory, question, identity, and reflection files. <br>
Risk: Reflection outputs may preserve incorrect inferences or speculative relationship context. <br>
Mitigation: Review generated memories and questions before relying on them for future user interactions. <br>


## Reference(s): <br>
- [The Continuity Framework](references/framework.md) <br>
- [ClawHub skill page](https://clawhub.ai/riley-coyote/skills/continuity-framework) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [CLI text output, Markdown memory files, and JSON reflection logs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Creates local continuity files under CONTINUITY_MEMORY_DIR, defaulting to ~/clawd/memory.] <br>

## Skill Version(s): <br>
1.0.0 (source: server evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
