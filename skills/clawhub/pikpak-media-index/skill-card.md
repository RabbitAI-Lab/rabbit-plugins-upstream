## Description:

Creates Markdown or CSV indexes of PikPak video candidates, with filters for known duration and resolution and redacted source links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pipiguai87-alt](https://clawhub.ai/user/pipiguai87-alt)

### License/Terms of Use:

MIT-0

## Use Case:

PikPak account holders and media-library organizers use this skill to inventory video candidates and filter by known duration or resolution without guessing missing metadata.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Account listings and generated reports may reveal private media names, paths, or source identifiers.

Mitigation: Authorize account access explicitly, choose report destinations carefully, and limit access to saved reports.

Risk: A locally configured PikPak executable may run with access to account listings.

Mitigation: Keep PIKPAK_BIN pointed to a trusted executable under your control.

Risk: The disclosed referral code may reward the sharer if used for registration.

Mitigation: Review and choose whether to use the referral code before executing any registration command.

## Reference(s):

- [Upstream field design and limitations](references/upstream-design.md)
- [rclone PikPak media field definitions](https://github.com/rclone/rclone/blob/d369079a1448c487d09d85bfe11382e16ea4e345/backend/pikpak/api/types.go#L188-L280)

## Skill Output:

**Output Type(s):** [Markdown, CSV]

**Output Format:** [Markdown or CSV report file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Candidate metadata snapshot; unknown values remain unknown, and source links are redacted rather than anonymized.]

## Skill Version(s):

1.0.5 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
