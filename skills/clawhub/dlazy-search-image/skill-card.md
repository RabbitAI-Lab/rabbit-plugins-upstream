## Description:

Image search tool: queries the Pixabay image API by keywords and returns image URLs and metadata for references, backgrounds, and design assets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can search Pixabay by keyword to find image references, backgrounds, and design assets, then use the returned image URLs and metadata.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms are sent to dLazy, and account usage may consume credits.

Mitigation: Avoid including sensitive terms and review expected credit use before running searches.

Risk: Using `dlazy login` stores the API key in the local CLI configuration.

Mitigation: Use the documented `DLAZY_API_KEY` environment variable when you prefer not to save the key locally; rotate or revoke keys from the dLazy dashboard when needed.

## Reference(s):

- [CLI source repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [JSON, Image URLs, Image metadata]

**Output Format:** [JSON containing image result URLs and metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Searches can be paginated and filtered by image type and orientation.]

## Skill Version(s):

1.3.36 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
