## Description:

Video search tool that queries the Pixabay video API by keyword and returns stock video URLs and metadata for footage sourcing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and agent users use this skill to search for stock video footage by keyword, category, duration, and video type, then consume returned video URLs and metadata in downstream content workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search queries and task parameters are sent through dLazy's hosted service.

Mitigation: Install and use the skill only when a dLazy-mediated workflow is acceptable for the data being searched.

Risk: A persistent dLazy API key may be stored in the local CLI configuration.

Mitigation: Use per-run DLAZY_API_KEY for temporary credentials, or review and manage ~/.dlazy/config.json when persistent authentication is not desired.

Risk: The search workflow should only need keyword and filter parameters, but the CLI supports local file inputs for other dLazy tools.

Mitigation: Avoid passing local files to this skill unless a future version explicitly requires them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-search-video)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, JSON]

**Output Format:** [Markdown guidance with shell commands; runtime command output is JSON containing video search results, URLs, and metadata.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires npm or npx, a dLazy API key, and outbound access to api.dlazy.com and files.dlazy.com; supports async task polling and optional local download.]

## Skill Version(s):

1.3.10 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
