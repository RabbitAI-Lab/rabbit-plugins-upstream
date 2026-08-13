## Description:

Versatile video generation with Kling v3 Omni, supporting prompts and multimodal image or video references to create dynamic generated media.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to invoke dLazy's Kling v3 Omni video generation from an agent, supplying prompts and optional image, video, or audio references. The skill returns generated media URLs or asynchronous task identifiers through the dLazy CLI/API flow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill invokes a third-party dLazy CLI package and hosted API.

Mitigation: Confirm trust in the dLazy CLI package and service before installing or invoking the skill.

Risk: Prompts and selected local media are sent to dLazy services for generation.

Mitigation: Avoid passing private or sensitive media unless the user is comfortable uploading it to dLazy.

Risk: The CLI can persist an API key in local user configuration.

Mitigation: Use npx @dlazy/cli@1.2.3 or DLAZY_API_KEY when less local persistence is preferred.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-kling-v3-omni)
- [Publisher profile](https://clawhub.ai/user/dlazyai)
- [dLazy CLI homepage](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Configuration, JSON]

**Output Format:** [Markdown guidance with CLI commands and JSON result references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated outputs are returned as dLazy-hosted media URLs, or as asynchronous task identifiers when no-wait mode is used.]

## Skill Version(s):

1.3.6 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
