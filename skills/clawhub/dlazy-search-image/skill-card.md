## Description:

Image search tool: queries Pixabay image API by keywords and returns image URLs and metadata for references, backgrounds, and design assets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, designers, and agents use this skill to search for image references, backgrounds, and design assets by keyword and receive image URLs plus metadata for downstream work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and search parameters are sent to dLazy services rather than processed only through a local Pixabay-only tool.

Mitigation: Review the request before execution and avoid sending confidential or sensitive prompts unless this use of dLazy services is acceptable.

Risk: The skill requires a dLazy API key and may save that key in the local CLI configuration.

Mitigation: Use `dlazy login`, `dlazy auth set`, or `DLAZY_API_KEY` according to local credential policy, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: Local file paths passed to image, video, or audio fields may be uploaded to dLazy media storage.

Mitigation: Only provide local paths for files intended for upload, and choose explicit save paths for downloaded assets.

Risk: The artifact contains documentation inconsistencies around command options and examples.

Mitigation: Use `dlazy search_image -h` or `--dry-run` to confirm current CLI behavior before making service calls.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-search-image)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)
- [Publisher profile](https://clawhub.ai/user/dlazyai)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON CLI responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns image URLs and metadata; may download a selected result when a save path is provided.]

## Skill Version(s):

1.3.21 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
