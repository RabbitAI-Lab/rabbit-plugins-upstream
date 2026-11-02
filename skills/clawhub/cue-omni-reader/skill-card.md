## Description:

Cue Omni Reader converts documents, webpages, images, audio, and video into Markdown or clean text, with OCR, transcription, and visual understanding.

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and knowledge workers use Cue Omni Reader to extract structured text from documents, web pages, images, audio, and video for review or downstream workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review reports requests for API keys in chat and conflicting claims about whether local files are processed remotely.

Mitigation: Clarify the remote-processing data flow before using confidential files. Configure credentials through a protected local interface, rotate any key already shared in chat, limit authorized directories, and use reviewed, pinned Bridge versions.

## Reference(s):

- [Cue Omni Reader product page](https://cuecue.cn/hub/omni-reader)
- [Omni Reader parsing evaluation](https://mp.weixin.qq.com/s/SAPD3ajU2_D_EeRDiTHshQ)
- [Omni Reader parsing evaluation](https://mp.weixin.qq.com/s/S_-gcxDcaGMHbXjd5IepBg)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration instructions]

**Output Format:** [Markdown, clean text, or chunked text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Extracted content may include OCR text, transcripts, and video frame descriptions; supported detail mode is text.]

## Skill Version(s):

1.2.17 (source: server-resolved release metadata; artifact frontmatter states 1.8.9)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
