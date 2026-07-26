## Description: <br>
把一条社媒视频快速变成多个平台可发的尺寸版本——在 9:16、1:1、4:5、16:9 之间选择 crop / pad / scale 最佳策略，保护人脸、产品与字幕安全区，输出各平台可直接使用的适配方案。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[leooooooow](https://clawhub.ai/user/leooooooow) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External creators, marketers, and agents use this skill to turn one source video into platform-ready social video variants. It helps choose crop, pad, or proportional scale strategies while preserving faces, products, subtitles, safe zones, and delivery notes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may guide an agent to inspect and process user-provided video files. <br>
Mitigation: Use approved source videos only, avoid unnecessary sensitive content, and review generated output paths before processing. <br>
Risk: Suggested ffmpeg commands can create resized outputs that crop, pad, compress, or overwrite files if used without review. <br>
Mitigation: Preview command parameters, write to new output filenames, and inspect each rendered variant before publishing. <br>
Risk: Social platform dimensions, duration limits, file-size limits, and ad placement rules can change. <br>
Mitigation: Verify current platform or ad-dashboard specifications before final delivery or publication. <br>


## Reference(s): <br>
- [Output Template](references/output-template.md) <br>
- [Platform Spec Sheet](references/platform-spec-sheet.md) <br>
- [Crop / Pad / Scale Guide](references/crop-pad-scale-guide.md) <br>
- [Resize Checklist](assets/resize-checklist.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown with tables, per-version resize recommendations, risk notes, and optional ffmpeg command blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include platform dimensions, crop or pad strategy, safe-zone checks, subtitle handling, compression guidance, and publication risks.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
