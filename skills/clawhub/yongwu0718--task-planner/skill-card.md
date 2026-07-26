## Description: <br>
Task Planner helps users turn unordered tasks and goals into prioritized daily, weekly, and long-term plans that account for deadlines, dependencies, available time, and personal energy patterns. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yongwu0718](https://clawhub.ai/user/yongwu0718) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users use this skill when they have many tasks, unclear priorities, or broad goals and need guided planning. The skill collects task attributes, breaks goals into actionable steps, builds weekly pools, generates daily plans, and prompts users to confirm scope, dependencies, workload, and completion criteria. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Daily-plan JSON output can contain personal planning details and may be overwritten during plan generation. <br>
Mitigation: Avoid entering sensitive private information and review the target plan file contents before relying on or sharing it. <br>
Risk: Plans depend on user-provided deadlines, availability, dependencies, and energy patterns, so unrealistic inputs can produce unrealistic schedules. <br>
Mitigation: Review the generated plan with the user, confirm workload and completion criteria, and adjust time blocks before treating the plan as actionable. <br>


## Reference(s): <br>
- [ClawHub Task Planner Release](https://clawhub.ai/yongwu0718/skills/task-planner) <br>
- [Energy Mapping Guide](references/energy_mapping.md) <br>
- [Task Attribute Prompt](references/task_attribute_prompt.md) <br>
- [Task Dump Prompt](references/task_dump_prompt.md) <br>
- [Weekly Plan Guide](references/weekly_plan_guide.md) <br>
- [Daily Plan Schema](assets/daily_plan_schema.json) <br>
- [Long-Term Plan Schema](assets/long_term_plan_schema.json) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, JSON, Files] <br>
**Output Format:** [Markdown planning tables and structured JSON plan data] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Chinese-language planning workflow; may write or overwrite a local daily-plan JSON file when producing a daily plan.] <br>

## Skill Version(s): <br>
0.1.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
