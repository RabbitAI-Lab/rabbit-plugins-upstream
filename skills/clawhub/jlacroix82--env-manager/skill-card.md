## Description:

Scaffolds workspace-confined starter project files for Python, Node, Docker, Go, and Rust, tracks environment/service/port metadata, and returns toolchain commands as data for the calling agent to inspect and run.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jlacroix82](https://clawhub.ai/user/jlacroix82)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering agents use this skill to scaffold starter files for Python, Node, Docker, Go, and Rust projects, and to keep workspace-local environment, service, and port metadata. It returns setup and health-check commands as data for the calling agent to inspect and run separately.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup creates or overwrites starter project files and environment state on every successful setup call, with no preview or confirmation step.

Mitigation: Review the installation workspace and requested environment name before calling setup, and avoid setup when existing starter files must be preserved.

Risk: Returned command arrays are intended for a separate calling agent to execute, so running them without review could apply unwanted local toolchain actions.

Mitigation: Inspect command status and warnings first; run only entries that are expected for the target project and treat blocked or not_found entries as non-executable.

Risk: Service and port status is bookkeeping metadata, not live process control or live network truth.

Mitigation: Use service and port records as inventory hints only, and verify real runtime state with separate trusted checks when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/jlacroix82/skills/env-manager)
- [README](artifact/README.md)
- [Security audit](artifact/SECURITY-AUDIT.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration]

**Output Format:** [JSON objects and human-readable text containing scaffold metadata, warnings, generated-file status, and command arrays for the calling agent]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Setup calls write scaffold files and JSON state inside the workspace; command entries include status values such as ready, blocked, not_found, or error.]

## Skill Version(s):

3.0.8 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
