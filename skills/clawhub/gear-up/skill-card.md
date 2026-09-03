## Description:

Create and activate the smallest temporary capability needed to close a real execution gap during a task, then measure whether it helped and discard or nominate it for reuse.

This skill is ready for commercial/non-commercial use.

## Publisher:

[raguets](https://clawhub.ai/user/raguets)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use Gear Up when a task has a proven, material execution gap that existing skills, tools, context, knowledge retrieval, and Academy candidates cannot reliably close. It guides creation, validation, activation, measurement, cleanup, and possible handoff of the smallest temporary capability needed for that task.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A generated temporary tool or instruction could introduce unintended behavior or side effects.

Mitigation: Review generated artifacts, inspect dependencies and permissions, validate syntax or structure, and use dry-runs or human gates before high-impact permissions or side effects.

Risk: The workflow could be misused to create capabilities for missing knowledge, convenience, or speculative future needs.

Mitigation: Apply the six-question capability gap gate and reuse search order before creating anything.

Risk: An agent could overstate that a generated capability is active when the runtime has only written files.

Mitigation: Require explicit runtime confirmation before claiming activation; otherwise report the artifact as staged or ask for the minimal runtime action required.

## Reference(s):

- [Capability Gap Gate](references/capability-gap-gate.md)
- [Artifact Selection](references/artifact-selection.md)
- [Runtime Adapter Contract](references/runtime-contract.md)
- [Runtime Manifest Example](references/runtime-manifest.example.yaml)
- [Academy Handoff](references/academy-handoff.md)
- [ClawHub Skill Page](https://clawhub.ai/raguets/skills/gear-up)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with optional structured YAML snippets, code, configuration, and shell commands when a temporary capability is justified.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should remain scoped to the proven gap and include validation, activation status, measured outcome, and cleanup or Academy handoff details when applicable.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
