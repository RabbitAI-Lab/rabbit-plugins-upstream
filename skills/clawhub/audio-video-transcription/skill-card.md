## Description:

Transcribes publicly accessible audio or video into text for spoken-content extraction, meeting or livestream notes, subtitles, and editing material.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dunkong](https://clawhub.ai/user/dunkong)

### License/Terms of Use:

MIT-0

## Use Case:

External users and content teams use this skill to convert audio or video files into transcripts, extract spoken scripts, organize recordings, and prepare subtitle or editing material.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends media URLs, local uploads, and API-key authenticated requests to api.we-media.cn for processing.

Mitigation: Use only when the user is comfortable sharing the media and a We-Media API key with that service.

Risk: The skill performs paid API calls after user confirmation.

Mitigation: Review the printed cost estimate and require explicit confirmation before running commands with --yes.

Risk: Server security evidence flags broader API machinery and local-file upload behavior that are not clearly disclosed for a narrow transcription release.

Mitigation: Publisher should remove unrelated endpoints and bytecode, and clearly disclose local-upload behavior before deployment.

Risk: Successful paid responses may be cached locally for 24 hours.

Mitigation: Avoid processing sensitive media unless local caching is acceptable, or clear the skill cache according to local policy after use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dunkong/skills/audio-video-transcription)
- [We-Media API](https://api.we-media.cn)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Excel files, Shell commands, Configuration guidance]

**Output Format:** [Markdown, JSON, or Excel files with terminal status markers and optional report Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a We-Media API key; paid calls require explicit confirmation; successful POST responses may be cached locally for 24 hours.]

## Skill Version(s):

1.0.1 (source: server release metadata; artifact frontmatter lists v1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
