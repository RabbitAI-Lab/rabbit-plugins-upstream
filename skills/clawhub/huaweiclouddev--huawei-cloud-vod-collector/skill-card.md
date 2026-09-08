## Description:

Captures Huawei Cloud developer feedback from errors, user rejections, or direct reports, then turns it into structured Voice of Developer records and GitCode issues.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and product or support engineers use this skill to capture poor Huawei Cloud tool and service experiences during agent sessions, enrich them into structured feedback, and submit actionable issues to GitCode.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic hooks can capture tool failures, rejection text, reports, and conversation or environment context more broadly than a user may expect.

Mitigation: Review or disable broad hooks before deployment, limit captured context to what is needed, and require user review before preserving or submitting feedback.

Risk: Feedback records may retain sensitive conversation, error, or environment details locally before delivery.

Mitigation: Run the sanitizer, remove thinking or full-dialog capture where not needed, and require a final sanitized preview before submission.

Risk: Delivery uses AtomGit-GO credentials and remote GitCode issue submission.

Mitigation: Use only approved credentials, keep the token file protected, and confirm the configured GitCode repository before submitting issues.

Risk: The installer can clone and build the AtomGit-GO helper from an external source.

Mitigation: Avoid running the installer unless the helper source is pinned and verified, or provide a reviewed local helper build.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-vod-collector)
- [Hooks setup guide](references/hooks-setup.md)
- [OpenClaw integration guide](references/openclaw-integration.md)
- [Acceptance criteria](references/acceptance-criteria.md)
- [VoD feedback record template](assets/VOD_FEEDBACKS.md)
- [GitCode issue template](assets/VOD_ISSUE.md)
- [AtomGit-GO](https://gitcode.com/weixin_45218422/AtomGit-GO)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown feedback records and GitCode issue content, with shell commands and JSON status responses from helper scripts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Stores feedback under .vod/feedbacks and may submit issues to the configured GitCode repository.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
