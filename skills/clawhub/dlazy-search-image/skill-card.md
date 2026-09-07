## Description:

Image search tool that queries the Pixabay image API by keyword and returns image URLs and metadata for references, backgrounds, and design assets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and design-focused agents use this skill to find reference images, backgrounds, and design assets from keyword searches.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a dLazy cloud CLI workflow that sends prompts or queries to api.dlazy.com.

Mitigation: Review the request contents before execution and avoid sending confidential prompts or sensitive business data.

Risk: The dLazy CLI can upload local media paths to files.dlazy.com when such paths are provided.

Mitigation: Avoid passing sensitive local file paths and prefer isolated or on-demand execution after reviewing the CLI source and package provenance.

Risk: The workflow requires a dLazy API key stored locally or supplied through DLAZY_API_KEY.

Mitigation: Use scoped credentials, rotate or revoke keys from the dLazy dashboard when needed, and avoid exposing keys in command history or logs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-search-image)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [JSON, API Calls, Shell commands, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI may return image URL metadata or an asynchronous task identifier when invoked with no-wait behavior.]

## Skill Version(s):

1.3.14 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
