## Description:

Generates 4MP high-resolution raster images through the dLazy Recraft V4 Pro CLI for print-ready and large-format assets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative automation agents use this skill to submit image prompts and generation parameters to dLazy's hosted Recraft V4 Pro service, then receive generated image URLs or save resulting assets locally.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a third-party npm CLI and dLazy-hosted APIs that require a dLazy account and API key.

Mitigation: Review the pinned CLI package before use, prefer the npx invocation when avoiding a global install, and rotate or revoke the API key from the dLazy dashboard when needed.

Risk: Prompts and any local file paths supplied for media inputs may be uploaded to dLazy-hosted services.

Mitigation: Avoid sending sensitive prompts or files unless approved for third-party processing, and use dry-run mode when validating payloads or cost estimates before generation.

Risk: Image generation may consume dLazy credits.

Mitigation: Use --dry-run to review payload and cost estimates before calling the API, and handle insufficient-balance responses by directing the user to the dLazy credits dashboard.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-recraft-v4-pro)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, files]

**Output Format:** [JSON response containing generated image metadata and hosted image URLs, with optional local image file download when --save is used]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports asynchronous task IDs with --no-wait, cost-estimate dry runs, aspect-ratio parameters, and timeout controls.]

## Skill Version(s):

1.3.20 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
