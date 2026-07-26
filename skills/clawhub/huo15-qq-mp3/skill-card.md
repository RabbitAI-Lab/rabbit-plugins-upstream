## Description: <br>
将QQ音乐下载的音频文件（OGG/FLAC/M4A/WAV/AAC 等）批量转换为通用 MP3 格式，保留元数据。支持单文件与整目录批处理，自动检测 ffmpeg 并选择最优编码参数。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zhaobod1](https://clawhub.ai/user/zhaobod1) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, engineers, and music-library users use this skill to guide an agent through converting supported QQ Music audio downloads to MP3 with ffmpeg while preserving metadata and supporting single-file or recursive directory workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A single-file ffmpeg command documented by the skill uses overwrite mode for the output MP3. <br>
Mitigation: Use the bundled script for skip-on-existing behavior, or have the agent confirm before overwriting an existing output file. <br>
Risk: The skill depends on ffmpeg with libmp3lame support, so conversion will fail if that binary or encoder is unavailable. <br>
Mitigation: Check `ffmpeg -version` before conversion and install an ffmpeg build that includes libmp3lame. <br>
Risk: QQ Music encrypted formats are outside the conversion workflow and require separate decryption before transcoding. <br>
Mitigation: Confirm inputs are supported audio formats before running conversion, and avoid treating encrypted files as directly convertible. <br>


## Reference(s): <br>
- [Skill homepage](https://github.com/zhaobod1/huo15-skills) <br>
- [qmc-decoder](https://github.com/Presburger/qmc-decoder) <br>
- [Unlock Music](https://git.unlock-music.dev/um/web) <br>
- [ffmpeg downloads](https://ffmpeg.org/download.html) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown with inline bash code blocks and command-line guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires ffmpeg with libmp3lame for actual audio conversion.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
