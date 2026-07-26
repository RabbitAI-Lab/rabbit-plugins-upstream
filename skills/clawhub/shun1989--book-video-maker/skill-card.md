## Description: <br>
根据书名生成 9:16 竖屏书单短视频，包含 AI 配图、中文语音朗读、中英字幕和 Ken Burns 镜头移动。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[shun1989](https://clawhub.ai/user/shun1989) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Content creators and social media operators use this skill to turn Chinese book titles into vertical book recommendation videos with generated script lines, images, narration, subtitles, and final MP4 output. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Book notes, prompts, and generated media content may be sent to ARK/Doubao and edge-tts services during the workflow. <br>
Mitigation: Avoid sensitive or proprietary book notes and prompts unless those services are approved for the content. <br>
Risk: The generator writes files to the selected output directory and invokes FFmpeg/ffprobe. <br>
Mitigation: Verify the output directory before running and review local dependency behavior before production use. <br>
Risk: Broad activation triggers and unconstrained inputs can start the workflow for unintended content. <br>
Mitigation: Tighten triggers and add URL or content-size validation before production deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/shun1989/skills/book-video-maker) <br>
- [README.md](artifact/README.md) <br>
- [SKILL.md](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, files] <br>
**Output Format:** [Markdown guidance with Python CLI examples; runtime artifacts include JSON script data, JPG images, MP3 narration, intermediate MP4 segments, and a final 1080x1920 MP4.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires ARK_API_KEY, FFmpeg/ffprobe, edge-tts, requests, and the documented font paths.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release, target metadata, frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
