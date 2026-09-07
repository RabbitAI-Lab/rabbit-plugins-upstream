## Description:

Generates ElevenLabs eleven_v3 multi-voice dialogue audio by assigning voices to dialogue lines, supporting up to 10 unique voices and audio tags such as [giggling] and [whispers].

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate multi-speaker dialogue audio for character dialogue, podcasts, short skits, and similar voiceover workflows through the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cloud generation sends prompts, parameters, and any intended uploaded media files to dLazy services.

Mitigation: Review the dLazy CLI source and npm package before use, and avoid passing sensitive local files unless upload is intended.

Risk: A saved dLazy API key or global CLI installation can persist local access beyond a single invocation.

Mitigation: Prefer npx or other on-demand execution where practical, provide only the needed API key, and rotate or revoke keys from the dLazy dashboard when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-dialogue)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, JSON, Files, Guidance]

**Output Format:** [Markdown instructions with CLI commands and JSON responses; generated audio may be returned as hosted URLs or saved files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key and npm or npx; on-demand npx execution is available.]

## Skill Version(s):

1.3.13 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
