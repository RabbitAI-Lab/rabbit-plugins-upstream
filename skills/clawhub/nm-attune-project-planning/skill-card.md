## Description: <br>
Converts a specification into a phased, dependency-ordered implementation plan after specification is complete and before execution begins. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering teams use this skill after a specification is complete to create a structured implementation plan with architecture components, task breakdowns, dependencies, estimates, acceptance criteria, and risks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can continue from planning into execution without a confirmation prompt. <br>
Mitigation: Use --standalone or explicitly instruct the agent to stop after planning when execution is not desired. <br>
Risk: Generated implementation plans may be incomplete, inaccurate, or misaligned with project constraints. <br>
Mitigation: Review the plan, dependencies, estimates, acceptance criteria, and risks before acting on it. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-attune-project-planning) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/athola) <br>
- [Project homepage](https://github.com/athola/claude-night-market/tree/master/plugins/attune) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown implementation plan and task planning guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May save docs/implementation-plan.md and proceed to execution unless the user provides --standalone or explicitly asks to stop after planning.] <br>

## Skill Version(s): <br>
1.9.17 (source: server release metadata; artifact frontmatter lists 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
