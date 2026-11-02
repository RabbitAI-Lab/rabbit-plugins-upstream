## Description:

Transcribe audio and video for agents by Speech is Cheap. Fast, high-quality, and cost-effective ($0.06 - $0.12/hr). Use an API key or x402 USDC.

This skill is ready for commercial/non-commercial use.

## Publisher:

[speechischeap](https://clawhub.ai/user/speechischeap)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to transcribe audio or video from a URL or local file, retrieve asynchronous job results, and optionally request speaker labels, word timestamps, or sound labels.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Transcription sends the selected media or media URL, options, and any webhook URL to Speech is Cheap; retention and refund promises were not independently verified.

Mitigation: Send only caller-approved media, consider --private for sensitive recordings, and review the service's privacy and retention terms.

Risk: Wallet mode can authorize USDC payments and uses local purchase recovery state.

Mitigation: Use a trusted signer with approval controls, approve a per-purchase --max-usd ceiling, and keep recovery state private.

Risk: Dependency code and live payment behavior were not tested.

Mitigation: Review dependencies and verify payment behavior before relying on wallet mode.

## Reference(s):

- [Speech is Cheap privacy policy](https://speechischeap.com/privacy/)
- [Speech is Cheap security](https://speechischeap.com/company/security/)
- [x402 errors and refunds](https://docs.speechischeap.com/errors/)
- [x402 payments and refunds](https://docs.speechischeap.com/x402-v2/payments/)
- [x402 webhooks](https://docs.speechischeap.com/x402-v2/webhooks/)
- [Maintenance repository listed by the publisher](https://github.com/speechischeap/clawhub-asr)

## Skill Output:

**Output Type(s):** [Text, JSON, SRT subtitles, VTT/WebVTT subtitles, Shell commands, Guidance]

**Output Format:** [Transcripts as JSON, SRT, or VTT/WebVTT; job status as JSON or text; shell commands and configuration guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional speaker labels, word timestamps, sound labels, and asynchronous webhook delivery.]

## Skill Version(s):

1.5.0 (source: release evidence, CHANGELOG.md, manifest.json; released 2026-11-01)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
