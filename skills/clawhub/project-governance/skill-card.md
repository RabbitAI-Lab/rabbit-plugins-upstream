## Description:

Sets up and maintains a governance workspace for long-running AI-assisted projects, including project rules, file indexes, session handoffs, changelogs, version records, and parameter registries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[century0327](https://clawhub.ai/user/century0327)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI-assisted project teams use this skill to scaffold and maintain durable governance files so agents can find authoritative files, track decisions, avoid repeated mistakes, and resume work across sessions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated governance files may replace existing project governance if --force is used.

Mitigation: Review existing governance files first and use --force only when intentional replacement is desired.

Risk: Default templates may not match a project's actual permission zones, autonomy levels, artifact locations, or parameter policy.

Mitigation: Review and customize the generated AGENTS.md and registries before relying on them for agent behavior.

Risk: Automatic skill discovery and instruction loading are documented primarily for Trae, while other agents may behave differently.

Mitigation: Use the generated agent-neutral governance files explicitly and validate behavior in the target agent before depending on automatic loading.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/century0327/skills/project-governance)
- [README](artifact/README.md)
- [Skill Instructions](artifact/SKILL.md)
- [Example Workflow](artifact/examples/example-workflow.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and generated local governance files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates and updates project governance files; the CLI is deterministic and does not overwrite existing files unless --force is used.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
