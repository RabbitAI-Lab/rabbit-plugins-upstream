## Description:

视频深读 video-digest turns user-provided YouTube links or video IDs into Chinese structured notes with timestamps, fact/opinion separation, follow-up transcript retrieval, and content-angle prompts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bonniegeng-max](https://clawhub.ai/user/bonniegeng-max)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to turn YouTube videos with available subtitles into concise Chinese learning notes and reusable local transcript archives. It supports single-video deep reads, small-batch triage, timestamped follow-up questions, and social-media topic ideation without drafting a full article by default.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: YouTube metadata, transcripts, and generated notes are stored locally and may reveal viewing or research interests.

Mitigation: Use a trusted output directory, pass --out for sensitive work, and delete saved video folders when the notes are no longer needed.

Risk: The skill depends on yt-dlp and proxy access to YouTube, and authenticated proxy URLs may be visible to local process-inspection tools while commands run.

Mitigation: Install and update yt-dlp intentionally, prefer credential-free local proxy URLs, and avoid long-lived proxy passwords in HTTPS_PROXY.

Risk: Generated notes may overstate or blur what the source video actually supports.

Mitigation: Use the timestamped transcript evidence, preserve fact/opinion separation, and mark uncertain claims as needing verification.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/bonniegeng-max/skills/video-digest)
- [Note template](references/note_template.md)
- [TED conversation example](references/examples/example_ted_conversation.md)
- [vLLM Shorts example](references/examples/example_vllm_shorts.md)

## Skill Output:

**Output Type(s):** [markdown, text, shell commands, guidance]

**Output Format:** [Chinese Markdown notes and timestamped text, with local meta.json, transcript.txt, and note.md files when a video is processed.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires python3, yt-dlp, and a working local proxy for YouTube access; reuses saved transcripts for follow-up retrieval and does not perform local transcription when subtitles are unavailable.]

## Skill Version(s):

1.1.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
