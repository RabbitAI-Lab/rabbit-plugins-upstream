## Description: <br>
Helps agents burn SRT subtitles into video, soft-mux subtitle tracks, or create a final localized MP4 by mixing a dub track with the original audio bed in one ffmpeg pass. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[hanshaoyuyehanshaoyuye](https://clawhub.ai/user/hanshaoyuyehanshaoyuye) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and content localization agents use this skill to prepare upload-ready videos with burned subtitles, soft subtitle tracks, or mixed dub audio. It is most relevant when a local video, SRT file, and optional dub track need to be composed with ffmpeg. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can auto-download and run a third-party ffmpeg binary without mandatory checksum verification. <br>
Mitigation: Prefer a trusted local ffmpeg with libass from a package manager, or set a known-good EVERMEET_FFMPEG_SHA256 before using the auto-download fallback. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/hanshaoyuyehanshaoyuye/skills/wjs-burning-subtitles) <br>
- [Evermeet ffmpeg static build download](https://evermeet.cx/ffmpeg/getrelease/zip) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, guidance, code, configuration] <br>
**Output Format:** [Markdown guidance with bash command examples and a Python helper script] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The helper script writes MP4 outputs when run with local video, subtitle, and optional dub inputs.] <br>

## Skill Version(s): <br>
8.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
