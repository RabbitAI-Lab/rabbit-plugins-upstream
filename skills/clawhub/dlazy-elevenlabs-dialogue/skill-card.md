## Description:

Helps generate multi-voice ElevenLabs dialogue audio from voice-assigned lines, with optional emotion tags.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to prepare and generate character dialogue, podcasts, or short skits with distinct voices and optional delivery cues.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running an external npm package or installing it globally exposes the environment to third-party code.

Mitigation: Review the @dlazy/cli package and source before installing; use the documented npx option to avoid a persistent global install.

Risk: CLI authentication can save an API key in local configuration.

Mitigation: Pass DLAZY_API_KEY per invocation if you do not want the key stored in ~/.dlazy/config.json.

Risk: Prompts and supplied media files are sent to dLazy endpoints.

Mitigation: Review inputs before submission and avoid sending sensitive material unless the service is approved for it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-dialogue)
- [dLazy CLI source (listed in metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The service may return an audio asset URL or a task ID for asynchronous generation; the CLI can save the result locally.]

## Skill Version(s):

1.3.21 (source: ClawHub release metadata; artifact frontmatter lists 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
