## Description:

Fitness Daily helps an agent record daily fitness-habit check-ins, generate completion reports, track multi-day trends, and summarize status from a four-category, 15-item checklist.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wwumit](https://clawhub.ai/user/wwumit)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to run a personal fitness accountability checklist, store daily completion records, and produce readable progress reports. It is not medical, nutrition, or professional training advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The checklist may be mistaken for medical, nutrition, or professional training advice.

Mitigation: Treat the checklist as personal habit guidance only, adapt it to individual circumstances, and consult a qualified professional for medical, nutrition, or training concerns.

Risk: Fitness check-in history is stored in a local CSV file that may contain sensitive personal habit data.

Mitigation: Review the log path before use, protect or relocate the CSV file as needed, and avoid storing sensitive details beyond the checklist values.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wwumit/skills/fitness-daily)
- [Publisher profile](https://clawhub.ai/user/wwumit)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Files, Guidance]

**Output Format:** [Terminal text reports with optional CSV log entries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Stores check-in history locally in a CSV file, defaulting to ~/.fitness-daily.csv unless a custom --log path is provided.]

## Skill Version(s):

1.0.0 (source: server release evidence and package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
