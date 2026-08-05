## Description:

Env Manager scaffolds starter files for Python, Node, Docker, Go, and Rust projects, tracks environment, service, and port metadata, and returns structured toolchain commands for the calling agent to inspect and run.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jlacroix82](https://clawhub.ai/user/jlacroix82)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to initialize common project skeletons in a workspace and keep lightweight environment, service, and port inventory while deciding which generated toolchain commands to run.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Malformed setup input may create directories outside the promised workspace because of a type validation and path confinement gap.

Mitigation: Until the bug is fixed, pass only documented setup types (python, node, docker, go, rust) and sanitized environment names, and review generated file paths before accepting writes.

Risk: Every setup call writes or overwrites scaffold and state files without a preview step.

Mitigation: Use the skill in a disposable or version-controlled workspace and inspect changes before keeping them.

Risk: The skill returns toolchain commands for a calling agent to run.

Mitigation: Inspect command entries before execution, run only expected commands, and do not run entries marked blocked or not_found.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/jlacroix82/skills/env-manager)
- [README](artifact/README.md)
- [Security audit](artifact/SECURITY-AUDIT.md)

## Skill Output:

**Output Type(s):** [Text, Code, Shell commands, Configuration]

**Output Format:** [JSON objects and plain text summaries; scaffold files and JSON state are written to the workspace.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill returns commands as data for the calling agent; it does not execute generated commands.]

## Skill Version(s):

3.0.8 (source: server release metadata and clawhub.yaml)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
