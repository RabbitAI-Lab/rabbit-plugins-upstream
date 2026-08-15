## Description: <br>
Scaffolds starter files for Python, Node, Docker, Go, and Rust projects, tracks environment, service, and port metadata, and returns toolchain commands for the calling agent to review and run. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jlacroix82](https://clawhub.ai/user/jlacroix82) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent builders use this skill to create starter project files for common development stacks and keep workspace-local metadata for environments, services, and ports. The calling agent can inspect the returned command objects before deciding whether to execute them. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: File writes may be redirected outside the expected workspace if ENV_MANAGER_WORKSPACE is controlled by an untrusted caller. <br>
Mitigation: Install only in environments where that variable cannot be set by untrusted callers, or wait for the publisher to constrain the override and update the documentation. <br>
Risk: Setup calls write or overwrite scaffold files and JSON state without a preview step. <br>
Mitigation: Review the target environment name and call behavior before invoking setup, and inspect generated files before running returned commands. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jlacroix82/skills/env-manager) <br>


## Skill Output: <br>
**Output Type(s):** [text, code, shell commands, configuration] <br>
**Output Format:** [JSON objects plus human-readable command text; scaffolded project files are written to the workspace] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands are returned for agent review and execution; the skill also writes starter files and JSON environment metadata.] <br>

## Skill Version(s): <br>
3.0.6 (source: server release metadata and clawhub.yaml) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
