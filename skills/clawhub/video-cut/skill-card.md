## Description: <br>
Video Cut helps an agent turn an unedited long-form talking-head, vlog, or podcast video into a compact first cut by planning cuts, rendering with ffmpeg, and self-checking the edited result. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[whitetowerai](https://clawhub.ai/user/whitetowerai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and content-focused agent users use this skill to produce a rough first cut from a raw local or YouTube video. It guides the agent through transcription, editorial keep/drop planning, frame-safe rendering, and post-render checks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill downloads or reads user-supplied video and processes it with local media tools. <br>
Mitigation: Use trusted media sources, confirm local tool availability, and avoid running the workflow on private media unless local processing and storage are acceptable. <br>
Risk: The workflow creates or overwrites files such as work/source.mp4, work/audio16k.wav, first_cut.mp4, and reports. <br>
Mitigation: Review output paths and run the skill in a dedicated project directory before processing large or important media. <br>
Risk: Editorial cut decisions can remove or retain the wrong content if the transcript, analysis, or keep/drop plan is not reviewed. <br>
Mitigation: Inspect the generated plan, boundary review, self-check transcript, and frame checks before treating the rendered video as final. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/whitetowerai/skills/video-cut) <br>
- [Edit Plan Schema](reference/edit_coarse.schema.md) <br>
- [Video Editing Pitfalls](reference/pitfalls.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON edit plans and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces local project files and edited media outputs such as cut plans, timeline data, review reports, and first-cut video files.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
