## Description:

Captures poor Huawei Cloud developer experiences, turns them into structured Voice of Developer feedback, sanitizes and deduplicates records, and can deliver them as GitCode issues.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to capture errors, rejected responses, and reported issues from Huawei Cloud workflows, then prepare sanitized feedback files or GitCode issues for product follow-up.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic feedback capture can collect conversation context, error details, and environment information beyond what the user intended to share.

Mitigation: Review generated files in .vod/feedbacks/ before delivery, redact unnecessary conversation content, and use the provided sanitizer before publishing.

Risk: Quality telemetry is enabled unless opted out.

Mitigation: Set SKILL_QUALITY_REPORT=0 before running skill commands when telemetry should be disabled.

Risk: GitCode delivery can publish feedback externally to the configured repository.

Mitigation: Verify delivery.channels.gitcode.repo_url in assets/config.yaml and confirm the issue body before delivery.

Risk: The AtomGit-GO login flow stores tokens in the user's home directory.

Mitigation: Use the login flow only when trusted, protect or remove the auth.toml token file, and prefer already configured trusted delivery tooling when available.

## Reference(s):

- [Skill page](https://clawhub.ai/huaweicloudskill/skills/huawei-cloud-vod-collector)
- [CLI Installation Guide](references/cli-installation-guide.md)
- [Hook Configuration and Deployment Guide](references/hooks-setup.md)
- [OpenClaw Integration](references/openclaw-integration.md)
- [IAM Policies](references/iam-policies.md)
- [Verification Method](references/verification-method.md)
- [Acceptance Criteria](references/acceptance-criteria.md)
- [Huawei Cloud KooCLI documentation](https://support.huaweicloud.com/cli/index.html)
- [AtomGit-GO](https://gitcode.com/weixin_45218422/AtomGit-GO)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Configuration, API calls, Guidance]

**Output Format:** [Markdown feedback records and GitCode issue content with supporting shell commands and JSON status responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Feedback files are stored under .vod/feedbacks/ and delivery uses the configured GitCode repository.]

## Skill Version(s):

1.0.6 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
