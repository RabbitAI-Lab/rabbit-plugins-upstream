## Description:

ElevenLabs eleven_v3 text-to-speech with 12 curated multilingual voices and controls for stability, similarity, and style.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate multilingual voice audio for dubbing, audiobooks, and character dialogue through the dLazy ElevenLabs TTS wrapper.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on an external npm CLI package and a hosted dLazy service.

Mitigation: Review and trust the @dlazy/cli package before use, and prefer npx or a local or sandboxed install over a global install when possible.

Risk: Prompts, parameters, and selected local files may be sent to dLazy services for processing and output hosting.

Mitigation: Use a scoped and revocable dLazy API key, and avoid sending sensitive prompts or files unless dLazy processing and hosting are acceptable.

Risk: The artifact documents an image-style output example for a text-to-speech skill.

Mitigation: Treat the documented output schema as inaccurate until the publisher updates it, and verify returned output type and MIME metadata at runtime.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-tts)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Files, Guidance]

**Output Format:** [Markdown with inline bash commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return hosted generated output URLs, asynchronous task identifiers, or save the generated asset to a local path.]

## Skill Version(s):

1.3.15 (source: server release evidence; artifact frontmatter lists 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
