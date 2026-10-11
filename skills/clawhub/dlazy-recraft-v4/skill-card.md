## Description:

Helps agents generate 1MP raster images with Recraft V4 for everyday creative work and rapid iteration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request raster images for everyday design work and quick visual iterations through dLazy's Recraft V4 service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing and running the dLazy CLI requires trusting the npm package and hosted service.

Mitigation: Review the package and service before installation; use the on-demand npx option if a global installation is not desired.

Risk: Prompts and any local media supplied to the CLI are sent to dLazy-hosted endpoints.

Mitigation: Avoid supplying sensitive prompts or media unless their cloud processing is acceptable.

Risk: Logging in stores an API key locally.

Mitigation: Use DLAZY_API_KEY for less persistent authentication, and rotate or revoke stored keys when necessary.

## Reference(s):

- [dLazy CLI repository (publisher-provided link)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Text with shell commands and JSON image-result links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Image results may include a hosted PNG URL; asynchronous requests return a task ID for later retrieval.]

## Skill Version(s):

1.3.27 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
