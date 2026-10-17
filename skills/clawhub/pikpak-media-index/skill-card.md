## Description:

Creates Markdown or CSV indexes of PikPak video candidates with metadata-based duration and resolution filters and redacted source links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pipiguai87-alt](https://clawhub.ai/user/pipiguai87-alt)

### License/Terms of Use:

MIT-0

## Use Case:

PikPak account holders can inventory video candidates in their media library and filter by known duration or resolution without downloading media. The report is a metadata snapshot, not a verification of media contents.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Listing an entire PikPak account and exporting a report may expose private filenames, paths, sizes, durations and source identifiers.

Mitigation: Authorize account access explicitly, scope scans to a specific folder when possible and keep report files private.

Risk: The disclosed referral code may benefit the publisher if used during registration.

Mitigation: Review the referral code before choosing whether to use a registration command; the indexing skill does not require registration.

## Reference(s):

- [Upstream field design and limitations](references/upstream-design.md)
- [rclone PikPak media field definitions](https://github.com/rclone/rclone/blob/d369079a1448c487d09d85bfe11382e16ea4e345/backend/pikpak/api/types.go#L188-L280)

## Skill Output:

**Output Type(s):** [Markdown, CSV, Shell commands]

**Output Format:** [Markdown or CSV metadata report, with text instructions for generating it]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may include private filenames, paths, sizes, durations and source identifiers; unknown metadata is not inferred.]

## Skill Version(s):

1.0.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
