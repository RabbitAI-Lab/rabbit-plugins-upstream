## Description: <br>
User behavior correction skill triggered by fix-style feedback; it analyzes the mistake, improves the relevant prompt, rule, memory, skill, or hook to prevent recurrence, and then completes the current issue. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[drumrobot](https://clawhub.ai/user/drumrobot) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to respond to user feedback about agent mistakes, diagnose the behavioral cause, update the appropriate durable guidance or enforcement medium, and resume the original work. It is intended for environments where persistent agent behavior changes are acceptable after review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create durable changes to agent memory, rules, skills, hooks, and settings. <br>
Mitigation: Review every proposed persistent change before applying it, and prefer scoped local changes when the correction is project-specific. <br>
Risk: The workflow may inspect prior agent history while diagnosing recurring behavior. <br>
Mitigation: Avoid installing it in environments where prior-session history should not be searched or modified. <br>
Risk: Hook or settings changes can alter later agent behavior beyond the immediate fix request. <br>
Mitigation: Use explicit /fix or fix: invocations, verify hook behavior with normal prompts, and keep enforcement changes narrowly scoped. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/fix) <br>
- [Publisher profile](https://clawhub.ai/user/drumrobot) <br>
- [SKILL.md](SKILL.md) <br>
- [Step 2 prompt improvement guide](step2-improvement.md) <br>
- [Step 3 resume guide](step3-resume.md) <br>
- [Step 4 wrap-up guide](step4-wrapup.md) <br>
- [Behavior discipline guide](behavior-discipline.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown and plain text guidance with possible code, shell command, configuration, and file-edit outputs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or update durable agent memory, rules, skill files, hooks, settings, task lists, and verification artifacts when the workflow determines those changes are needed.] <br>

## Skill Version(s): <br>
0.3.9 (source: server release metadata and changelog; SKILL.md frontmatter reports 0.1.5) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
