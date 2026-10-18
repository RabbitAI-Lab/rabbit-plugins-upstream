## Description:

Audits PikPak shares for known expired, soon-to-expire, and zero-view items, then provides read-only reports and guidance for separately authorized share management.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pipiguai87-alt](https://clawhub.ai/user/pipiguai87-alt)

### License/Terms of Use:

MIT-0

## Use Case:

PikPak account holders and their authorized agents use this skill to review share-list metadata, identify shares needing attention, and plan manually approved changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The local PikPak CLI can access private share-list metadata.

Mitigation: Confirm account access is authorized, use a trusted CLI and shell environment, and keep generated reports private.

Risk: A report may be written to an unintended or existing path.

Mitigation: Review the destination before writing; overwrite an existing report only with explicit authorization.

Risk: Registration with the disclosed optional referral code or account-changing commands may have unintended effects.

Mitigation: Obtain explicit confirmation before registration or any share creation or revocation; the audit itself remains read-only.

## Reference(s):

- [PikPak Share Manager release](https://clawhub.ai/pipiguai87-alt/skills/pikpak-share-manager)
- [Share audit design and limitations](references/upstream-design.md)
- [rclone PikPak share request fields (design reference, not release provenance)](https://github.com/rclone/rclone/blob/d369079a1448c487d09d85bfe11382e16ea4e345/backend/pikpak/api/types.go#L485-L491)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Plain-text audit summary and optional JSON report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports list share metadata and flags; account changes require separate approval.]

## Skill Version(s):

1.0.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
