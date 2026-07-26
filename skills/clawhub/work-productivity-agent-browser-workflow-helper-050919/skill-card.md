## Description: <br>
Helps users plan, troubleshoot, harden, and extend Agent Browser-style workflows with practical local-friendly artifacts and verification notes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kyro-ma](https://clawhub.ai/user/kyro-ma) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
AI-agent users, skill authors, maintainers, and teams use this skill to clarify browser workflow goals, produce plans, checklists, implementation support, or decision aids, and validate results against the original need. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad implicit invocation wording may activate the skill for unrelated browser, automation, CLI, or bug-fix requests. <br>
Mitigation: Confirm the request is about Agent Browser-style workflow planning or troubleshooting before relying on this skill, and narrow trigger terms before deployment if accidental activation is observed. <br>
Risk: Generated workflow advice or implementation support may not fit the user's local environment or safety requirements. <br>
Mitigation: Review assumptions, validate outputs against the stated success criteria, and inspect any proposed code, checklist, or configuration before use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/kyro-ma/skills/work-productivity-agent-browser-workflow-helper-050919) <br>
- [Requirement plan](references/requirement-plan.md) <br>
- [Agent Browser demand signal](https://clawhub.ai/skills/agent-browser-clawdbot) <br>
- [Browser workflow reliability discussion](https://github.com/manishiitg/coding-agent-loop/issues/128) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Guidance] <br>
**Output Format:** [Markdown with checklists, plans, analysis, and optional code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs should surface assumptions, validation notes, and remaining risks when helpful.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
