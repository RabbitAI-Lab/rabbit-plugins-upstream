## Description:

Tingwu ASR helps agents transcribe audio and video with Alibaba Cloud Tingwu and produce FunASR-compatible Markdown transcripts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cat-xierluo](https://clawhub.ai/user/cat-xierluo)

### License/Terms of Use:

MIT

## Use Case:

Developers, legal professionals, and agent users use this skill to convert local or URL-sourced audio and video into cloud-generated transcripts when offline transcription is unavailable or lower accuracy. It supports long media, batch transcription, speaker separation, archiving, and Markdown output for follow-on summarization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores Alibaba Tingwu account credentials and reusable session cookies locally.

Mitigation: Use a dedicated account where possible, keep config/.env and config/cookies.json private, and avoid passing cookies on the command line.

Risk: Selected recordings are uploaded to Alibaba Cloud Tingwu for transcription.

Mitigation: Confirm cloud processing is approved before using sensitive, confidential, or regulated recordings.

Risk: URL transcription can download arbitrary media before upload.

Mitigation: Avoid untrusted URLs and do not run arbitrary URL transcription from machines with access to private networks.

Risk: Scheduled check-ins can repeatedly use the authenticated account.

Mitigation: Enable scheduled check-ins only when the account owner explicitly wants automated quota collection.

## Reference(s):

- [Tingwu ASR ClawHub release](https://clawhub.ai/cat-xierluo/skills/tingwu-asr)
- [Skill homepage](https://github.com/cat-xierluo/legal-skills)
- [Tingwu web app](https://tingwu.aliyun.com/home)
- [Internal REST API reference](references/api-capture.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown transcripts, status text, JSON task metadata, and shell command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include transcript Markdown, archive paths, pending task records, raw API JSON when requested, and optional slide image references for video.]

## Skill Version(s):

0.4.2 (source: frontmatter, changelog, release metadata; released 2026-09-09)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
