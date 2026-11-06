## Description:

The HyperFrames CLI by job - scaffold, check, look at frames, edit the timeline, preview, render locally or in the cloud, publish, project history - plus reading its JSON and recovering from build or render failures.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to create and inspect HyperFrames video projects, edit timelines, validate compositions, and render or publish videos locally or through cloud services.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill directs agents to submit public reports and may read existing AI-account credentials without first asking.

Mitigation: Get approval before public reports, provider-credential checks, or cloud uploads; use HYPERFRAMES_NO_TELEMETRY=1 to disable the documented telemetry and feedback path.

Risk: The external CLI and unbundled companion instructions were not verified in the security review.

Mitigation: Use a reviewed, fixed CLI version and scoped cloud credentials.

## Reference(s):

- [HyperFrames CLI on ClawHub](https://clawhub.ai/heygen-com/skills/hyperframes-cli)
- [Lint, validate, inspect, and snapshots](artifact/references/lint-validate-inspect.md)
- [Preview, render, and publish](artifact/references/preview-render.md)
- [Cloud rendering and authentication](artifact/references/cloud.md)
- [AWS Lambda rendering](artifact/references/lambda.md)
- [Google Cloud Run rendering](artifact/references/cloudrun.md)
- [Doctor and browser setup](artifact/references/doctor-browser.md)

## Skill Output:

**Output Type(s):** [Shell commands, Project files, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may create or modify video project files and render or publish video assets.]

## Skill Version(s):

1.0.85 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
