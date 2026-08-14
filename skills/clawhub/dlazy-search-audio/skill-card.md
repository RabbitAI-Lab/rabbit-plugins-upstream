## Description:

Audio search tool: searches Pixabay Music and returns royalty-free track URLs and metadata for background music selection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search Pixabay Music through the dLazy CLI and retrieve royalty-free audio track URLs and metadata for background music selection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends user queries and API-key-authenticated requests to dLazy services.

Mitigation: Use the skill only when sending the search query to dLazy is acceptable, and review the dLazy CLI before installing or invoking it.

Risk: The CLI supports saving returned assets to a local path.

Mitigation: Use --save only with an intentional destination path chosen for the current task.

Risk: The included CLI documentation contains generic command examples and may not match the specific search_audio option names.

Mitigation: Invoke dlazy search_audio -h and prefer search_audio --query for actual searches.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-search-audio)
- [dLazy CLI project](https://github.com/dlazyai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, json, guidance]

**Output Format:** [Markdown guidance with shell command examples; CLI responses are JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires dLazy CLI authentication. Search results include audio track URLs and metadata; async calls may return a task identifier for polling.]

## Skill Version(s):

1.3.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
