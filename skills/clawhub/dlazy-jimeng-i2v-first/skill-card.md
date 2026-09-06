## Description:

Generate dynamic videos from a first-frame image and prompt using Jimeng through the dLazy hosted API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to generate Jimeng image-to-video outputs from a prompt and a first-frame image through the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media files are sent to dLazy hosted endpoints for inference and media storage.

Mitigation: Review input prompts and media for sensitive content before use, and apply the relevant service terms and organizational data-handling policy.

Risk: Using the skill requires a dLazy API key and may consume account credits.

Mitigation: Use a scoped, revocable organization key, store it through the documented CLI authentication flow or environment variable, and use dry-run cost checks when appropriate.

Risk: The security evidence notes documentation quality issues around the --firstFrame versus --image examples and video versus image output format.

Mitigation: Confirm the active CLI interface with `dlazy jimeng-i2v-first -h` and validate returned output types before relying on automation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-i2v-first)
- [dLazy homepage](https://dlazy.com)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON, Media URLs]

**Output Format:** [Markdown guidance with CLI commands and JSON response objects; generated media is returned as hosted URLs or saved when requested.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; supports dry-run cost checks, asynchronous task IDs, polling, and optional local saving.]

## Skill Version(s):

1.3.12 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
