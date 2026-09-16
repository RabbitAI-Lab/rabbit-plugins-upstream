## Description:

Video search tool: queries Pixabay video API by keywords and returns stock video URLs and metadata for footage sourcing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and agent users use this skill to search for stock video footage by keyword and retrieve video URLs and metadata through the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on a third-party hosted service and npm CLI, so prompts, parameters, and relevant media inputs may be sent to dLazy endpoints.

Mitigation: Install only in environments where dLazy service use is acceptable, prefer npx or an isolated environment, and review the dLazy CLI source or package before use near sensitive files or credentials.

Risk: Authentication uses a dLazy API key stored in local CLI configuration or supplied through an environment variable.

Mitigation: Use a revocable API key, keep it scoped to the intended organization, and rotate or revoke it from the dLazy dashboard when access is no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-search-video)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON API output examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the dLazy CLI and a dLazy API key; search results are returned as JSON outputs containing stock video metadata and URLs.]

## Skill Version(s):

1.3.17 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
