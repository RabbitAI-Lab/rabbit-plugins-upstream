## Description:

Omni Reader parses URLs and uploaded files, including documents, images, scanned pages, audio, video, web pages, and archives, into Markdown or clean text with OCR, transcription, and visual-understanding support.

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and end users use this skill to convert local files or reachable URLs into agent-readable Markdown, transcripts, outlines, and extracted tables. It is suited to document processing, OCR, audio/video transcription, web capture, and follow-on summarization or format conversion workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence rates the release suspicious because privacy and credential disclosures may conflict with remote-service behavior.

Mitigation: Install only when selected files, URLs, and parsed content are acceptable to send to Cue's service, and review data-sensitivity requirements before use.

Risk: Local-file parsing can expose more filesystem content than intended if allowed roots are broad.

Mitigation: Set OMNI_ALLOWED_ROOTS to the narrowest required directories and avoid sensitive directories.

Risk: API credentials are required for service access.

Mitigation: Use a revocable CUE_API_KEY, store it locally, and rotate it if exposed.

Risk: Referral and payment prompts can steer account behavior.

Mitigation: Treat those prompts as vendor account guidance rather than neutral assistant advice.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/panting09266-ai/skills/cue-omni-reader)
- [Cue Omni Reader Product Page](https://cuecue.cn/hub/omni-reader)
- [Cue API Key Documentation](https://cuecue.cn/hub/api-key)
- [Cue MCP Catalog](https://cuecue.cn/api/mcp-catalog)
- [Omni Reader Evaluation Article 1](https://mp.weixin.qq.com/s/SAPD3ajU2_D_EeRDiTHshQ)
- [Omni Reader Evaluation Article 2](https://mp.weixin.qq.com/s/S_-gcxDcaGMHbXjd5IepBg)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, shell commands, guidance, files]

**Output Format:** [Markdown or clean text, with JSON status data and optional saved result files when using the local bridge.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return asynchronous operation status for large parses; remote output is inline on completion, while local bridge output can be paged, saved, or discarded.]

## Skill Version(s):

1.2.12 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
