## Description: <br>
Autonomous memory and self-learning system that helps AI agents log experience, manage persistent memories and preferences, extract recurring lessons, adapt behavior, and verify whether changes improved future work. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[brucetangc](https://clawhub.ai/user/brucetangc) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and agent operators use this skill to add persistent self-improvement workflows to an AI agent, including session summaries, structured learning logs, user preference memory, behavior-file updates, verification checks, and backup or sync commands. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can retain conversation-derived summaries, preferences, and learning entries in persistent workspace files. <br>
Mitigation: Enable it only when persistent agent memory is intended, avoid logging secrets or sensitive content, and review memory files periodically. <br>
Risk: The learning cycle can update behavior and memory files such as MEMORY.md, TOOLS.md, USER.md, SOUL.md, and AGENTS.md. <br>
Mitigation: Review or disable automatic cycle and promotion behavior, keep backups, and require user approval for behavior-changing proposals. <br>
Risk: Backup import can restore or overwrite memory data from ZIP files. <br>
Mitigation: Import only trusted backup ZIPs and use overwrite mode only after verifying the target workspace and backup contents. <br>
Risk: The documented Windows recovery path includes a recursive directory delete command. <br>
Mitigation: Treat that command as a manual recovery step and verify the exact skill directory path before running it. <br>


## Reference(s): <br>
- [ClawHub release page](https://clawhub.ai/brucetangc/skills/self-improvement-llm) <br>
- [CLI reference](references/cli_ref.md) <br>
- [Reflection frameworks](references/reflection_frameworks.md) <br>
- [Self-improving agent inspiration](https://clawhub.ai/pskoett/self-improving-agent) <br>
- [Hermes Agent](https://github.com/NousResearch/hermes-agent) <br>
- [Reflexion paper](https://arxiv.org/abs/2303.11366) <br>
- [Reflexion draft code](https://github.com/noahshinn/reflexion-draft) <br>
- [AutoGPT](https://github.com/Significant-Gravitas/AutoGPT) <br>
- [LangGraph](https://github.com/langchain-ai/langgraph) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands plus JSON, Markdown, and ZIP file artifacts created by the skill scripts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can create or update persistent memory files, learning-trail JSON, hook context, generated skill drafts, behavior files, and backup archives when enabled and run.] <br>

## Skill Version(s): <br>
2.3.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
