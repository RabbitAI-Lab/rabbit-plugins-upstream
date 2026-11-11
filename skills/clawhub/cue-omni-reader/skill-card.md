## Description:

Cue Omni Reader parses supported local files and URLs into Markdown or clean text, including OCR, audio transcription, and video frame understanding.

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use Cue Omni Reader to convert supported documents, scans, images, audio, video, webpages, and archives into structured Markdown or clean text for review and downstream workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence rates this release suspicious because of reported credential-handling and privacy contradictions.

Mitigation: Review the security guidance before installation; do not share API keys in chat, and confirm data handling for the chosen setup.

Risk: The security evidence reports unpinned package commands.

Mitigation: Review package commands and pin versions before running them.

Risk: The security evidence reports capabilities that may not match the stated document-parsing purpose, and notes that scanner analysis is partial.

Mitigation: Inspect the skill and its referenced components before enabling it; treat the scan as incomplete because some local references were unresolved.

## Reference(s):

- [Cue Omni Reader product page](https://cuecue.cn/hub/omni-reader)
- [Parsing evaluation article](https://mp.weixin.qq.com/s/SAPD3ajU2_D_EeRDiTHshQ)
- [Parsing evaluation article](https://mp.weixin.qq.com/s/S_-gcxDcaGMHbXjd5IepBg)

## Skill Output:

**Output Type(s):** [Markdown, Text]

**Output Format:** [Markdown or clean text; optional hypertext or chunked results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One source per request; maximum 256 MiB per file.]

## Skill Version(s):

1.2.19 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
