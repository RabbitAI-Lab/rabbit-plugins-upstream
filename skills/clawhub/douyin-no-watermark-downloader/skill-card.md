## Description:

下载抖音视频到本地（无水印），以 mp4 格式默认保存在桌面目录。

This skill is ready for commercial/non-commercial use.

## Publisher:

[lvleiai123](https://clawhub.ai/user/lvleiai123)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to run a local Python downloader for public Douyin share links and save the resulting no-watermark MP4 file to the desktop.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The downloader sends the user's Douyin link to lvhomeproxy2.dpdns.org for parsing.

Mitigation: Install and use only if users are comfortable sending provided Douyin links to that third-party parsing service.

Risk: The script downloads a video URL returned by the parsing service.

Mitigation: Prefer a version that documents its network services, restricts accepted domains, and validates returned download URLs before downloading.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/lvleiai123/skills/douyin-no-watermark-downloader)

## Skill Output:

**Output Type(s):** [guidance, shell commands, files]

**Output Format:** [Markdown guidance with inline shell commands and local MP4 file output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Downloads MP4 files to the user's Desktop by default and prints success or failure status in the terminal.]

## Skill Version(s):

1.0.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
