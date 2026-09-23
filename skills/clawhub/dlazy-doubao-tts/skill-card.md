## Description:

Synthesize Chinese or English text into natural speech using Doubao TTS through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate speech narration from text with selectable Doubao voices, language options, speed controls, and optional local saving of generated assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or run the dLazy npm CLI.

Mitigation: Review the package source and install command before use, and prefer the pinned npx invocation when a persistent global install is not required.

Risk: Authentication may store a dLazy API key in the local user configuration.

Mitigation: Use OS-level account protections, rotate or revoke keys from the dLazy dashboard when needed, and use the DLAZY_API_KEY environment variable for per-invocation credentials when appropriate.

Risk: Text prompts and explicitly passed files are sent to dLazy hosted services.

Mitigation: Avoid submitting private or sensitive content unless the service terms and data handling practices are acceptable for the intended use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-doubao-tts)
- [dLazy CLI source link from metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [JSON result with generated asset URLs, plus optional local files when the save flag is used.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; supports asynchronous task IDs and polling for completion.]

## Skill Version(s):

1.3.17 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
