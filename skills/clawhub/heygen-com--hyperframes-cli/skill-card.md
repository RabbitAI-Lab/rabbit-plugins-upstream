## Description:

The HyperFrames CLI by job - scaffold, check, look at frames, edit the timeline, preview, render locally or in the cloud, publish, project history - plus reading its JSON and recovering from build or render failures.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to guide video-project work with HyperFrames, including scaffolding and checking compositions, editing timelines, previewing and rendering videos, and handling publishing or cloud-rendering workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may submit feedback to a public service, and it can read existing AI-account credentials for usage checks.

Mitigation: Set HYPERFRAMES_NO_TELEMETRY=1 to opt out; require explicit permission before account-usage checks or public reports.

Risk: Cloud rendering can upload project media, and cloud workflows can create or tear down infrastructure.

Mitigation: Review project contents before upload, restrict deployment permissions, and get explicit authorization for infrastructure creation or teardown.

Risk: Setup may install AI skills automatically.

Mitigation: Use a reviewed CLI version and disable automatic skill installation when it is not wanted.

## Reference(s):

- [HyperFrames CLI skill page](https://clawhub.ai/heygen-com/skills/hyperframes-cli)
- [Preview, render, and publish](artifact/references/preview-render.md)
- [Cloud rendering](artifact/references/cloud.md)
- [AWS Lambda rendering](artifact/references/lambda.md)
- [Google Cloud Run rendering](artifact/references/cloudrun.md)
- [Feedback and telemetry](artifact/references/feedback.md)

## Skill Output:

**Output Type(s):** [Shell commands, Files, JSON, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with shell commands; project JSON and video files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may interact with project files, feedback services, cloud rendering, and cloud infrastructure.]

## Skill Version(s):

1.0.77 (source: server-resolved release version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
