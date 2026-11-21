## Description:

video2text-ai helps agents convert a single local video file or public video URL into a cleaned transcript, then use an optional prompt to generate summaries, social media copy, highlights, meeting notes, course breakdowns, recaps, interview notes, translations, and related text outputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, content teams, and agents use this command skill to turn one public video URL or local video file into a cleaned transcript, then apply an optional prompt to produce summaries, rewrites, highlights, meeting notes, translations, or other reusable text derivatives.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive, confidential, or regulated video content could be uploaded to a third-party transcription service.

Mitigation: Use only videos you are allowed to send to GuaiKei and its storage provider; avoid sensitive meetings or regulated data unless the service terms and retention controls are approved.

Risk: User-supplied URLs could expose internal, localhost, metadata-service, or private-network resources.

Mitigation: Do not provide private-network URLs; require strict public-domain and IP filtering before production deployment.

Risk: Upload and network behavior is broader than the skill's user-facing description may imply.

Mitigation: Review network destinations before installing and require upload-destination allowlisting, explicit upload consent, size limits, and verifiable retention documentation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/scripts)
- [GuaiKei video text service](https://www.guaikei.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Plain text or prompt-directed structured text on stdout, with diagnostics on stderr]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GUAIKEI_API_TOKEN and processes one video source or one prior task ID per command invocation.]

## Skill Version(s):

1.0.0 (source: server release metadata and package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
