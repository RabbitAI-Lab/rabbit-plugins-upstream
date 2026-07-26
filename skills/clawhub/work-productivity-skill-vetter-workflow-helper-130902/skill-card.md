## Description: <br>
Vet third-party or generated skills for usefulness, safety, overlap, and publish quality. Use when the user needs to decide whether to install, keep, rename, merge, improve, or publish a skill based on evidence and review criteria. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kyro-ma](https://clawhub.ai/user/kyro-ma) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
AI-agent users, skill authors, maintainers, and teams use this skill to review third-party or generated skills before installing, publishing, revising, merging, or rejecting them. It supports practical go/no-go decisions by separating usefulness, safety, duplication risk, trigger quality, and maintenance concerns. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad trigger text may cause the skill to be invoked more often than intended. <br>
Mitigation: Use it for explicit skill vetting tasks and tighten trigger keywords if narrower routing is needed. <br>
Risk: Generated review recommendations could be incomplete or misleading if the available skill evidence is thin. <br>
Mitigation: Require the vetting report to separate security blockers from quality improvements and to tie decisions to explicit criteria. <br>


## Reference(s): <br>
- [Requirement Plan](references/requirement-plan.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/kyro-ma/skills/work-productivity-skill-vetter-workflow-helper-130902) <br>
- [Publisher Profile](https://clawhub.ai/user/kyro-ma) <br>
- [Skill Vetter Demand Signal](https://clawhub.ai/skills/skill-vetter) <br>
- [GitHub Demand Signal](https://clawhub.ai/skills/github) <br>
- [SkillScan Demand Signal](https://clawhub.ai/skills/skillscan) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, Code, Shell commands, Guidance] <br>
**Output Format:** [Markdown reports, checklists, revised skill text, and validation commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include overlap analysis, install or publish recommendations, required fixes, and concise verification notes.] <br>

## Skill Version(s): <br>
0.1.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
