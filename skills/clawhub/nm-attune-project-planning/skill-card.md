## Description: <br>
Converts a specification into a phased, dependency-ordered implementation plan for use after specification is complete and before execution begins. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill after a specification is complete to turn requirements into architecture, task breakdowns, dependency ordering, acceptance criteria, effort estimates, and implementation planning guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can move from planning into execution without a separate confirmation prompt after the implementation plan is saved. <br>
Mitigation: Review the generated plan before allowing continuation, use --standalone or explicitly ask the agent to stop after planning, and run it in a workspace where unintended edits can be reverted. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-attune-project-planning) <br>
- [Attune plugin source](https://github.com/athola/claude-night-market/tree/master/plugins/attune) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown planning guidance, including task breakdowns, acceptance criteria, dependency notes, risks, and implementation-plan content.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May save an implementation plan to docs/implementation-plan.md and can continue to the execution phase unless stopped by user request, a --standalone flag, or a failed plan save.] <br>

## Skill Version(s): <br>
1.9.16 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
