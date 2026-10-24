## Description:

Audits PikPak shares for expiry, near-expiry, and zero-visit indicators, producing a read-only report and guidance for separately authorized manual share management.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pipiguai87-alt](https://clawhub.ai/user/pipiguai87-alt)

### License/Terms of Use:

MIT-0

## Use Case:

PikPak account holders and administrators use the skill to identify shares with expired, near-expiry, or potentially zero-visit indicators in a private report. It does not change shares; any management action requires separate, explicit authorization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Audit reports contain private share metadata.

Mitigation: Write reports only to a user-authorized location and keep them private; overwrite an existing report only with explicit authorization.

Risk: An untrusted CLI override or execution environment could run an unintended executable.

Mitigation: Use a trusted PikPak CLI and trusted local environment; avoid untrusted CI, multi-tenant, or privileged services.

Risk: Live share-list field compatibility has not been verified, so findings may need confirmation.

Mitigation: Confirm audit results before relying on them, and separately authorize any share changes.

## Reference(s):

- [Upstream design and verification boundaries](artifact/references/upstream-design.md)
- [PikPak connected-app quota guidance](https://mypikpak.com/zh-CN/help-center/transfer_quota/connected_apps_quota)
- [PikPak WebDAV speed limits](https://mypikpak.com/zh-CN/help-center/connected_apps/webdav/speed_limit)
- [ClawHub skill release](https://clawhub.ai/pipiguai87-alt/skills/pikpak-share-manager)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Guidance]

**Output Format:** [JSON audit report with human-readable management guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports selected share metadata without passwords or share links; share changes are not automated and require separate authorization.]

## Skill Version(s):

1.0.9 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
