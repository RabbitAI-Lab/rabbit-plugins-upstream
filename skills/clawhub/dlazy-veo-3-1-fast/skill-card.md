## Description:

Fast response and generation of short videos with Google Veo 3.1 Fast.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to generate short videos from text prompts or images, and to extend a supplied video through dLazy's hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The server security review reports a benign verdict with medium confidence; it says the CLI login step is not clearly connected to Veo generation and some references could not be checked.

Mitigation: Review the dLazy CLI and service details before logging in or providing an API key; the skill documentation says keys can be rotated or revoked from the account dashboard.

Risk: Prompts and local image, video, or audio inputs are sent to dLazy's hosted API or media storage.

Mitigation: Avoid sending confidential prompts or media unless your organization permits sharing them with the service.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-veo-3-1-fast)
- [dLazy service](https://dlazy.com)
- [CLI project (link listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Video, JSON]

**Output Format:** [Hosted video URL or saved video file, with JSON generation status and metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generation mode, duration, aspect ratio, resolution, and optional asynchronous task status.]

## Skill Version(s):

1.3.39 (source: server-resolved release metadata; artifact frontmatter lists 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
