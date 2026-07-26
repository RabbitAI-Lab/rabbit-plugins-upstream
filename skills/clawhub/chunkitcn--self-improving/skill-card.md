## Description: <br>
Self-reflection, self-criticism, self-learning, and self-organizing memory for agents that evaluate their own work, catch mistakes, and improve across tasks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chunkitcn](https://clawhub.ai/user/chunkitcn) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to add local, user-visible memory and correction handling so an agent can learn from explicit feedback, self-reflection, and recurring workflow patterns. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Persistent local memory can influence future agent behavior and preserve unwanted or sensitive context. <br>
Mitigation: Review the memory files before and after installation, avoid storing sensitive information, and use the documented forget/export flows when memory should be removed. <br>
Risk: Workspace steering edits can change how the agent behaves in later tasks. <br>
Mitigation: Review proposed changes to AGENTS.md, SOUL.md, and HEARTBEAT.md before applying them. <br>
Risk: The optional Proactivity companion is a separate skill with its own behavior and possible network access. <br>
Mitigation: Install the companion only after explicit user approval and review it separately before use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chunkitcn/skills/self-improving) <br>
- [Skill homepage](https://clawic.com/skills/self-improving) <br>
- [Setup guide](setup.md) <br>
- [Security boundaries](boundaries.md) <br>
- [Learning mechanics](learning.md) <br>
- [Memory operations](operations.md) <br>
- [Heartbeat rules](heartbeat-rules.md) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces local memory files under ~/self-improving/ and optional workspace steering edits when installed.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata; artifact frontmatter version 1.2.16) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
