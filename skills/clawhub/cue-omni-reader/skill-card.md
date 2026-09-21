## Description:

Omni Reader helps agents parse URLs and files, including PDFs, Office documents, images, scans, audio, video, web pages, archives, text, and code, into Markdown or clean text.

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agent operators use this skill to convert documents, media, web pages, and local or remote file sources into readable Markdown for summarization, extraction, OCR, transcription, and downstream analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The integration uses a Cue API key and can access local files through the Bridge.

Mitigation: Install only after trusting Cue and the npm package publisher, never paste or print the API key in chat, and set OMNI_ALLOWED_ROOTS to the smallest specific folders needed.

Risk: Privacy behavior is under-disclosed and may involve Cue services for some content despite privacy wording.

Mitigation: Avoid submitting sensitive files unless the user accepts that processing may involve Cue services, and prefer the documented no-store behavior where available.

Risk: Install and update commands can fetch npm packages dynamically.

Mitigation: Use pinned package versions for normal use and avoid @latest commands unless deliberately updating after review.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/panting09266-ai/skills/cue-omni-reader)
- [Omni Reader web experience](https://cuecue.cn/hub/omni-reader)
- [Cue API key documentation](https://cuecue.cn/hub/api-key)
- [Cue MCP catalog](https://cuecue.cn/api/mcp-catalog)
- [Official parsing evaluation article](https://mp.weixin.qq.com/s/SAPD3ajU2_D_EeRDiTHshQ)
- [Official parsing evaluation article](https://mp.weixin.qq.com/s/S_-gcxDcaGMHbXjd5IepBg)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown and clean text, with JSON MCP responses and inline shell or configuration snippets when setup or polling is needed.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Large parses may return an operation for polling, and local Bridge results may be read, saved, or discarded through the documented tools.]

## Skill Version(s):

1.2.13 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
