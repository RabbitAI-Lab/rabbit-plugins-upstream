## Description:

Video search tool: queries Pixabay video API by keywords and returns stock video URLs and metadata for footage sourcing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and content production agents use this skill to search for stock video footage by keyword and retrieve video URLs and metadata for sourcing workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a third-party cloud CLI and sends prompts and parameters to dLazy API endpoints.

Mitigation: Avoid submitting sensitive prompts or files unless they are intended to be processed by dLazy.

Risk: The skill depends on the pinned @dlazy/cli npm package and requires npm or npx execution.

Mitigation: Review the pinned package before installation, or use npx for on-demand execution when a global install is not desired.

Risk: Authentication requires a dLazy API key stored in local configuration or supplied through DLAZY_API_KEY.

Mitigation: Store keys with appropriate local access controls, rotate or revoke keys from the dLazy dashboard when needed, and avoid exposing API keys in logs.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-search-video)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns stock video result metadata and URLs; async mode can return a generateId for later polling.]

## Skill Version(s):

1.3.19 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
