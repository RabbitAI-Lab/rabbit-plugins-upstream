## Description:

Memory Optimizer creates personalized study and review plans using forgetting-curve, spaced-repetition, and retrieval-practice concepts, then can generate Markdown reports with visual review schedules through its bundled Node.js script.

This skill is ready for commercial/non-commercial use.

## Publisher:

[55zhang](https://clawhub.ai/user/55zhang)

### License/Terms of Use:

MIT-0

## Use Case:

External users and students use this skill to turn study goals, exam timelines, daily availability, and subject workloads into a practical memory-focused study plan. The agent collects planning inputs, may run the local planner script, and returns review schedules, capacity warnings, learning tactics, and optional report files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can run a bundled local Node.js planner script and write Markdown and SVG outputs.

Mitigation: Run it only in a trusted workspace and provide an output path only when creating or overwriting those files is acceptable.

Risk: The skill may activate on general study or memory questions.

Mitigation: Confirm the user wants a structured memory-optimization plan before collecting detailed study data or running the planner.

Risk: Generated study schedules and memory guidance may be incomplete or unsuitable for a user's actual constraints.

Mitigation: Treat generated plans as planning aids, review capacity warnings, and adjust timing, workload, and rest needs before relying on the plan.

## Reference(s):

- [Memory Science References](references/memory-science-references.md)
- [Study Diary Template](assets/study-diary-template.md)
- [ClawHub Skill Page](https://clawhub.ai/55zhang/skills/memory-optimizer)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Files]

**Output Format:** [Markdown guidance with optional Markdown report and SVG chart files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or overwrite a user-specified Markdown report and a same-name .chart.svg file when an output path is provided.]

## Skill Version(s):

1.0.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
