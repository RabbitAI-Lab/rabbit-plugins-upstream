## Description:

Generates speech, music, and sound effects by selecting an appropriate dLazy CLI audio or TTS model from the user's prompt.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and agent users use this skill to choose and invoke dLazy-hosted audio generation models for text-to-speech, dialogue, music, and sound effects. It is intended for workflows where prompts, parameters, and explicitly referenced media can be sent to the dLazy service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and explicitly referenced media files are sent to dLazy-hosted services for generation.

Mitigation: Use the skill only with content approved for dLazy processing, and avoid sending confidential or regulated data unless the service terms and organizational policy allow it.

Risk: The documented CLI is broader than a narrow audio-only helper and includes image and video file upload behavior.

Mitigation: Constrain agent use to the listed audio models and check `dlazy <model_name> -h` before execution.

Risk: Authentication can save a dLazy API key in the local CLI configuration.

Mitigation: Use `DLAZY_API_KEY` or `npx @dlazy/cli@1.2.3` when avoiding a global install or saved key, and rotate or revoke keys from the dLazy dashboard when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-audio-generate)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON CLI output envelopes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated media URLs are returned by the dLazy CLI and hosted on files.dlazy.com; usage requires a dLazy API key.]

## Skill Version(s):

1.3.22 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
