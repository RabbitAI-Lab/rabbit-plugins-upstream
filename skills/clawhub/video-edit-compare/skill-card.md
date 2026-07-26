## Description: <br>
Use when a completed cut-as-code delivery needs a strict side-by-side review against its original source, including cuts, varispeed, color grade, and graphics. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[whitetowerai](https://clawhub.ai/user/whitetowerai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and video-production agents use this skill after a final render exists to create a strict original-versus-final comparison on the original source clock. It helps review cuts, dropped ranges, varispeed, color grade, graphics, and continuous original audio against the delivered video. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The rendering script runs ffmpeg and ffprobe on user-named media files. <br>
Mitigation: Run it only in projects where processing the selected videos with local media tooling is acceptable. <br>
Risk: The requested output video path is overwritten by ffmpeg's -y behavior, and parent directories may be created. <br>
Mitigation: Review the output path before execution and keep important review artifacts outside paths selected for regeneration. <br>


## Reference(s): <br>
- [Video Edit Compare on ClawHub](https://clawhub.ai/whitetowerai/skills/video-edit-compare) <br>


## Skill Output: <br>
**Output Type(s):** [Files, Markdown, JSON, Shell commands] <br>
**Output Format:** [MP4 comparison video, JSON compare plan and filtergraph cache files, and Markdown verification summary] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires ffmpeg, ffprobe, Python, and Pillow; --filter-only writes the plan and inspectable cache files without rendering video.] <br>

## Skill Version(s): <br>
1.0.1 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
