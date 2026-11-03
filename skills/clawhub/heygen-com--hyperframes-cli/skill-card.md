## Description:

The HyperFrames CLI by job - scaffold, check, look at frames, edit the timeline, preview, render locally or in the cloud, publish, project history - plus reading its JSON and recovering from build or render failures.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use the HyperFrames CLI to scaffold and edit video projects, check and preview them, and render or publish finished videos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow directs the agent to submit post-render feedback to a public channel, which may expose identifying or project details if a report is not sanitized.

Mitigation: Set HYPERFRAMES_NO_TELEMETRY=1 or require approval before each public submission; remove identifying paths, names, secrets, and credentials from reports.

Risk: The workflow recommends AI-provider usage checks that inspect existing account credentials.

Mitigation: Skip routine usage checks unless the user authorizes them.

Risk: The external CLI implementation was not verified by the artifact review and may process credentials or project data during rendering and uploads.

Mitigation: Use a reviewed CLI version, consider --skip-skills, and render locally for private projects.

## Reference(s):

- [ClawHub listing](https://clawhub.ai/heygen-com/skills/hyperframes-cli)
- [Initialize and scaffold projects](references/init-and-scaffold.md)
- [Lint, check, and inspect projects](references/lint-validate-inspect.md)
- [Preview, render, and publish](references/preview-render.md)
- [Cloud rendering](references/cloud.md)
- [FFmpeg downloads](https://ffmpeg.org/download.html)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance, Video files]

**Output Format:** [Markdown guidance with shell command examples and JSON configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may create or upload video project files and rendered videos when run.]

## Skill Version(s):

1.0.80 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
