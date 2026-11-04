## Description:

The HyperFrames CLI by job - scaffold, check, look at frames, edit the timeline, preview, render locally or in the cloud, publish, project history - plus reading its JSON and recovering from build or render failures.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to scaffold and inspect HyperFrames video projects, edit timelines, check and preview compositions, and render or publish videos locally or through cloud services.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow may send public feedback and use existing AI-account logins for routine account checks.

Mitigation: Get explicit approval before public feedback or account-usage checks; HYPERFRAMES_NO_TELEMETRY=1 suppresses feedback and telemetry but does not disable credential-based usage checks.

Risk: Cloud rendering can upload project content and incur account charges.

Mitigation: Review the project upload and expected costs before cloud rendering.

Risk: Sibling documentation and external CLI behavior are not fully verified.

Mitigation: Use a reviewed, pinned CLI wrapper and restrict infrastructure permissions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/heygen-com/skills/hyperframes-cli)
- [Init and scaffold](references/init-and-scaffold.md)
- [Lint, validate, inspect](references/lint-validate-inspect.md)
- [Preview and render](references/preview-render.md)
- [Cloud rendering](references/cloud.md)
- [AWS Lambda rendering](references/lambda.md)
- [Google Cloud Run rendering](references/cloudrun.md)
- [Feedback and reporting](references/feedback.md)
- [CLI conventions](references/conventions.md)
- [Compare and batch rendering](references/compare-and-batch.md)
- [Doctor and browser setup](references/doctor-browser.md)
- [Beat grids](references/beats.md)
- [Upgrade and project information](references/upgrade-info-misc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, JSON configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct the agent to create or update a video project and render or publish video files.]

## Skill Version(s):

1.0.82 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
