## Description:

Guides agents through developing, checking, previewing, and rendering HyperFrames video compositions with the CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative teams use this skill to guide agents through scaffolding, testing, previewing, and rendering HyperFrames video projects locally or in supported cloud environments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Default public feedback submissions may disclose project details, logs, reproduction commands, or client information.

Mitigation: Disable telemetry and feedback, or require approval of each sanitized feedback payload before sending it.

Risk: Running the CLI through an unpinned npx command offers less supply-chain control.

Mitigation: Prefer a project-pinned HyperFrames CLI wrapper and review commands before execution.

## Reference(s):

- [HyperFrames CLI skill release](https://clawhub.ai/heygen-com/skills/hyperframes-cli)
- [HyperFrames catalog search documentation](https://hyperframes.heygen.com/developers/catalog-search)
- [Preview, render, and feedback reference](references/preview-render.md)
- [Cloud rendering reference](references/cloud.md)
- [AWS Lambda rendering reference](references/lambda.md)
- [Google Cloud Run rendering reference](references/cloudrun.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration instructions]

**Output Format:** [Markdown with shell commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct the agent to create project files and render video using the CLI.]

## Skill Version(s):

1.0.64 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
