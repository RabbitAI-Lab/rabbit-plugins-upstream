## Description:

HyperFrames CLI helps agents run `npx hyperframes` commands for scaffolding, linting, visual inspection, preview, rendering, and environment troubleshooting for HyperFrames video projects.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lucas-kay8](https://clawhub.ai/user/lucas-kay8)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate the HyperFrames video development loop: create projects, validate compositions, inspect layout, preview work, render outputs, and troubleshoot the local render environment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may cause agents to run mutable npm package code while scaffolding, linting, previewing, rendering, or troubleshooting HyperFrames projects.

Mitigation: Use a pinned and reviewed HyperFrames CLI version or a lockfile-backed local install, and run commands inside a limited workspace.

Risk: The scaffold workflow can modify projects and install additional AI coding skills.

Mitigation: Review requested project changes and installed skills before use, and avoid `--non-interactive` until consent behavior is clear.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/lucas-kay8/skills/hyperframes-cli)

## Skill Output:

**Output Type(s):** [guidance, shell commands, code, configuration]

**Output Format:** [Markdown with inline shell commands and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct agents to run mutable npm-based commands that scaffold, inspect, preview, render, or modify HyperFrames projects.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
