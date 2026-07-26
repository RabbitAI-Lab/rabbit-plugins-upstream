## Description: <br>
Memory Compress condenses AI agent memory logs into structured summaries that preserve key events, lessons, and todos while reducing long Markdown logs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to compress daily AI agent logs, long-session memory, project retrospectives, and maintenance summaries into smaller Markdown memory records. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads local memory logs that may contain sensitive information. <br>
Mitigation: Review the logs before processing and clarify whether any LLM or remote provider will handle sensitive content. <br>
Risk: The skill can append summaries to MEMORY.md, update .last-memory-maintenance, and optionally move source logs into an archive. <br>
Mitigation: Ask the agent to preview planned file changes before batch runs and review compressed summaries before appending or archiving. <br>
Risk: The optional callback_url may notify an external endpoint after processing. <br>
Mitigation: Leave callback_url unset unless outbound notification is intended and the destination is trusted. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/thcjp/skills/memory-compress) <br>
- [SkillHub Homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, files, guidance] <br>
**Output Format:** [Markdown summaries with optional shell commands and file updates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May append summaries to MEMORY.md, update .last-memory-maintenance, and optionally archive source logs.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
