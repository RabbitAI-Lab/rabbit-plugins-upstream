## Description:

Searches Pixabay Music and returns royalty-free track URLs and metadata for background music selection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to find background music candidates by short style keywords, with optional duration and result-count filters. It is intended to return track URLs and metadata that can be reviewed before use.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on a third-party dLazy CLI and hosted service that uses persistent credentials.

Mitigation: Use npx or an isolated install, store a dedicated revocable API key, and rotate or revoke credentials from the dLazy dashboard when no longer needed.

Risk: Search inputs and any explicitly passed local file paths may be sent to dLazy endpoints.

Mitigation: Avoid sensitive prompts and do not pass local file paths unless uploading those files to the service is intended.

Risk: The security scan found inconsistent command documentation around prompt, image, and video references.

Mitigation: Check `dlazy search_audio -h` before execution and prefer the documented `--query`, duration, and pagination options for audio search.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-search-audio)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, shell commands, json, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search results include track URLs and metadata; asynchronous runs may return a generateId for polling.]

## Skill Version(s):

1.3.14 (source: server release metadata; artifact frontmatter says 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
