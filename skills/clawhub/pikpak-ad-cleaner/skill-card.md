## Description:

Scans an authorized PikPak folder for suspected promotional files and produces a categorized, read-only report with optional cleanup commands for individually approved items.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pipiguai87-alt](https://clawhub.ai/user/pipiguai87-alt)

### License/Terms of Use:

MIT-0

## Use Case:

PikPak users and their agents can review suspected ads and junk in a specifically authorized cloud folder before deciding whether to clean up individual files. The skill does not delete files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Scanning exposes folder metadata through an existing PikPak CLI session.

Mitigation: Authorize the specific folder before allowing the agent to scan it.

Risk: Filename-based classifications can be mistaken for confirmed junk, and the recovery behavior of cleanup commands is unverified.

Mitigation: Review the report and approve each ID; do not run printed rm commands unless PikPak recovery behavior is independently confirmed.

Risk: Reports can reveal private file paths.

Mitigation: Keep reports in a controlled private location.

Risk: The disclosed referral code may reward its sharer.

Mitigation: Ignore or opt out of the referral code if you do not want to use it.

## Reference(s):

- [PikPak Ad Cleaner on ClawHub](https://clawhub.ai/pipiguai87-alt/skills/pikpak-ad-cleaner)
- [Upstream design and limitations](references/upstream-design.md)
- [rclone lsjson documentation](https://github.com/rclone/rclone/blob/d369079a1448c487d09d85bfe11382e16ea4e345/docs/content/commands/rclone_lsjson.md#L48-L50)
- [Czkawka core instructions](https://github.com/qarmin/czkawka/blob/eb8b91dbb4d25dff416202674ee0de84ee4b5e5c/instructions/Instruction_Core.md#L37-L47)

## Skill Output:

**Output Type(s):** [Files, Shell commands, Guidance]

**Output Format:** [JSON report and plain-text commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports high, review, and protected categories; only prints commands for individually approved IDs from an unchanged report and never executes them.]

## Skill Version(s):

1.0.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
