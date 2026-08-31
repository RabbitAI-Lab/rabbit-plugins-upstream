## Description:

Happy Horse 1.0 helps agents call dLazy's hosted video model for text-to-video, first-frame-to-video, reference-to-video, and video editing workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to generate or edit short videos through the dLazy Happy Horse 1.0 cloud service from an agent workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and user-supplied media are sent to dLazy's cloud service for generation.

Mitigation: Do not submit confidential or restricted content unless the user's data-handling requirements allow dLazy cloud processing.

Risk: Generated output URLs are hosted by dLazy.

Mitigation: Review generated media links before sharing them and avoid treating hosted outputs as private by default.

Risk: The CLI can save an API key in a local configuration file.

Mitigation: Use the DLAZY_API_KEY environment variable or npx for per-invocation use when persistent local credentials are not desired.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-happyhorse-1-0)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI returns generated media URLs and can save generated assets to a local path when requested.]

## Skill Version(s):

1.3.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
