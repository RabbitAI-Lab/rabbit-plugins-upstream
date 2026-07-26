## Description: <br>
Executing Plans helps agents execute written plans step by step with verification, visible deviation handling, and an execution log that records results and feedback. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mohitagw15856](https://clawhub.ai/user/mohitagw15856) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, agent operators, and reviewers use this skill when carrying out an existing plan, resuming multi-session work, or controlling execution drift. It keeps each step tied to verification, visible handling of deviations, stop conditions, and plan feedback. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Execution plans may contain incorrect, stale, or unsafe concrete actions. <br>
Mitigation: Review the plan and its verification commands before running them, and stop or replan when assumptions fail. <br>
Risk: The skill can make flawed plan guidance look authoritative if verification is skipped. <br>
Mitigation: Require each step to record the check that was actually run, its outcome, and any deviation classification. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/mohitagw15856/skills/executing-plans) <br>
- [Skill homepage](https://mohitagw15856.github.io/pm-claude-skills/skill/executing-plans.html) <br>
- [Publisher profile](https://clawhub.ai/user/mohitagw15856) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown execution log and completion report] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes per-step results, verification outcomes, classified deviations, done-test evidence, plan feedback, and follow-ups.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
