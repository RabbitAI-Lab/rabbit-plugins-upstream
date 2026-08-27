## Description:

Structured Decision Expert turns upstream multi-dimensional findings into auditable decision blocks with verdicts, weighted scores, counter-evidence, and prioritized actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and business analysts use this skill to convert upstream product, market, or operational analysis into a standardized decision block that can be reviewed, reported, and monitored.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Decision inputs, prompts, media-derived evidence, and generated artifacts may be processed through LinkFox API-backed services.

Mitigation: Use only data approved for that processing path, and get explicit user confirmation before sending sensitive business context, private files, or media-derived evidence.

Risk: Counter-evidence monitoring can create recurring scheduled tasks that persist after the initial decision workflow.

Mitigation: Confirm each scheduled task with the user, record its purpose and cadence, and verify how to stop or delete it before relying on recurring monitoring.

Risk: The bundled upload helper can publish local files to publicly accessible OSS URLs.

Mitigation: Upload only files the user has confirmed are safe to make public, and avoid public upload for confidential material.

Risk: Generated decision blocks may look definitive even when upstream evidence is incomplete or stale.

Mitigation: Preserve upstream limitations, display counter-evidence conditions, and rerun the decision workflow when hard constraints or monitored assumptions change.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-expert-structured-decision-making)
- [Structured Decision Block Input Schema](artifact/skills/structured-decision-block/references/structured-decision-block-input-schema.json)
- [Structured Decision Block Output Example](artifact/skills/structured-decision-block/references/structured-decision-block-output-example.md)
- [Structured Decision Block Engine](artifact/skills/structured-decision-block/scripts/decision_block.py)
- [Task Scheduler API Reference](artifact/skills/linkfox-task-scheduler/references/api.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Files, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown decision blocks, structured JSON, HTML report files, scheduled-task configuration, and concise text summaries.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include local report/data files and persistent monitoring task definitions when the user asks to track counter-evidence.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
