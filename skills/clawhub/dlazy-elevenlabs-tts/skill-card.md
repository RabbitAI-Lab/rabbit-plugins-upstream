## Description:

Provides ElevenLabs eleven_v3 text-to-speech through the dLazy CLI with curated multilingual voices and stability, similarity, and style controls for dubbing, audiobooks, and character dialog.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content teams use this skill to generate multilingual spoken audio from prompts for dubbing, audiobook narration, and character dialog through dLazy's hosted ElevenLabs TTS wrapper.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, selected files, and generated outputs are sent through dLazy's hosted service.

Mitigation: Avoid submitting sensitive or restricted content unless the user's data-handling requirements allow that service path.

Risk: The skill depends on the third-party @dlazy/cli npm package.

Mitigation: Prefer npx or a non-global install when possible, and review the linked package and source before use.

Risk: Authentication uses a dLazy API key that may be stored locally or passed through the environment.

Mitigation: Use a revocable organization key and rotate or revoke it when access requirements change.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-tts)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [API Calls, Files, Shell commands]

**Output Format:** [JSON result with hosted generated asset URLs and optional saved local files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports asynchronous task IDs, polling, and local save paths.]

## Skill Version(s):

1.3.13 (source: server release metadata; artifact frontmatter says 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
