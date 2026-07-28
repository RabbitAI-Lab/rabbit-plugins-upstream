## Description: <br>
Helps agent users, skill authors, maintainers, and teams create practical Gog-style Google Workspace productivity workflows, checklists, analyses, code changes, shell commands, and implementation support. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kyro-ma](https://clawhub.ai/user/kyro-ma) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
AI-agent users, skill authors, maintainers, and teams use this skill to turn Gog-style Google Workspace productivity requests into concrete plans, templates, checklists, analyses, code changes, shell commands, or decision support. It is intended for practical bug fixing, setup hardening, reliability improvements, and adjacent workflow creation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad triggers and implicit invocation can activate the skill on unrelated Google, CLI, or bug-fix requests. <br>
Mitigation: Review the activation context before use and narrow trigger language if the skill is installed in environments with many unrelated productivity or engineering tasks. <br>
Risk: Workflow-helper outputs may still need local validation before they are applied to real workspaces or repositories. <br>
Mitigation: Check generated plans, commands, code changes, and configuration snippets against the user's stated success criteria before deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/kyro-ma/skills/work-productivity-gog-google-workflow-helper) <br>
- [Requirement plan](references/requirement-plan.md) <br>
- [Popular ClawHub skill demand: Gog](https://clawhub.ai/skills/gog) <br>
- [Hacker News: programming setup discussion](https://news.ycombinator.com/item?id=49069300) <br>
- [Hacker News: tech stack discussion](https://news.ycombinator.com/item?id=49061251) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown or plain text guidance with optional code blocks, shell commands, checklists, templates, and configuration snippets.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs should include visible assumptions, validation notes, and remaining risks when useful.] <br>

## Skill Version(s): <br>
0.20260728.40429 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
