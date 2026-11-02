## Description:

Image search tool: queries Pixabay image API by keywords and returns image URLs and metadata for references, backgrounds, and design assets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Designers and other users can search Pixabay by keyword and retrieve image URLs and metadata for reference images, backgrounds, and design assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms are sent to dLazy, and requests may incur credit charges.

Mitigation: Review search terms before sending them and use --dry-run to inspect the payload and cost estimate before making a request.

Risk: The login flow saves an API key in the local CLI configuration.

Mitigation: Use the documented DLAZY_API_KEY environment-variable option if you prefer not to save the key locally; rotate or revoke keys from the dLazy dashboard when needed.

Risk: The documented example uses --prompt while the option list specifies --query.

Mitigation: Check the installed command's help with dlazy search_image -h and follow the current option names.

## Reference(s):

- [CLI repository (linked in skill metadata)](https://github.com/dlazy-ai/cli)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [JSON, Image URLs, Image metadata]

**Output Format:** [JSON search results with image URLs and metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search results can be filtered by image type, orientation, page, result count, and language; an asset can optionally be saved to a local path.]

## Skill Version(s):

1.3.37 (source: server-resolved ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
