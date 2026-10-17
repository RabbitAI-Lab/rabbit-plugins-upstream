## Description:

Guides evidence-based self-assessment of SRE inspection scripts, scheduled tools, agents, and human-agent teams, producing a traceable report of results and evidence gaps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thneoly](https://clawhub.ai/user/thneoly)

### License/Terms of Use:

MIT-0

## Use Case:

SRE practitioners and developers use existing inputs, outputs, logs, and independent expectations to assess inspection tools, identify missing evidence, and document limited, reproducible findings. Reports are builder self-assessments, not independent acceptance or certification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Builder self-assessment may be mistaken for independent certification or acceptance.

Mitigation: Label reports as unreviewed self-assessments and require independent review before claiming certification or acceptance.

Risk: Reviewing operational materials or running checks outside approved scope may expose sensitive data or affect production systems.

Mitigation: Limit reading, execution, and writing to explicitly supplied materials and authorized permissions; review generated reports before use.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/thneoly/skills/sre-inspection-selfcheck)
- [Task recipes and minimum evidence](artifact/references/task-recipes.md)
- [Scope and metrics](artifact/references/scope-and-metrics.md)
- [Evidence and ground-truth rules](artifact/references/evidence-and-truth.md)
- [Report template](artifact/references/report-template.md)
- [Adjudication cases](artifact/references/adjudication-cases.md)

## Skill Output:

**Output Type(s):** [Markdown, Guidance]

**Output Format:** [Markdown self-assessment report or evidence-gap checklist; optional machine-readable summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes scoped findings, evidence references, limitations, and next steps; no aggregate score]

## Skill Version(s):

1.1.0 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
