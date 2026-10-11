## Description:

Helps agents generate Wan 2.7 videos from text, reference media, or first and last frames through dLazy's hosted service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request video generation from prompts, reference images or videos, and first and last frames.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media are sent to dLazy's hosted service.

Mitigation: Confirm the service is appropriate for the content before sending prompts or files.

Risk: The CLI can save the API key on the local device.

Mitigation: Use an environment variable instead if local credential persistence is a concern.

Risk: Running the npm CLI installs and executes third-party software.

Mitigation: Review and trust the CLI before use; prefer the on-demand npx option to avoid a persistent global installation.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-wan2-7)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI repository (listed in skill metadata; release provenance unavailable)](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Text with shell commands and JSON result descriptions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The service returns generated-media links; results may be downloaded locally.]

## Skill Version(s):

1.3.26 (source: server-resolved release metadata; skill files state 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
