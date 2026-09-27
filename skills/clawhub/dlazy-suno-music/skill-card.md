## Description:

Suno music generation model that supports inspiration mode, custom lyrics, vocal tracks, and instrumental music through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate music through the dLazy-hosted Suno workflow, including auto-lyric inspiration mode and custom lyric mode. It is useful when an agent needs to prepare a dLazy CLI invocation, return generation status, or save generated media.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local media files are sent to dLazy hosted services for generation.

Mitigation: Avoid sending sensitive content unless the user's data-handling requirements allow use of the dLazy service.

Risk: The dLazy CLI can store the API key in the local user configuration.

Mitigation: Use per-invocation DLAZY_API_KEY for sessions where persistent local credential storage is not desired, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: The skill depends on a third-party CLI package.

Mitigation: Review the pinned dLazy CLI package and source before installing it in sensitive environments.

Risk: The documentation contains a mismatched sample output, so returned media type examples may not match music generation expectations.

Mitigation: Validate the actual JSON response and media URLs before building downstream automation around the output.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-suno-music)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [JSON response with generated media URLs, plus optional downloaded media when --save is used]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Async mode can return a generation task identifier for later polling.]

## Skill Version(s):

1.3.19 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
