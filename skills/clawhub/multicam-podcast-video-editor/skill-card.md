## Description:

Edit podcasts, interviews, and multi-camera recordings (播客): waveform audio sync, active-speaker camera switching, split-screen layouts, podcast clips, and Descript/Opus Clip style transcript editing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[brajendrak00068](https://clawhub.ai/user/brajendrak00068)

### License/Terms of Use:

MIT-0

## Use Case:

Podcast creators, interview editors, and production teams can synchronize multi-camera footage, switch angles around active speakers, and assemble highlight openings and podcast clips.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan reports incomplete coverage because a local reference could not be resolved.

Mitigation: Review the unresolved reference before relying on the scan's benign verdict.

Risk: Using the editing service requires an API key, and submitted media may contain private material.

Mitigation: Keep LEVEA_API_KEY in the tool's secret configuration and submit only footage you are authorized to share with Levea.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/brajendrak00068/skills/multicam-podcast-video-editor)
- [Levea editing service](https://livecore.ai/?openclaw=1&utm_source=clawhub&utm_medium=skill&utm_campaign=multicam-podcast-video-editor)
- [Levea API](https://api.livecore.ai)

## Skill Output:

**Output Type(s):** [Guidance, API Calls, Video]

**Output Format:** [Structured edit status and project details, with an MP4 export URL when available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Editing requires a Levea account and API key; the exported video URL is returned after export.]

## Skill Version(s):

1.0.6 (source: frontmatter, ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
