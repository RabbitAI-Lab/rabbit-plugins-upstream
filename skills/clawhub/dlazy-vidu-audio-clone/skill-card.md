## Description:

Clone a voice from reference audio and generate spoken audio for new text using Vidu Audio Clone.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to invoke dLazy's hosted Vidu Audio Clone workflow for authorized voice cloning and text-to-speech audio generation from reference audio.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill enables voice cloning without evidence of built-in consent safeguards.

Mitigation: Use it only with voices and reference audio the user is authorized to clone.

Risk: Reference audio, prompt text, and generated results may be processed by dLazy and hosted on dLazy file services.

Mitigation: Avoid sensitive inputs unless the deployment accepts dLazy processing and hosting terms.

Risk: Authentication may save a dLazy API key in local CLI configuration.

Mitigation: Use per-command DLAZY_API_KEY or npx for lower persistence, and rotate or revoke keys when no longer needed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-vidu-audio-clone)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Guidance]

**Output Format:** [Markdown instructions with CLI commands and JSON responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted generated-result URLs or an asynchronous task identifier for later polling.]

## Skill Version(s):

1.3.17 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
