## Description:

Audits PikPak shares for known expired, near-expiry, and zero-visit conditions and provides guidance for separately authorized manual management without creating or revoking shares.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pipiguai87-alt](https://clawhub.ai/user/pipiguai87-alt)

### License/Terms of Use:

MIT-0

## Use Case:

PikPak account holders and their authorized assistants use this skill to review share expiry and activity, then decide whether any manual share changes are warranted.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Auditing an account exposes private share metadata in the resulting report.

Mitigation: Obtain account access authorization and keep reports private; the tool creates report files with restricted permissions by default.

Risk: An untrusted local PikPak executable override could access the configured account.

Mitigation: Use only a trusted local CLI and verify any PIKPAK_BIN override before running the audit.

Risk: Unverified live CLI fields or unknown dates and visit counts can make share classifications incomplete.

Mitigation: Review uncertain entries manually and confirm any create or revoke action separately; never treat a zero-visit or unknown flag as automatic deletion approval.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/pipiguai87-alt/skills/pikpak-share-manager)
- [Share audit design and limitations](artifact/references/upstream-design.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [JSON share audit report or human-readable summary and manual management guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports list share metadata and review flags, not share links or passwords; incomplete audits fail rather than presenting a complete report.]

## Skill Version(s):

1.0.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
