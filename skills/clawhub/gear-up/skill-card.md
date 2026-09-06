## Description:

Gear Up is an Overpowered-suite skill that guides agents to create, activate, validate, measure, and discard or nominate the smallest temporary capability needed to close a real execution gap.

This skill is ready for commercial/non-commercial use.

## Publisher:

[raguets](https://clawhub.ai/user/raguets)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill when an active task has a material execution gap that installed skills, available tools, retrieved knowledge, current context, and Academy candidates cannot reliably close. It helps choose the smallest temporary artifact, validate it before use, measure whether it helped, and discard or nominate it for later evaluation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated temporary tools, skills, or context can affect sensitive data, production systems, account actions, or irreversible side effects if used without review.

Mitigation: Review generated artifacts before use, inspect permissions and dependencies, prefer dry runs, and apply human gates for high-impact actions.

Risk: A generated artifact may be treated as active even when the runtime has only written or staged it.

Mitigation: Require explicit runtime activation evidence before relying on the artifact, and report it as staged when confirmation is unavailable.

Risk: Temporary context could conflict with higher-priority user, project, or system instructions.

Mitigation: Scope temporary context to the task and verify that it does not override higher-authority instructions before activation.

## Reference(s):

- [Overpowered suite](https://github.com/raguets/overpowered)
- [Capability Gap Gate](references/capability-gap-gate.md)
- [Artifact Selection](references/artifact-selection.md)
- [Runtime Adapter Contract](references/runtime-contract.md)
- [Academy Handoff](references/academy-handoff.md)
- [Runtime Manifest Example](references/runtime-manifest.example.yaml)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with structured checklists, manifests, and code or shell snippets when a justified temporary artifact is created]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should remain task-scoped and temporary unless validated evidence supports Academy nomination.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
