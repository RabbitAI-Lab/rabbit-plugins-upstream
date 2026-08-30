## Description:

Use ACE-Step API to generate music, edit songs, and remix music. Supports text-to-music, lyrics generation, audio continuation, and audio repainting. Use this skill when users mention generating music, creating songs, music production, remix, or audio continuation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huanmeng9527](https://clawhub.ai/user/huanmeng9527)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate an ACE-Step API service for text-to-music generation, lyric-guided song creation, remixing, and audio continuation. It helps agents prepare commands, configuration, and workflow guidance for generating and retrieving local audio outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Lyrics, prompts, or unreleased musical material may be sent to a local, custom, or cloud ACE-Step API endpoint.

Mitigation: Verify the configured API URL before use and avoid sending sensitive material to an endpoint the user does not trust.

Risk: API credentials may be stored in the skill configuration.

Mitigation: Store API keys carefully, use the script's masked key-checking commands, and avoid exposing config contents in logs or chat.

Risk: Generated audio and JSON task results are written to the local acestep_output directory.

Mitigation: Review generated files before sharing them and clear outputs that contain private prompts, lyrics, or draft music.

## Reference(s):

- [ACE-Step API Reference](artifact/api-reference.md)
- [ClawHub skill page](https://clawhub.ai/huanmeng9527/skills/acestep)
- [ACE Music API key page](https://acemusic.ai/api-key)
- [jq download page](https://jqlang.github.io/jq/download/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline bash commands; generated runs can save JSON task results and audio files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill uses curl and jq, calls a configured ACE-Step API endpoint, and saves generated outputs under acestep_output.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
