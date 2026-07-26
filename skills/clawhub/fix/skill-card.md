## Description: <br>
A behavior-correction skill that responds to fix-oriented feedback by analyzing the mistake, improving the relevant behavioral prompt, rule, memory, or hook, and then resuming the current work. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[drumrobot](https://clawhub.ai/user/drumrobot) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent operators use this skill when an agent repeats or risks repeating an operational mistake and needs a structured root-cause analysis, prevention update, and completion of the interrupted work. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can make durable changes to agent behavior by editing rules, memories, skill files, settings, or hooks. <br>
Mitigation: Install it only when that persistent behavior-correction workflow is desired, prefer `--plan` for review, and inspect diffs before accepting changes. <br>
Risk: The trigger phrases are broad enough that the skill may be invoked accidentally during ordinary feedback. <br>
Mitigation: Invoke it intentionally with an explicit `fix:` or `/fix` command and avoid enabling automatic behavior changes from ambiguous feedback. <br>
Risk: Changes under agent configuration directories or hook registrations can affect future sessions beyond the current task. <br>
Mitigation: Review proposed edits under `~/.claude`, `~/.agents`, `~/.gemini`, settings files, and hooks, and use local scoping when the correction should not be global. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/drumrobot/skills/fix) <br>
- [SKILL.md](artifact/SKILL.md) <br>
- [Step 2 Improvement Guide](artifact/step2-improvement.md) <br>
- [Step 3 Resume Guide](artifact/step3-resume.md) <br>
- [Step 4 Wrap-up Guide](artifact/step4-wrapup.md) <br>
- [Behavior Discipline Guide](artifact/behavior-discipline.md) <br>
- [Ambiguity Guard Hook](artifact/resources/fix-and-ambiguity-guard.sh) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown instructions with optional code, shell commands, configuration changes, and generated files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or modify persistent agent behavior artifacts such as rules, skill files, memory entries, settings, hooks, or plan documents when invoked without planning-only mode.] <br>

## Skill Version(s): <br>
0.3.8 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
