## Description:

The HyperFrames CLI by job - scaffold, check, look at frames, edit the timeline, preview, render locally or in the cloud, publish, project history - plus reading its JSON and recovering from build or render failures.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to create and edit HyperFrames video projects, inspect and validate compositions, and preview or render videos locally or through cloud services.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill directs public feedback and coding-agent account checks without a separate opt-in.

Mitigation: Require explicit approval before feedback or account checks; set HYPERFRAMES_NO_TELEMETRY=1 to disable feedback when unwanted.

Risk: Cloud rendering and deployment can upload project content or change cloud infrastructure.

Mitigation: Review uploads deliberately and require approval before infrastructure changes; use --skip-skills to avoid installing the additional skill pack.

## Reference(s):

- [HyperFrames CLI skill guide](artifact/SKILL.md)
- [Initialize projects and capture websites](artifact/references/init-and-scaffold.md)
- [Lint, check, and inspect frames](artifact/references/lint-validate-inspect.md)
- [Preview, render, and publish](artifact/references/preview-render.md)
- [Managed cloud rendering](artifact/references/cloud.md)
- [AWS Lambda rendering](artifact/references/lambda.md)
- [Google Cloud Run rendering](artifact/references/cloudrun.md)
- [CLI conventions](artifact/references/conventions.md)
- [Compare projects and batch rendering](artifact/references/compare-and-batch.md)
- [Browser setup and diagnostics](artifact/references/doctor-browser.md)
- [Feedback reporting](artifact/references/feedback.md)
- [HeyGen CLI authentication reference](https://github.com/heygen-com/heygen-cli)
- [FFmpeg downloads](https://ffmpeg.org/download.html)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, JSON examples]

**Output Format:** [Markdown guidance with shell command examples, JSON snippets, and project configuration instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples use project paths, timestamps, render options, and cloud settings as parameters.]

## Skill Version(s):

1.0.75 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
