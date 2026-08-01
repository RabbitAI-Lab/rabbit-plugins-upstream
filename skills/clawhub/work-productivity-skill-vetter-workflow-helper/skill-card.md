## Description: <br>
Helps AI-agent users, skill authors, maintainers, and teams plan Skill Vetter-style workflows for bug fixing, safety hardening, reliability improvement, and adjacent skill creation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kyro-ma](https://clawhub.ai/user/kyro-ma) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External AI-agent users, skill authors, maintainers, and teams use this skill to turn Skill Vetter-style needs into practical workflows, checklists, plans, analyses, code changes, or decision support for bug fixing, safety hardening, reliability, and related skill work. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad trigger terms and implicit invocation may cause the skill to activate during unrelated security, GitHub, or bug-fix conversations. <br>
Mitigation: Constrain routing keywords or disable implicit invocation unless the user explicitly requests Skill Vetter-style workflow planning. <br>
Risk: Workflow, checklist, analysis, code-change, or decision-support output may be incomplete for a user's specific repository or policy context. <br>
Mitigation: Review generated guidance against the stated success criteria, local security requirements, and available source evidence before acting on it. <br>


## Reference(s): <br>
- [ClawHub skill release page](https://clawhub.ai/kyro-ma/skills/work-productivity-skill-vetter-workflow-helper) <br>
- [Requirement Plan](references/requirement-plan.md) <br>
- [Skill Vetter demand signal](https://clawhub.ai/skills/skill-vetter) <br>
- [GitHub skill demand signal](https://clawhub.ai/skills/github) <br>
- [SkillScan demand signal](https://clawhub.ai/skills/skillscan) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown or plain text with optional code, shell commands, checklists, and configuration snippets.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include assumptions, validation notes, risks, and follow-up work.] <br>

## Skill Version(s): <br>
0.20260730.234524 (source: evidence.json release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
