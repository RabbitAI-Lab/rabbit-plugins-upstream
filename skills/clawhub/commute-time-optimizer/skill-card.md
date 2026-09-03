## Description:

Commute Time Optimizer helps users compare housing, job, travel-mode, and hybrid-office choices by calculating weekday rush-hour commute time, annual time and money costs, multi-year tradeoffs, and schedule options.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT

## Use Case:

External users and employees use this skill to evaluate commute tradeoffs when choosing where to live, comparing job offers, selecting a travel mode, or planning hybrid office days. It is intended for local decision support using user-provided route assumptions rather than real-time routing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Commute routes, schedules, home options, and job locations can reveal personal information.

Mitigation: Run calculations locally and avoid sharing sensitive route or schedule details in prompts, logs, or public artifacts.

Risk: The model provides decision-support estimates from editable assumptions, not real-time routing or guaranteed traffic predictions.

Mitigation: Use observed commute times, confirm office-day constraints, and review the model assumptions before relying on recommendations.

## Reference(s):

- [Commute Cost Model](references/commute-model.md)
- [Server-resolved source repository](https://github.com/voronindenis5/commute-time-optimizer)
- [ClawHub skill listing](https://clawhub.ai/voronindenis5/skills/commute-time-optimizer)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and optional JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Calculations run locally from user-provided commute assumptions.]

## Skill Version(s):

1.0.1 (source: server release metadata; artifact frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
