## Description:

Bootstrap-only skill that installs the StateRoot CLI from official release assets and runs once-per-machine setup so local agent harnesses get hooks and the built-in session skill.

This skill is ready for commercial/non-commercial use.

## Publisher:

[usama04](https://clawhub.ai/user/usama04)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this bootstrap skill to install StateRoot, run global setup, and initialize a project only when they want local cross-agent continuity. The skill expires after setup and points agents to the CLI-provided built-in StateRoot skill for daily use.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill installs a local CLI and can lead to persistent local agent integrations.

Mitigation: Review the installer source or use the MSI/downloaded script path, run `stateroot setup --dry-run` first when appropriate, and use `stateroot uninstall` to remove integrations later.

Risk: Pipe-to-shell installation can execute remote release scripts.

Mitigation: Ask for user confirmation before piping installer scripts, prefer a manually reviewed installer when the user hesitates, and use only official GitHub release assets.

Risk: Setup and project initialization write local configuration, harness hooks, and optional project state.

Mitigation: Run setup only for intentional StateRoot onboarding, run `stateroot init` only in projects that should have StateRoot state, and avoid manually creating StateRoot directories.

## Reference(s):

- [ClawHub StateRoot listing](https://clawhub.ai/usama04/skills/stateroot)
- [StateRoot homepage](https://stateroot.dev)
- [Installation documentation](https://stateroot.dev/docs/getting-started/installation)
- [Setup documentation](https://stateroot.dev/docs/getting-started/setup)
- [Privacy guide](https://stateroot.dev/docs/guides/privacy)
- [StateRoot releases](https://github.com/CognizTech/stateroot/releases)
- [Install reference](references/install.md)
- [Disclosure reference](references/disclosure.md)
- [Failure handling reference](references/failures.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Bootstrap instructions only; requires confirmation before pipe-to-shell installation and expires after setup.]

## Skill Version(s):

1.1.0 (source: server release metadata and skill manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
