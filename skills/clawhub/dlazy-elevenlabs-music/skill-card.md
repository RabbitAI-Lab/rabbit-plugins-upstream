## Description:

Helps agents generate 10–300 seconds of original music from text prompts using ElevenLabs music_v1 through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use an agent to request background music, advertising music, and short-video soundtracks from natural-language prompts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing and running a third-party CLI locally can expose the environment to untrusted package behavior.

Mitigation: Review and trust the pinned @dlazy/cli@1.2.3 package before installing or invoking it; use the on-demand npx option if preferred.

Risk: Authentication can persist a dLazy API key in local CLI configuration.

Mitigation: Use DLAZY_API_KEY for per-invocation authentication if local key persistence is undesirable.

Risk: Files supplied to the CLI may be uploaded to dLazy services.

Mitigation: Do not pass sensitive local files unless you intend to upload them.

Risk: Copied image/video examples may misrepresent the music result format.

Mitigation: Check the actual response and asset type rather than relying on the illustrative example.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-music)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI source linked by skill metadata (not verified release provenance)](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and JSON result guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated music is returned through hosted asset URLs or saved locally; asynchronous requests can return a task ID for polling.]

## Skill Version(s):

1.3.22 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
