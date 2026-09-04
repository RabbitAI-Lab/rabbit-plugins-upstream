## Description:

Sleep Optimizer helps users collect sleep, nap, drowsiness, and life-stage information, then generates an evidence-informed sleep assessment and improvement plan with charts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[55zhang](https://clawhub.ai/user/55zhang)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to analyze sleep patterns, life-stage context, naps, and daytime drowsiness, then produce a personalized sleep improvement plan. The skill is intended for self-help planning and explicitly does not replace medical advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags broad automatic activation and under-scoped local file read/write behavior.

Mitigation: Prefer explicit invocation, review file paths before execution, and export reports only to deliberate destinations.

Risk: The skill can handle sleep-related personal data and drowsiness records.

Mitigation: Share only the minimum sleep data needed for the plan, avoid unnecessary sensitive details, and keep any local input files in trusted locations.

Risk: Sleep guidance may be mistaken for medical advice.

Mitigation: Treat outputs as self-help planning and seek clinical care for persistent insomnia, suspected sleep apnea, restless legs symptoms, or significant anxiety or depression.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/55zhang/skills/sleep-optimizer)
- [Sleep science references](references/sleep-science-references.md)
- [Lifestyle sleep references](references/lifestyle-sleep-references.md)
- [Sleep diary template](assets/sleep-diary-template.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, code, configuration, guidance]

**Output Format:** [Markdown reports with inline text charts, optional SVG chart files, and Node.js command examples.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write a Markdown report and a same-named .chart.svg file when an output path is requested.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata; artifact frontmatter reports 2.3.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
