## Description:

Video search tool: queries Pixabay video API by keywords and returns stock video URLs and metadata for footage sourcing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search for stock video footage by keyword and retrieve video URLs and metadata through the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms and explicitly provided inputs are sent to dLazy's hosted API.

Mitigation: Use the skill only when sharing those inputs with dLazy is acceptable, and avoid including confidential terms or data.

Risk: The dLazy API key may be stored in local CLI configuration.

Mitigation: Use operating-system account protections, rotate or revoke keys from the dLazy dashboard when needed, or provide the key per invocation through an environment variable.

Risk: Local file paths passed to media fields may be uploaded to dLazy media storage.

Mitigation: Avoid passing local paths unless the upload is intentional and the file is appropriate for third-party processing.

Risk: The documented CLI is a generic dLazy tool rather than a search-only executable.

Mitigation: Review the pinned CLI package before installation and prefer on-demand npx execution when a persistent global binary is not desired.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-search-video)
- [dLazy CLI Repository](https://github.com/dlazyai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [JSON returned by the dLazy CLI, with Markdown command examples in the skill documentation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results include stock video URLs and metadata; asynchronous mode may return a task identifier instead of immediate outputs.]

## Skill Version(s):

1.3.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
