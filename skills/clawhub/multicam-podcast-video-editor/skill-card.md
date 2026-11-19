## Description:

Edit podcasts, interviews, and multi-camera recordings (播客): waveform audio sync, active-speaker camera switching, split-screen layouts, podcast clips, and Descript/Opus Clip style transcript editing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[brajendrak00068](https://clawhub.ai/user/brajendrak00068)

### License/Terms of Use:

MIT

## Use Case:

Podcast creators, editors, and production teams use the skill to synchronize camera and audio tracks, select camera angles around active speakers, and assemble podcast episodes or clips.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review reports no findings but has medium confidence because a local reference could not be resolved, so the review evidence is incomplete.

Mitigation: Review the skill and its referenced behavior and decide whether the unresolved reference matters before installing.

Risk: The editing service requires an API key, and source media is supplied through public URLs.

Mitigation: Keep the API key in the plugin configuration or LEVEA_API_KEY environment setting, and use media URLs that are appropriate to share with the service.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/brajendrak00068/skills/multicam-podcast-video-editor)
- [Levea editing service](https://livecore.ai/)
- [Levea API](https://api.livecore.ai)

## Skill Output:

**Output Type(s):** [Video (MP4 download URL), Project metadata, Status and verification reports]

**Output Format:** [Structured tool responses and rendered video media]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The service returns a project ID; an MP4 URL is available after export.]

## Skill Version(s):

1.0.7 (source: SKILL.md frontmatter; server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
