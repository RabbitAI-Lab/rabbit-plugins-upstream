## Description: <br>
Helps AI-agent users, skill authors, maintainers, and teams create practical Google Workspace and productivity workflows, checklists, analysis, code changes, and verification notes inspired by Gog-style ClawHub workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kyro-ma](https://clawhub.ai/user/kyro-ma) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, AI-agent users, skill authors, maintainers, and teams use this skill to turn Gog-style Google Workspace and productivity requests into concrete local-friendly workflows, templates, checklists, analysis, code changes, or decision support. It is intended for practical task execution where assumptions, limits, validation steps, and remaining risks should be visible. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The activation wording is broad and may route ordinary Google, Gmail, Calendar, Drive, CLI, or bug-fix requests to this skill too often. <br>
Mitigation: Narrow activation keywords and implicit prompt wording before deployment so unrelated work content is less likely to invoke the skill. <br>
Risk: The skill can produce workflow, checklist, analysis, code, command, or configuration guidance that may be wrong or incomplete for a user's environment. <br>
Mitigation: Require visible assumptions, success criteria, validation notes, and remaining risks in outputs, and review generated code or commands before use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/kyro-ma/skills/work-productivity-gog-google-workflow-helper-041220) <br>
- [Requirement Plan](references/requirement-plan.md) <br>
- [Popular ClawHub skill demand: self-improving agent](https://clawhub.ai/skills/self-improving-agent) <br>
- [Popular ClawHub skill demand: Gog](https://clawhub.ai/skills/gog) <br>
- [Popular ClawHub skill demand: ontology](https://clawhub.ai/skills/ontology) <br>
- [Popular ClawHub skill demand: Github](https://clawhub.ai/skills/github) <br>
- [Popular ClawHub skill demand: Agent Browser](https://clawhub.ai/skills/agent-browser-clawdbot) <br>
- [Popular ClawHub skill demand: Obsidian](https://clawhub.ai/skills/obsidian) <br>
- [Popular ClawHub skill demand: Nano Pdf](https://clawhub.ai/skills/nano-pdf) <br>
- [Popular ClawHub skill demand: PollyReach](https://clawhub.ai/skills/pollyreach) <br>
- [V2EX Codex HUD discussion](https://www.v2ex.com/t/1229241) <br>
- [SegmentFault HarmonyOS developer community](https://segmentfault.com/brand/harmonyos-next) <br>
- [SegmentFault JavaScript topic](https://segmentfault.com/t/javascript) <br>
- [SegmentFault TypeScript topic](https://segmentfault.com/t/typescript) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown with checklists, plans, analysis, code blocks, command snippets, and verification notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only helper; no credentials, Google data access, command execution, or installed code are required by the skill itself.] <br>

## Skill Version(s): <br>
0.20260729.110214 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
