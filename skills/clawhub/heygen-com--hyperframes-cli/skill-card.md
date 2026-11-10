## Description:

The HyperFrames CLI helps agents scaffold and inspect projects, edit timelines, preview and render videos, publish, review project history, and recover from build or render failures.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to create and inspect HyperFrames video projects, validate and edit compositions, preview and render videos, and troubleshoot build or rendering problems.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running the skill may use an unpinned CLI version, send feedback or usage telemetry, or start cloud operations with external effects.

Mitigation: Pin the CLI to a reviewed version; keep feedback, usage checks, uploads, and destructive cloud actions optional, and require clear authorization before running them.

## Reference(s):

- [HyperFrames CLI on ClawHub](https://clawhub.ai/heygen-com/skills/hyperframes-cli)
- [Project scaffolding](references/init-and-scaffold.md)
- [Validation and inspection](references/lint-validate-inspect.md)
- [Preview, render, and publish](references/preview-render.md)
- [Cloud rendering](references/cloud.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Project files, Video renders]

**Output Format:** [Markdown guidance, shell commands, JSON, and HyperFrames project files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or modify project files and render video outputs.]

## Skill Version(s):

1.0.88 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
