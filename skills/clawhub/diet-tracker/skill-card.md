## Description: <br>
Tracks daily diet and calculates nutrition information to help achieve weight loss goals. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yonghaozhao722](https://clawhub.ai/user/yonghaozhao722) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users can use this skill to log meals, estimate calories and macronutrients, check remaining daily nutrition budgets, and receive meal logging reminders for weight-loss tracking. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Meal logging can copy private diet records into an Obsidian vault and push repository contents to GitHub without clear user-facing consent. <br>
Mitigation: Review before installing and use only if this storage and sync behavior is acceptable; disable or require explicit confirmation before Obsidian or GitHub sync. <br>
Risk: Nutrition lookup and diet logging may expose sensitive personal diet information through external lookup or storage locations. <br>
Mitigation: Disclose the USDA endpoint and all storage locations before use, and prefer local-only storage unless the user opts in to external lookup or sync. <br>


## Reference(s): <br>
- [Food database](artifact/references/food_database.json) <br>
- [ClawHub skill page](https://clawhub.ai/yonghaozhao722/skills/diet-tracker) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Guidance] <br>
**Output Format:** [Markdown and text responses with nutrition summaries, diet log entries, and script-backed command guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or update daily diet log files and report estimated calories, macronutrients, remaining budgets, and predicted weight change.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release metadata and artifact _meta.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
