## Description:

Image search tool: queries Pixabay image API by keywords and returns image URLs and metadata for references, backgrounds, and design assets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, designers, and content creators use this skill to search for image references, backgrounds, and design assets by keyword through the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on a third-party CLI and hosted service that may receive search terms, account API keys, and local media paths intentionally provided by the user.

Mitigation: Install only after reviewing the dLazy CLI source, prefer npx or another isolated execution method, and avoid sending sensitive content unless the service is trusted.

Risk: The documentation mixes Pixabay image-search branding with a dLazy CLI and API flow.

Mitigation: Confirm the intended command and service path before use, especially when handling sensitive queries or credentials.

Risk: Authentication stores or uses a dLazy API key for requests.

Mitigation: Use per-invocation environment variables where appropriate, keep local config permissions restricted, and rotate or revoke keys from the dLazy dashboard when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-search-image)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [JSON returned by the dLazy CLI, with image URLs and metadata for matching search results.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return an asynchronous task identifier when invoked without waiting; saved assets depend on CLI options.]

## Skill Version(s):

1.3.17 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
