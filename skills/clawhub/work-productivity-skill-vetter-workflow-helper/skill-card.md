## Description: <br>
Helps AI-agent users, skill authors, maintainers, and teams create practical vetting workflows, checklists, analysis, code changes, and decision support for fixing bugs, improving setup safety, and hardening reliability. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kyro-ma](https://clawhub.ai/user/kyro-ma) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers, AI-agent users, skill authors, maintainers, and teams use this skill to turn skill-vetting and reliability requests into concrete plans, checklists, analyses, code changes, or decision aids. It is especially aimed at practical workflows for bug fixes, setup hardening, safety review, and adjacent skill creation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill has broad trigger wording and may activate for generic security, GitHub, or bug-fix requests. <br>
Mitigation: Review whether the request is actually about skill vetting, workflow planning, hardening, reliability, or adjacent skill creation before applying the skill. <br>
Risk: Workflow outputs can contain proposed code, shell commands, configuration changes, or safety recommendations that may be incorrect for the user's environment. <br>
Mitigation: Validate proposed changes against the stated success criteria, scan or review artifacts before deployment, and keep assumptions and remaining risks visible. <br>


## Reference(s): <br>
- [Requirement Plan](references/requirement-plan.md) <br>
- [Work Productivity Skill Vetter Workflow Helper on ClawHub](https://clawhub.ai/kyro-ma/skills/work-productivity-skill-vetter-workflow-helper) <br>
- [Popular ClawHub Skill Demand: Skill Vetter](https://clawhub.ai/skills/skill-vetter) <br>
- [Popular ClawHub Skill Demand: Github](https://clawhub.ai/skills/github) <br>
- [Popular ClawHub Skill Demand: SkillScan](https://clawhub.ai/skills/skillscan) <br>
- [Ask HN: How would you learn AI-assisted development from the ground up?](https://news.ycombinator.com/item?id=49098829) <br>
- [Ask HN: Do we need a stronger process for vetting code?](https://news.ycombinator.com/item?id=49094175) <br>
- [GitHub Issue: Bump the GitHub Actions off the deprecated Node 20 runtime](https://github.com/Lukietoo/Luke-site/issues/7) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with optional inline code blocks, shell commands, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include reusable checklists, implementation notes, verification notes, assumptions, limits, and follow-up risks.] <br>

## Skill Version(s): <br>
0.20260730.10356 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
