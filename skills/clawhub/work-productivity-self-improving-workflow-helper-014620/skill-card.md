## Description: <br>
Helps AI-agent users, skill authors, maintainers, and teams create practical self-improving workflows for bug fixing, setup hardening, reliability improvement, and adjacent skill creation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kyro-ma](https://clawhub.ai/user/kyro-ma) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, maintainers, skill authors, and agent users use this skill to turn requests about self-improving agent workflows into concrete plans, checklists, templates, code changes, or decision support. It is intended for productivity and reliability work such as bug fixing, setup hardening, validation, and workflow improvement. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may activate too broadly for ordinary requests involving logs, improvements, or bug fixes. <br>
Mitigation: Use explicit invocation for this release when possible and narrow trigger terms in future maintenance to self-improving agent workflow or agent reliability contexts. <br>
Risk: Workflow or code recommendations may be applied without enough review for the user's environment. <br>
Mitigation: Review proposed changes, scan any generated skill files before deployment, and validate outputs against the stated success criteria. <br>


## Reference(s): <br>
- [Requirement Plan](references/requirement-plan.md) <br>
- [ClawHub Self-Improving Agent Demand Signal](https://clawhub.ai/skills/self-improving-agent) <br>
- [ClawHub Self-Improving + Proactive Agent Demand Signal](https://clawhub.ai/skills/self-improving) <br>
- [Hacker News Demand Signal](https://news.ycombinator.com/item?id=48684171) <br>
- [OpenClaw SegmentFault Reference](https://segmentfault.com/a/1190000047666647) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown, optionally with code blocks, commands, checklists, or configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include assumptions, validation notes, risks, and follow-up work.] <br>

## Skill Version(s): <br>
0.20260729.110214 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
