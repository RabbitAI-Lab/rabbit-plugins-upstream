## Description:

Captures Huawei Cloud developer pain points, converts them into structured Voice of Developer feedback records, and can deliver selected reports as GitCode issues.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to capture Huawei Cloud tool or service errors, user rejection signals, and problem reports, then sanitize, enrich, and route selected feedback to GitCode for follow-up.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic feedback capture and local .vod records may include sensitive conversation context or file-derived content.

Mitigation: Configure or restrict hooks, avoid @filepath inputs for sensitive files, keep capture limits enabled, and run the sanitizer before retaining or delivering feedback.

Risk: GitCode delivery can submit feedback content to an external repository.

Mitigation: Verify the configured repo_url, review and sanitize each feedback record before delivery, and deliver only records that are appropriate to share externally.

Risk: The AtomGit-GO login flow can install helper software and store an access token locally in plaintext.

Mitigation: Verify the AtomGit-GO source before installation, restrict auth.toml permissions, use a dedicated AtomGit home when appropriate, and delete the token file when access is no longer needed.

Risk: Hook triggers on tool errors or rejection keywords may capture unintended events.

Mitigation: Review hook definitions and keyword lists before enabling the skill, and disable or narrow triggers that do not match the intended deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-vod-collector)
- [Publisher profile](https://clawhub.ai/user/huaweiclouddev)
- [Hooks setup guide](references/hooks-setup.md)
- [OpenClaw integration guide](references/openclaw-integration.md)
- [Acceptance criteria](references/acceptance-criteria.md)
- [VoD feedback record template](assets/VOD_FEEDBACKS.md)
- [GitCode issue template](assets/VOD_ISSUE.md)
- [AtomGit-GO source repository](https://gitcode.com/weixin_45218422/AtomGit-GO)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown feedback records, JSON command results, shell commands, and GitCode issue body text.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates local .vod feedback files and can submit selected sanitized content to a configured GitCode repository.]

## Skill Version(s):

1.0.1 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
