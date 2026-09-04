## Description:

Searches for image assets by keyword through the dLazy CLI and returns image URLs and metadata for references, backgrounds, and design assets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, designers, and agents use this skill to find reference, background, and design images by keyword and receive image URLs and metadata for downstream work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill is described as Pixabay image search, while security evidence says it requires and uses dLazy services and credentials.

Mitigation: Tell users before use that prompts and parameters are sent to dLazy, and install only after they accept the dLazy service and credential model.

Risk: The dLazy CLI can store an API key locally unless an environment variable is used.

Mitigation: Use per-invocation DLAZY_API_KEY for temporary use when appropriate, and rotate or revoke keys from the dLazy dashboard when access should change.

Risk: API calls may consume dLazy credits.

Mitigation: Use dry-run or confirm expected usage and account balance before making requests.

Risk: Local files explicitly passed to supported dLazy media fields may be uploaded to dLazy media storage.

Mitigation: Do not pass sensitive local file paths unless upload to dLazy is intended and approved.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-search-image)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Configuration, Guidance]

**Output Format:** [JSON returned by the dLazy CLI, with optional Markdown guidance from the agent]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include image URLs, metadata, or asynchronous task identifiers when --no-wait is used.]

## Skill Version(s):

1.3.13 (source: ClawHub release metadata; artifact frontmatter lists 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
