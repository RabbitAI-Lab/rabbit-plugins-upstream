## Description:

AI video editor and autonomous MCP video editing agent (37 tools, 280+ animated caption templates, 189+ actions) — replaces raw ffmpeg/MoviePy scripts for creative edits. Use when the user wants to edit a video, cut silences, generate viral clips for TikTok, Reels, or YouTube Shorts, reframe 16:9 to 9:16 vertical, add word-by-word captions or subtitles, edit multicam podcasts, insert B-roll, motion graphics, VFX, chroma key, color grading, voiceover, music, or export MP4.

This skill is ready for commercial/non-commercial use.

## Publisher:

[brajendrak00068](https://clawhub.ai/user/brajendrak00068)

### License/Terms of Use:

MIT-0

## Use Case:

Video creators and editors use this skill to turn a natural-language brief into edited video projects, including cuts, captions, reframing, graphics, effects, audio work, and MP4 exports. It connects to the Levea editing service and requires a Levea account and API key.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review was partial because four local Markdown references could not be resolved, so their context was not assessed.

Mitigation: Review the referenced material before deployment and use the skill with that incomplete scan context in mind.

Risk: The skill sends editing work to a cloud service and requires a Levea API key.

Mitigation: Configure the API key through the tool's secret or configuration mechanism and avoid placing it in prompts or shared logs.

## Reference(s):

- [ClawHub release](https://clawhub.ai/brajendrak00068/skills/levea-ai-video-editor)
- [Levea service and account setup](https://livecore.ai/?openclaw=1&utm_source=clawhub&utm_medium=skill&utm_campaign=levea-ai-video-editor)

## Skill Output:

**Output Type(s):** [Video timeline edits, Rendered MP4 video, Verification report]

**Output Format:** [Video project updates with a verification report and, after export, an MP4 download URL]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The service may return a project ID and asynchronous render job details.]

## Skill Version(s):

1.0.39 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
