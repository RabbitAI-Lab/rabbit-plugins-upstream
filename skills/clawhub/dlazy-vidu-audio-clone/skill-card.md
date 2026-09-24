## Description:

Clone a voice from reference audio with Vidu Audio Clone and generate new spoken audio from text.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to call dLazy's Vidu Audio Clone workflow, supplying reference audio and prompt text to generate cloned-voice speech.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles voice/audio samples and may upload local audio to a hosted service.

Mitigation: Use only voices and audio you own or have clear permission to clone, and confirm before uploading local files.

Risk: The skill requires dLazy credentials and can save an API key in local CLI configuration.

Mitigation: Prefer per-invocation DLAZY_API_KEY when persistent credentials are not desired, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: Hosted generation may spend account credits.

Mitigation: Use the dry-run option when estimating payloads or costs, and confirm credit use before running generation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-vidu-audio-clone)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [JSON, Files, Guidance]

**Output Format:** [JSON result with hosted generated-audio output URLs and optional async task status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; local audio inputs may be uploaded to the hosted service; supports dry-run, async no-wait, and timeout options.]

## Skill Version(s):

1.3.19 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
