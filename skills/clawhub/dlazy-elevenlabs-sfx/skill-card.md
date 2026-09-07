## Description:

Generates 1-22 second sound effects from text prompts with the ElevenLabs text-to-sound model for foley, ambience, alerts, and game audio.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent to invoke the dLazy ElevenLabs SFX CLI for short sound-effect generation from text prompts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires dLazy credentials and sends requests to hosted dLazy API endpoints.

Mitigation: Use a revocable dLazy API key, rotate or revoke it when needed, and avoid sending sensitive prompt content unless the service terms are acceptable.

Risk: Installing the dLazy CLI globally increases trust in the package and account that publish the CLI.

Mitigation: Prefer on-demand npx execution or a reviewed local installation, and confirm that the package source and publisher are trusted before use.

Risk: Generated assets and any intentional file uploads are handled by the dLazy hosted service.

Mitigation: Only pass local files intended for upload and review generated outputs before downstream use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-sfx)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, files]

**Output Format:** [Markdown with inline bash commands and JSON examples; generated sound effects are returned as hosted URLs or saved files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports synchronous completion or asynchronous task IDs; generated sound effects are documented as 1-22 seconds.]

## Skill Version(s):

1.3.12 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
