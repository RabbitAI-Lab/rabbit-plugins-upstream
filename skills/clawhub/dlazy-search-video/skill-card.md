## Description:

Searches Pixabay videos by keyword and returns stock footage URLs and metadata through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to find stock video footage by keyword and inspect video links and metadata for their projects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search queries and piped inputs may be sent to third-party dLazy services.

Mitigation: Avoid including sensitive data in queries or piped inputs, and use the CLI only if its service is acceptable for the task.

Risk: Authentication stores a dLazy API key in local CLI configuration.

Mitigation: Use a task-scoped key where possible, protect the configuration, and rotate or revoke the key when needed.

Risk: The CLI may upload local files or save downloaded assets when those features are used.

Mitigation: Do not pass local file paths or use --save unless upload or download is explicitly intended; prefer on-demand npx execution to a global install if desired.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-search-video)
- [dLazy CLI homepage (declared metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [JSON search results with video URLs and metadata, summarized as text when useful]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports filters for video type, category, duration, and pagination; asynchronous searches may require polling.]

## Skill Version(s):

1.3.30 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
