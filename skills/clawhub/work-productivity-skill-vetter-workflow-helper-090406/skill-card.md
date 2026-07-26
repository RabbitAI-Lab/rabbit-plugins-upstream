## Description: <br>
Helps agent users, skill authors, maintainers, and teams create practical Skill Vetter-style workflows for bug fixing, setup and safety hardening, reliability improvement, and adjacent skill development. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kyro-ma](https://clawhub.ai/user/kyro-ma) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Agent users, skill authors, maintainers, and teams use this skill to turn Skill Vetter-style demand into actionable plans, checklists, analyses, code changes, and verification notes. It is intended for practical local workflows that clarify constraints, produce a concrete deliverable, and surface remaining risks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad activation triggers may invoke the skill in contexts where the user did not intend a vetting or workflow-helper response. <br>
Mitigation: Prefer explicit invocation by skill name and confirm the requested outcome before producing plans, code changes, or setup guidance. <br>
Risk: Generated plans or implementation support could introduce incorrect or unsuitable changes if applied without review. <br>
Mitigation: Review generated plans, commands, configuration, and code before applying them, and validate the result against the stated success criteria. <br>


## Reference(s): <br>
- [Requirement Plan](references/requirement-plan.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/kyro-ma/skills/work-productivity-skill-vetter-workflow-helper-090406) <br>
- [Popular ClawHub Skill Demand: Skill Vetter](https://clawhub.ai/skills/skill-vetter) <br>
- [Popular ClawHub Skill Demand: Github](https://clawhub.ai/skills/github) <br>
- [Popular ClawHub Skill Demand: SkillScan](https://clawhub.ai/skills/skillscan) <br>
- [HN Demand Signal: Inference Server for DGX Spark](https://news.ycombinator.com/item?id=49014048) <br>
- [HN Demand Signal: AI-Orchestrated Publishing Workflow](https://news.ycombinator.com/item?id=49009663) <br>
- [HN Demand Signal: GitHub GraphQL API Missing Data](https://news.ycombinator.com/item?id=49003232) <br>
- [GitHub Issue Demand Signal: External Context Provider Profile](https://github.com/QwenLM/qwen-code/issues/7585) <br>
- [GitHub Issue Demand Signal: Custom Save-as-PDF Filename](https://github.com/ngx-print/ngx-print/issues/331) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown or structured text with checklists, plans, code snippets, commands, configuration notes, and verification notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include reusable workflows, assumptions, limits, remaining risks, and follow-up work] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
