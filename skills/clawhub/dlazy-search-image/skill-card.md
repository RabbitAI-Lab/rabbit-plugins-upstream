## Description:

Image search tool: queries Pixabay image API by keywords and returns image URLs and metadata for references, backgrounds, and design assets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, designers, and agents use this skill to search for image references, backgrounds, and design assets by keyword and retrieve URLs plus metadata for downstream creative or documentation workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a third-party dLazy account and API key and sends search inputs to dLazy-hosted endpoints.

Mitigation: Confirm third-party API use is acceptable for the task and avoid submitting sensitive search terms.

Risk: The CLI can save the API key in local configuration when using login or auth setup.

Mitigation: Use DLAZY_API_KEY per invocation when persistent local credential storage is not desired, and rotate or revoke keys from the dLazy dashboard as needed.

Risk: The artifact describes local file path upload behavior for media fields in the broader CLI flow.

Mitigation: Do not pass local file paths unless upload to dLazy storage is intended.

Risk: The artifact frontmatter version differs from the server release version.

Mitigation: Use the server release version for this card and confirm the packaged artifact version before publication.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-search-image)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The invoked CLI returns JSON containing image search result URLs and metadata; asynchronous invocations may return a task identifier for polling.]

## Skill Version(s):

1.3.20 (source: server release evidence; artifact frontmatter reports 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
