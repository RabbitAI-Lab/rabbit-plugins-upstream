## Description:

Configure and operate the GameLearningRuntime CLI for project setup, bounded training, run review, knowledge transfer, and verified model playback.

This skill is ready for commercial/non-commercial use.

## Publisher:

[loonghao](https://clawhub.ai/user/loonghao)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to operate existing GLR projects, including bridge startup, goal-driven training, recording, run inspection, packaging, and model playback.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Project-declared tasks can execute training or other local processes.

Mitigation: Review project manifests and local overrides before running tasks, and pass only declared parameters.

Risk: Updates can change the CLI, runtime host, and project skills.

Mitigation: Apply updates only on explicit request and confirm the intended project skills directory or binary-only scope.

Risk: Exported packages or reports may expose secrets, private endpoints, or machine-local identifiers.

Mitigation: Inspect exports and reports before sharing, and omit sensitive values and local identifiers.

## Reference(s):

- [GLR CLI release on ClawHub](https://clawhub.ai/loonghao/skills/glr-cli)
- [CLI commands and contracts](references/commands.md)
- [Data collection and rendering](references/data-collection.md)
- [Portable project packages](references/packages.md)
- [Recording guidance](references/recording.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with CLI commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Instructions and interpretation of GLR command outputs; project operations may create run artifacts and reports.]

## Skill Version(s):

0.24.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
