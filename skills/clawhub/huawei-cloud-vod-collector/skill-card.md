## Description:

Captures developer feedback about Huawei Cloud issues and turns it into prioritized issue reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use it to record errors, corrections, and suggestions about Huawei Cloud tools or services, then organize that feedback into GitCode issue reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Feedback delivery may expose sensitive diagnostics or private reasoning in the target repository.

Mitigation: Keep hooks and delivery disabled until the repository, its visibility, and report contents are approved; remove private reasoning and check reports for secrets.

Risk: The downloaded telemetry implementation and its handling of reports are unverified.

Mitigation: Set SKILL_QUALITY_REPORT=0 unless the downloaded implementation has been reviewed.

Risk: GitCode credentials may appear in request URLs and related logs.

Mitigation: Use narrowly scoped, short-lived credentials and a trusted egress path; require TLS before enabling email notifications.

## Reference(s):

- [CLI installation guide](references/cli-installation-guide.md)
- [Deduplication and notifications](references/dedup-and-notify.md)
- [Hooks setup](references/hooks-setup.md)
- [OpenClaw integration](references/openclaw-integration.md)
- [Verification method](references/verification-method.md)
- [Huawei Cloud CLI documentation](https://support.huaweicloud.com/cli/index.html)
- [AtomGit-GO login project](https://gitcode.com/weixin_45218422/AtomGit-GO)

## Skill Output:

**Output Type(s):** [Markdown, Text, Shell commands, Configuration instructions]

**Output Format:** [Structured Markdown feedback files and GitCode issue reports, with shell commands and configuration guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

1.0.8 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
