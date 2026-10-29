## Description:

Anthropic's latest Sonnet — near-Opus quality on coding and long-horizon agentic work at Sonnet cost. Strong at reasoning, code generation, and complex tool orchestration. Supports text, image, and video inputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users can submit prompts, images, or videos to use dLazy's hosted Claude Sonnet 5 service for reasoning, coding, and content generation. Results are returned by the CLI as structured JSON and may include generated content or downloadable assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and parameters are sent to dLazy for hosted inference, and local media supplied as input is uploaded to its media storage.

Mitigation: Submit only prompts and media you intend to share with the service, and review dLazy's pricing and privacy terms before use.

Risk: Installing the CLI runs third-party npm code, and authentication uses a dLazy API key.

Mitigation: Use the pinned CLI version and the environment-variable option if you prefer not to save an API key in the local CLI configuration.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-claude-sonnet-5)
- [Publisher profile](https://clawhub.ai/user/dlazyai)
- [dLazy service](https://dlazy.com)
- [dLazy CLI project link listed in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy API key settings](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [Text, JSON, Generated content, Media files]

**Output Format:** [JSON CLI response containing generated content or output references; optional saved asset files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts a prompt and optional image or video inputs (up to 10 images and 8 videos); output can be saved to a local path.]

## Skill Version(s):

1.2.37 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
