## Description:

Video search tool: queries Pixabay video API by keywords and returns stock video URLs and metadata for footage sourcing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search for stock video footage by keyword and retrieve video URLs and metadata for media sourcing workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release is marked suspicious because search instructions are mixed with generation/file-upload behavior and mandatory billing/API-key flows.

Mitigation: Review before installing, prefer npx or a contained environment, and require explicit user confirmation after credential or billing changes.

Risk: The skill requires a dLazy API key and may save credentials in local CLI configuration.

Mitigation: Treat the API key as a secret, rotate or revoke it from the dLazy dashboard when needed, and use per-invocation environment variables when that better fits the environment.

Risk: Local media paths passed to image, video, or audio fields may be uploaded to dLazy-hosted storage.

Mitigation: Do not pass local media paths unless upload to dLazy is intended and acceptable for the data involved.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-search-video)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, json]

**Output Format:** [Markdown guidance with shell commands and JSON response examples; CLI calls return JSON containing video URL metadata.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires npm or npx and a dLazy API key; async calls may return a task identifier for polling.]

## Skill Version(s):

1.3.15 (source: server release metadata; artifact frontmatter lists 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
