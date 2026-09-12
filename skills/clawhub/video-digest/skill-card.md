## Description:

视频深读 helps an agent turn YouTube videos into concise structured notes with timestamps, fact/opinion separation, follow-up retrieval support, and content-idea prompts, using scripts only for transcript fetching and the running AI for note synthesis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bonniegeng-max](https://clawhub.ai/user/bonniegeng-max)

### License/Terms of Use:

MIT

## Use Case:

External users and agent operators use this skill to summarize YouTube videos into structured reading notes, scan batches of videos, retrieve timestamped transcript context for follow-up questions, and generate non-draft content angles. It is most directly aimed at AI, technology, interview, TED, lecture, and short-form educational videos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: YouTube requests and locally stored transcripts or notes may reveal viewing and research interests.

Mitigation: Use an output directory that is appropriate for agent access, and remove local archives when they are no longer needed.

Risk: Credential-bearing HTTPS_PROXY values can create proxy credential exposure risk when passed to command-line tools.

Mitigation: Prefer a local credential-free proxy or direct connection, and avoid proxy environment values that embed usernames or passwords.

Risk: The skill depends on yt-dlp from the package ecosystem.

Mitigation: Pin and review yt-dlp versions for controlled deployments, and update deliberately when YouTube extraction behavior changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/bonniegeng-max/skills/video-digest)
- [Publisher profile](https://clawhub.ai/user/bonniegeng-max)
- [Note template](references/note_template.md)
- [TED conversation example](references/examples/example_ted_conversation.md)
- [vLLM Shorts example](references/examples/example_vllm_shorts.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown notes with timestamped sections, local transcript and metadata files, brief batch summary cards, and retrieval-backed answers.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs can be saved under the configured video-notes directory and indexed for later retrieval; note language defaults to Chinese unless the user requests another language.]

## Skill Version(s):

1.1.4 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
