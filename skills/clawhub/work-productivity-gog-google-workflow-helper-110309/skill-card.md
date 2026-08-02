## Description: <br>
Helps agent users, skill authors, maintainers, and teams create practical Google Workspace and Gog-style workflow support, including plans, checklists, analyses, code changes, and decision aids. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kyro-ma](https://clawhub.ai/user/kyro-ma) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External agent users, skill authors, maintainers, and teams use this skill to turn Google Workspace and Gog-style productivity needs into concrete workflows, templates, checklists, analysis, code changes, or local-friendly automation plans. It is intended for practical implementation support where assumptions, constraints, validation steps, and remaining risks should be made visible. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad trigger terms may cause the skill to be suggested for general Google, Workspace, CLI, or bug-fix requests where a more specific skill would fit better. <br>
Mitigation: Confirm the user's concrete outcome, constraints, and success criteria before applying the workflow; prefer a narrower skill when the task requires product-specific account access, API setup, or troubleshooting. <br>
Risk: Generated workflows, scripts, or configuration snippets may not match the user's environment or Google Workspace policies. <br>
Mitigation: Keep assumptions visible, ask for missing details only when they materially change the output, and include validation steps before recommending execution or deployment. <br>


## Reference(s): <br>
- [Requirement Plan](references/requirement-plan.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/kyro-ma/skills/work-productivity-gog-google-workflow-helper-110309) <br>
- [Popular ClawHub skill demand: Gog](https://clawhub.ai/skills/gog) <br>
- [Fired by Google for creating the Google workspace CLI](https://news.ycombinator.com/item?id=48664969) <br>
- [LiteLLM issue summary - 2026-06-25](https://github.com/arielb1-sun-security/copilot-studio-test/issues/2209) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with optional code blocks, shell commands, checklists, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include a verification note, assumptions, limits, and follow-up work when useful.] <br>

## Skill Version(s): <br>
0.20260729.110214 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
