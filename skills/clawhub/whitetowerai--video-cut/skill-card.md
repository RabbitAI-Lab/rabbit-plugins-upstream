## Description:

End-to-end turn an unedited long-form talking-head, vlog, or podcast video into a compact first cut by downloading or using local media, transcribing, diagnosing weak sections, planning cuts, rendering with ffmpeg, and self-checking the result.

This skill is ready for commercial/non-commercial use.

## Publisher:

[whitetowerai](https://clawhub.ai/user/whitetowerai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and video-production agents use this skill to turn raw talking-head, vlog, podcast, or YouTube-style source footage into a tighter rough cut with an auditable JSON edit plan, rendered video, and self-check report.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can download or process user-provided video and create local intermediates, rendered video, and reports.

Mitigation: Run it in a dedicated project folder and avoid private media or account cookies unless those local media tools are trusted for that content.

Risk: The skill depends on a separate /video-understand prerequisite that supplies validated media, transcript, analysis, and timeline evidence.

Mitigation: Confirm /video-understand is installed and trusted before processing media; stop if the prerequisite is unavailable.

Risk: Editorial keep/drop decisions can omit useful context or create misleading pacing if the edit plan is not reviewed.

Mitigation: Review the JSON edit plan, inspect boundaries, and run the documented re-transcription, frame, silence, and A/V checks before treating the cut as complete.

## Reference(s):

- [Video Cut on ClawHub](https://clawhub.ai/whitetowerai/skills/video-cut)
- [edit_coarse.json format spec](artifact/reference/edit_coarse.schema.md)
- [Pitfalls and fixes](artifact/reference/pitfalls.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with JSON edit plans, shell commands, generated reports, and rendered video files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local work/ intermediates, timeline/edit JSON, review artifacts, a rendered first_cut.mp4, and a first_cut_report.md when run in the documented workflow.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
