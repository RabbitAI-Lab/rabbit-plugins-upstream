## Description: <br>
Convert videos for compatibility and uploads by selecting the right container, codec, bitrate, and verification path for each destination. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[leooooooow](https://clawhub.ai/user/leooooooow) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, marketers, and content teams use this skill to prepare video files for marketplaces, social platforms, ad managers, CMS uploads, and other destination-specific ingest requirements. It helps diagnose rejected uploads, reduce file size, choose FFmpeg conversion settings, and deliver a reproducible spec sheet. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may lead an agent to propose or run FFmpeg commands against private or unreleased video files. <br>
Mitigation: Review filenames, output paths, command arguments, and media sensitivity before execution. <br>
Risk: Upload requirements and platform limits can change after the bundled baseline references were written. <br>
Mitigation: Confirm the destination's current published requirements and use draft test uploads when available. <br>


## Reference(s): <br>
- [Conversion Delivery Template](references/output-template.md) <br>
- [Baseline Upload Requirements by Destination Type](references/platform-upload-specs.md) <br>
- [ffmpeg Recipes: Probe, Encode Ladders, Size Math](references/ffmpeg-recipes.md) <br>
- [Troubleshooting Rejected or Broken Uploads](references/troubleshooting-guide.md) <br>
- [Conversion - Pre-Delivery Checklist](assets/conversion-checklist.md) <br>
- [ClawHub skill page](https://clawhub.ai/leooooooow/skills/upload-video-converter) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands] <br>
**Output Format:** [Markdown with FFmpeg command examples and per-destination spec tables] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include verification checks, quality tradeoffs, and escalation notes for files that need editing or resizing before upload.] <br>

## Skill Version(s): <br>
1.1.0 (source: server evidence release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
