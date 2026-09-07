## Description:

Video search tool: queries Pixabay video API by keywords and returns stock video URLs and metadata for footage sourcing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and agents use this skill to search for stock video footage by keyword and retrieve video URLs and metadata for sourcing media assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence says the skill routes through dLazy, depends on an external CLI, stores an API key, and documents prompt or file-transfer behavior.

Mitigation: Review the skill before installing, prefer the pinned npx invocation over global install when practical, keep the API key revocable, and avoid passing local file paths unless uploads to dLazy are intended.

Risk: Downloaded assets may be written to a local path supplied through the CLI.

Mitigation: Save downloads only to trusted directories and inspect output paths before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-search-video)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The invoked CLI returns JSON containing video search outputs; asynchronous runs may return a task identifier for polling.]

## Skill Version(s):

1.3.14 (source: server release evidence; artifact frontmatter reports 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
