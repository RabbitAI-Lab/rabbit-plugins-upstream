## Description:

ElevenLabs eleven_v3 text-to-speech with 12 curated multilingual voices and stability, similarity, and style controls for dubbing, audiobooks, and character dialog.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate ElevenLabs text-to-speech audio through the dLazy CLI, with selectable multilingual voices and voice controls for narration, dubbing, audiobooks, and character dialog.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and any local media files supplied to the CLI are sent to dLazy-hosted services.

Mitigation: Only submit content approved for that service, and avoid passing local files that should not be uploaded.

Risk: The dLazy API key may be stored in the local CLI configuration.

Mitigation: Use scoped, revocable keys, rotate or revoke keys when needed, and restrict access to the local config file.

Risk: The skill depends on an npm CLI package that can be installed globally.

Mitigation: Review the linked package or source before installation, and prefer the pinned npx invocation or an isolated environment for sensitive systems.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-tts)
- [dLazy CLI repository](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Files, Text]

**Output Format:** [JSON response containing generated audio asset URLs, with an optional local audio file when saved]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports dry-run cost estimates, asynchronous task polling, and saving returned assets to a local path.]

## Skill Version(s):

1.3.14 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
