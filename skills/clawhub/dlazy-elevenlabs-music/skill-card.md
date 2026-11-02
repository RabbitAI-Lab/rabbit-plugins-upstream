## Description:

Generates original 10–300 second music from natural-language prompts through the dLazy hosted service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use natural-language prompts to generate music for background tracks, advertisements, and short videos. The skill submits requests to dLazy and can return a hosted media URL or save the result locally.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and any media supplied to the CLI are sent to dLazy, and generation consumes service credits.

Mitigation: Review prompts and media before sending; use --dry-run to preview the request and estimated cost.

Risk: The CLI stores an API key in the local user configuration when using its login or auth flow, and its implementation was not audited here.

Mitigation: Review the pinned CLI before installation, use DLAZY_API_KEY when you prefer not to save a key, and rotate or revoke keys through the dLazy dashboard as needed.

## Reference(s):

- [dLazy service](https://dlazy.com)
- [dLazy CLI repository (listed by the skill)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Audio files, JSON]

**Output Format:** [JSON result metadata with a hosted media URL, or a locally saved audio file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Prompt-based music generation for 10–300 seconds; supports asynchronous tasks and optional local saving.]

## Skill Version(s):

1.3.36 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
