## Description: <br>
Helps AI-agent users and skill authors turn Gog-style Google Workspace productivity requests into concrete plans, checklists, analyses, code changes, or workflow artifacts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kyro-ma](https://clawhub.ai/user/kyro-ma) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
AI-agent users, skill authors, maintainers, and teams use this skill to structure Gog-style Google Workspace productivity work into practical plans, checklists, workflow artifacts, analysis, or implementation support. It is intended for requests involving workspace tools, CLI workflows, bug fixes, reliability hardening, and adjacent skill creation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad trigger wording may activate the skill for general Google, workspace, CLI, Gmail, Calendar, Drive, or bug-fix prompts. <br>
Mitigation: Disable implicit invocation where supported or invoke the skill explicitly only for Gog-style or Google Workspace productivity planning tasks. <br>
Risk: The skill may produce plans, code changes, shell commands, or configuration guidance that affect user workflows. <br>
Mitigation: Review generated artifacts and commands against the stated success criteria before applying them. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/kyro-ma/skills/work-productivity-gog-google-workflow-helper-130446) <br>
- [Requirement Plan](references/requirement-plan.md) <br>
- [Popular ClawHub skill demand: self-improving agent](https://clawhub.ai/skills/self-improving-agent) <br>
- [Popular ClawHub skill demand: Gog](https://clawhub.ai/skills/gog) <br>
- [Popular ClawHub skill demand: Github](https://clawhub.ai/skills/github) <br>
- [Popular ClawHub skill demand: ontology](https://clawhub.ai/skills/ontology) <br>
- [Popular ClawHub skill demand: Obsidian](https://clawhub.ai/skills/obsidian) <br>
- [Popular ClawHub skill demand: Nano Pdf](https://clawhub.ai/skills/nano-pdf) <br>
- [Popular ClawHub skill demand: Agent Browser](https://clawhub.ai/skills/agent-browser-clawdbot) <br>
- [OpenClaw to FastClaw multi-agent architecture discussion](https://www.v2ex.com/t/1222063) <br>
- [SMTP Relay with Web Dashboard discussion](https://news.ycombinator.com/item?id=48601429) <br>
- [Google Workspace browser access discussion](https://news.ycombinator.com/item?id=48625428) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown or plain text, with code blocks or configuration snippets when the requested task requires them] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include concise plans, templates, reusable checklists, implementation notes, and verification notes.] <br>

## Skill Version(s): <br>
0.1.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
