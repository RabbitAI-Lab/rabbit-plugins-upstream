## Description:

Supports Chinese batch creative duplicate review workflows by grouping duplicate or near-duplicate image and video assets, identifying content collisions, and producing retention, repair, regeneration, and audit recommendations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External users, content teams, ecommerce operators, advertising teams, and developers use this skill to plan and run batch creative duplicate checks for images, videos, filenames, task ledgers, creative variables, and deduplication thresholds. It also provides AI-HIVE command workflows for optional image/video generation, media upload, asynchronous task polling, downloading, deterministic video edits, and audit records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release is labeled as duplicate checking but also includes AI-HIVE media generation, upload, download, and editing workflows that may process local media, credentials, and billable remote tasks.

Mitigation: Install only when both duplicate review and AI-HIVE media workflow capabilities are intended; require explicit user confirmation before uploading media or submitting any generation request that may spend credits.

Risk: Sensitive, private, or unlicensed media could be uploaded to AI-HIVE during reference upload, image generation, video generation, or media upload steps.

Mitigation: Use only authorized media, avoid sensitive inputs unless remote upload is acceptable, and keep human review for copyright, trademark, privacy, and platform-compliance decisions.

Risk: API credentials may be exposed if real AI-HIVE keys are pasted into files, logs, screenshots, or shared task records.

Mitigation: Use environment variables or the supported local config flow, keep examples as placeholders, and review logs and generated files before sharing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/batch-creative-duplicate-check-ai-hive)
- [AI-HIVE chat](https://ai-hive.iclip.cn/chat)
- [AI-HIVE API endpoint](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with JSON files and inline shell command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include duplicate groups, near-match analysis, content-collision notes, risk ratings, repair advice, regeneration queues, API task records, and local file paths.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
