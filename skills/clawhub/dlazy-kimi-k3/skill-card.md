## Description:

Moonshot AI's Kimi K3 thinking model supports text, image, and video understanding for complex analysis, coding, and writing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agent users can use Kimi K3 for complex analysis, coding, and writing, including tasks involving image or video understanding. It requires a dLazy API key and sends prompts and selected media to dLazy's hosted service for processing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan reports benign behavior with medium confidence, but some referenced paths and the CLI package were not available for inspection.

Mitigation: Review the CLI package and required login or setup steps before installing, and proceed only if you are comfortable using the assessed and unassessed components.

Risk: Prompts and any selected local image or video files are sent to dLazy's hosted services for processing.

Mitigation: Send only prompts and media that are appropriate to share with the hosted service.

## Reference(s):

- [dLazy service homepage](https://dlazy.com)
- [@dlazy/cli package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [CLI repository listed in skill metadata](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Text, Code, JSON]

**Output Format:** [JSON response envelope containing model-generated content; content format varies by prompt]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return text or structured results; optional image and video inputs are supported, and asynchronous calls may return a task identifier.]

## Skill Version(s):

1.2.38 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
