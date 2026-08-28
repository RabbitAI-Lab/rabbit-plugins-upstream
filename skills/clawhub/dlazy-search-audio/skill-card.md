## Description:

Audio search tool that searches Pixabay Music and returns royalty-free track URLs and metadata for background music selection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent to search for background music candidates through dLazy and receive track metadata and URLs for selection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a dLazy API key and may store or pass that credential through the dLazy CLI.

Mitigation: Use the documented dLazy authentication flow or per-invocation environment variable, and rotate or revoke organization keys when access changes.

Risk: Audio-search queries are sent to dLazy's hosted API at api.dlazy.com.

Mitigation: Use the skill only when the user is comfortable with dLazy's cloud service, and avoid sending sensitive or unrelated query content.

Risk: The --save option writes a downloaded result to a local path.

Mitigation: Use --save only with a destination path where the user intentionally wants the result written.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-search-audio)
- [dLazy publisher profile](https://clawhub.ai/user/dlazyai)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [shell commands, json, guidance, configuration]

**Output Format:** [JSON command output with concise text guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns audio result metadata and track URLs; asynchronous mode can return a task identifier, and --save can download a selected result to an intentional local path.]

## Skill Version(s):

1.3.10 (source: server release metadata; artifact frontmatter lists 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
