## Description:

解析文档、图片、扫描件、音视频和网页，并将内容整理为 Markdown 或纯文本。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agent users can use it to extract and organize content from files or URLs, including OCR and audio or video transcription. It returns readable text or Markdown for review and further work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill's privacy assurances conflict with its remote processing workflow, so private-file handling and retention are unclear.

Mitigation: Before using private files, confirm what Cue receives and retains; avoid sending sensitive files until that is clear.

Risk: The instructions direct users to paste API keys into chat, which can expose credentials.

Mitigation: Configure credentials outside chat and rotate any key already shared there. Restrict allowed directories and use reviewed, exact package versions for installation and maintenance.

## Reference(s):

- [Cue Omni Reader product page](https://cuecue.cn/hub/omni-reader)
- [Cue API key setup](https://cuecue.cn/api-key?src=clawhub-omni-reader)
- [Omni Reader evaluation article](https://mp.weixin.qq.com/s/SAPD3ajU2_D_EeRDiTHshQ)
- [Omni Reader evaluation article](https://mp.weixin.qq.com/s/S_-gcxDcaGMHbXjd5IepBg)

## Skill Output:

**Output Type(s):** [Markdown, Text, Configuration instructions, Shell commands]

**Output Format:** [Extracted content as Markdown or clean text; setup guidance may include JSON configuration and shell commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts a file or URL; long-running parses may return an operation that must be checked for completion.]

## Skill Version(s):

1.2.16 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
