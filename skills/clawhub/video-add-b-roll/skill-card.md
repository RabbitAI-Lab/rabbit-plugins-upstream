## Description:

Use when a talking-head, interview, documentary, or explanatory video needs deliberate transcript-timed visual cutaways from local media or Pexels.

This skill is ready for commercial/non-commercial use.

## Publisher:

[whitetowerai](https://clawhub.ai/user/whitetowerai)

### License/Terms of Use:

MIT-0

## Use Case:

Video editors and agents use this skill to plan, acquire, review, and verify transcript-timed B-roll for talking-head, interview, documentary, or explanatory videos. It supports local media and Pexels media while preserving review gates and provenance records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can download Pexels media or import local video into a project.

Mitigation: Use media with clear rights, keep provenance records, and provide the Pexels API key only through the local .env file.

Risk: The workflow runs ffmpeg and ffprobe against project media.

Mitigation: Keep ffmpeg patched and process media from trusted, project-local sources.

Risk: The workflow updates files under the target video project.

Mitigation: Run it only in the intended project and complete the review gates before applying final B-roll outputs.

## Reference(s):

- [B-Roll Rules](reference/broll-rules.md)
- [video-add-b-roll release page](https://clawhub.ai/whitetowerai/skills/video-add-b-roll)
- [WhiteTowerAI publisher profile](https://clawhub.ai/user/whitetowerai)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON plans, review artifacts, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces project-local B-roll plans, candidate analysis, review pages, normalized video clips, summaries, and verification evidence.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
