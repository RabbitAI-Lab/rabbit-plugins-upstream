## Description:

Creates a read-only report of file counts, known storage usage, and largest files in an authorized PikPak folder, with clear scan-completeness and unknown-size indicators.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pipiguai87-alt](https://clawhub.ai/user/pipiguai87-alt)

### License/Terms of Use:

MIT-0

## Use Case:

PikPak users and their agents use this skill to inspect an authorized folder, find large files, and assess known storage usage without deleting files or claiming to measure account quota.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reports can expose private file names and paths.

Mitigation: Authorize only the intended folder and keep generated reports in a private directory.

Risk: The report relies on the local PikPak CLI and its environment.

Mitigation: Run it only with a trusted PikPak CLI and trusted environment variables.

Risk: Unknown file sizes or incomplete scans can understate storage use.

Mitigation: Check completeness and unknown-size indicators; do not interpret scanned bytes as account quota.

## Reference(s):

- [Upstream design and limitations](references/upstream-design.md)
- [rclone lsjson documentation (design reference)](https://github.com/rclone/rclone/blob/d369079a1448c487d09d85bfe11382e16ea4e345/docs/content/commands/rclone_lsjson.md#L99-L118)

## Skill Output:

**Output Type(s):** [JSON reports, Text summaries]

**Output Format:** [JSON or plain text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes scan-completeness and unknown-size indicators; does not query account quota.]

## Skill Version(s):

1.0.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
