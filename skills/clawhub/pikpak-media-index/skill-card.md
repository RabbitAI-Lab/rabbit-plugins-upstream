## Description:

Builds a Markdown or CSV index of PikPak video candidates with known duration, resolution, original codec, and redacted source metadata.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pipiguai87-alt](https://clawhub.ai/user/pipiguai87-alt)

### License/Terms of Use:

MIT-0

## Use Case:

PikPak users and their agents can catalog video candidates in an authorized account, filter by known resolution or duration, and review metadata without downloading media.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Listing an account exposes private PikPak file metadata to the agent.

Mitigation: Run the local PikPak CLI only with the account holder's authorization and limit the scan to an approved folder when appropriate.

Risk: Generated reports can disclose filenames, paths, sizes, durations, and partially redacted sources.

Mitigation: Treat reports as private and store or share them only in locations approved by the user.

Risk: The disclosed registration referral code may reward the publisher.

Mitigation: Review the referral code and ask the user to choose whether to use it before any registration command.

## Reference(s):

- [Upstream design and metadata limitations](references/upstream-design.md)
- [rclone PikPak media metadata schema (technical reference, not release provenance)](https://github.com/rclone/rclone/blob/d369079a1448c487d09d85bfe11382e16ea4e345/backend/pikpak/api/types.go#L188-L280)
- [FFmpeg ffprobe documentation (technical reference, not a dependency)](https://github.com/FFmpeg/FFmpeg/blob/3e6cd5e7603cb81b028b9c17530697b8986bf69a/doc/ffprobe.texi#L141-L172)

## Skill Output:

**Output Type(s):** [Markdown, CSV]

**Output Format:** [Markdown table or CSV report, written to a chosen file or stdout]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports include paths, sizes, known duration and resolution, original codec, and partially redacted sources; missing metadata remains unknown.]

## Skill Version(s):

1.0.6 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
