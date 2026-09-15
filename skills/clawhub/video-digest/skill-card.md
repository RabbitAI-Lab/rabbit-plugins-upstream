## Description:

Video-digest turns YouTube subtitles into structured video notes, usually in Chinese, with summaries, timestamped sections, fact/opinion separation, follow-up retrieval, and content-idea prompts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bonniegeng-max](https://clawhub.ai/user/bonniegeng-max)

### License/Terms of Use:

MIT

## Use Case:

External users, researchers, and content creators use this skill to digest YouTube videos into reusable notes, scan batches of videos, and answer follow-up questions from saved transcripts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill installs and runs yt-dlp for YouTube subtitle fetching, and the dependency is not pinned by the release metadata.

Mitigation: Pin the yt-dlp version during installation and upgrade it deliberately after review.

Risk: Proxy configuration may be used for YouTube access, and proxy URLs with credentials can be visible to local same-user processes when passed to yt-dlp.

Mitigation: Prefer a local unauthenticated proxy endpoint and avoid putting usernames or passwords directly in HTTPS_PROXY.

Risk: Fetched metadata, transcripts, notes, and indexes remain on disk until the user deletes them.

Mitigation: Store notes in an appropriate local directory, review transcript sensitivity, and delete saved video-note folders when retention is no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/bonniegeng-max/skills/video-digest)
- [Video note template](references/note_template.md)
- [TED conversation example note](references/examples/example_ted_conversation.md)
- [vLLM Shorts example note](references/examples/example_vllm_shorts.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, files, guidance]

**Output Format:** [Markdown notes, text responses, shell commands, and local JSON/text files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Default note language is Chinese unless the user requests another language; generated notes include YouTube timestamps and source links when available.]

## Skill Version(s):

1.1.5 (source: server release metadata; artifact frontmatter reports 1.1.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
