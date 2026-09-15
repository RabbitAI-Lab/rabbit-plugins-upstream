## Description:

Audio generation skill that selects an appropriate dLazy CLI audio or TTS model based on the prompt.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to have an agent choose and run dLazy audio-generation commands for text-to-speech, dialogue, music, and sound-effect requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media files are sent to dLazy hosted endpoints for generation.

Mitigation: Only submit prompts and media that are appropriate to share with the dLazy service.

Risk: The dLazy API key is a credential stored in local CLI configuration or passed through an environment variable.

Mitigation: Protect the key like other credentials and rotate or revoke it from the dLazy dashboard if needed.

Risk: The skill depends on a pinned third-party npm CLI.

Mitigation: Review the linked source or npm package before installing, and prefer per-use npx or a restricted local install when possible.

## Reference(s):

- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-audio-generate)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, Text]

**Output Format:** [Markdown with inline shell commands and generated-output references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return generated audio URLs hosted by dLazy media storage through the dLazy CLI.]

## Skill Version(s):

1.3.18 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
