## Description:

Image search tool: queries Pixabay image API by keywords and returns image URLs and metadata for references, backgrounds, and design assets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, designers, and agents use this skill to search for image references, backgrounds, and design assets by keyword and retrieve image URLs with metadata.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search inputs and parameters are sent to dLazy endpoints rather than directly to Pixabay.

Mitigation: Install and use the skill only when routing image search through dLazy is acceptable for the intended data.

Risk: The CLI may store a dLazy API key in a local user configuration file.

Mitigation: Use the npx or DLAZY_API_KEY per-invocation path when less persistent credential storage is preferred, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: The skill relies on an external pinned npm CLI.

Mitigation: Review the referenced CLI source and package before installation, and keep installation limited to trusted environments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-search-image)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [JSON, Image URLs, Metadata, Shell commands, Guidance]

**Output Format:** [JSON returned by the dLazy CLI, with image URLs and metadata for matching assets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports query, image type, orientation, pagination, language, dry-run, async task, timeout, and save-path options.]

## Skill Version(s):

1.3.19 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
