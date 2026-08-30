## Description:

Image search tool that queries the Pixabay image API by keyword and returns image URLs and metadata for references, backgrounds, and design assets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search for image references, backgrounds, and design assets by keyword through the dLazy CLI and hosted API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The broader dLazy CLI can perform more cloud-inference behavior than this image-search skill requires.

Mitigation: Install only if the broader CLI is acceptable, and invoke it narrowly for search_image operations.

Risk: Queries and parameters are sent to dLazy-hosted services.

Mitigation: Avoid submitting sensitive prompts or parameters unless the user accepts dLazy processing.

Risk: The CLI can persist a dLazy API key in local configuration.

Mitigation: Use normal credential hygiene, rotate or revoke keys when needed, and prefer per-invocation environment variables when persistent storage is not desired.

Risk: Local file paths passed to media fields may be uploaded, and --save can write files locally.

Mitigation: Pass local paths only when upload is intended, and choose save destinations deliberately.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-search-image)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with CLI commands and JSON responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return async task identifiers when --no-wait is used; --save can write selected assets to a local path.]

## Skill Version(s):

1.3.10 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
