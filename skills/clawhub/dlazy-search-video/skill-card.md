## Description:

Video search tool: queries Pixabay video API by keywords and returns stock video URLs and metadata for footage sourcing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and content-production agents use this skill to search for stock video footage by keyword and retrieve video URLs and metadata through the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses dLazy as an intermediary service rather than a direct Pixabay-only integration.

Mitigation: Install and use it only when the user accepts dLazy-hosted processing and the documented API endpoints.

Risk: Authentication can persist a long-lived dLazy API key in the local CLI configuration.

Mitigation: Prefer per-invocation DLAZY_API_KEY when possible, and rotate or revoke keys from the dLazy dashboard when access changes.

Risk: Local media paths passed to the CLI may be uploaded to dLazy media storage.

Mitigation: Avoid passing local media paths unless upload is intended and the files are approved for external processing.

Risk: The install path can execute a global npm package.

Mitigation: Prefer npx or a sandboxed project-local install, and review the package source before global installation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-search-video)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [json, shell commands, guidance]

**Output Format:** [JSON results with video URLs and metadata, plus Markdown command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return asynchronous task metadata when invoked with --no-wait.]

## Skill Version(s):

1.3.16 (source: server release metadata; artifact frontmatter reports 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
