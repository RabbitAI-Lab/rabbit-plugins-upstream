## Description:

ElevenLabs eleven_v3 text-to-speech with 12 curated multilingual voices and stability, similarity, and style controls for dubbing, audiobooks, and character dialog.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent to generate ElevenLabs text-to-speech audio through the dLazy CLI, selecting voices and controls for dubbing, audiobook narration, or character dialogue.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and generated outputs are sent to dLazy-hosted services.

Mitigation: Review dLazy service handling before use, avoid submitting sensitive content unless approved, and use an organization API key that can be rotated or revoked.

Risk: The artifact output example shows image/png output for a text-to-speech skill.

Mitigation: Treat the example as a documentation error and validate actual generated output before integrating downstream automation.

Risk: Persistent global CLI installation and stored API credentials may leave a dLazy binary and API key on the system.

Mitigation: Use npx @dlazy/cli@1.2.3 for non-persistent runs when appropriate, and rotate or revoke the API key when access is no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-tts)
- [dLazy CLI source link from metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Audio files, Guidance]

**Output Format:** [Markdown guidance with bash commands and JSON result examples; generated audio is returned as hosted file URLs or saved locally with --save.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires npm or npx, a dLazy API key, and network access to dLazy-hosted API and file services.]

## Skill Version(s):

1.3.18 (source: server release evidence; artifact frontmatter lists 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
