## Description:

Image search tool: queries Pixabay image API by keywords and returns image URLs and metadata for references, backgrounds, and design assets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search for image assets by keyword and retrieve image URLs plus metadata for references, backgrounds, and design materials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may expect a direct Pixabay-only integration, while server evidence identifies dLazy API endpoints, credential storage, and broader CLI behavior.

Mitigation: Review the dLazy service endpoints and terms before installation, and treat search terms plus configured dLazy API keys as data processed by dLazy services.

Risk: A persistent global CLI install may save authentication in local user configuration.

Mitigation: Use the pinned npx invocation or per-command DLAZY_API_KEY when avoiding a persistent global binary or saved key is preferred.

Risk: Local file paths or broad JSON inputs passed to the CLI may cause their contents to be processed by the service.

Mitigation: Pass only the specific query and inputs intended for image search, and avoid local files unless their upload or processing is intended.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-search-image)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The wrapped CLI returns image-search results as JSON and can optionally return an asynchronous task identifier.]

## Skill Version(s):

1.3.11 (source: server release evidence; artifact frontmatter reports 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
