## Description:

Produces a read-only report of PikPak folder sizes, file counts, and largest files while distinguishing incomplete scans and unknown file sizes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pipiguai87-alt](https://clawhub.ai/user/pipiguai87-alt)

### License/Terms of Use:

MIT-0

## Use Case:

PikPak users and their agents use this skill to identify space-consuming folders and files within an authorized folder without deleting content or mistaking scanned bytes for account quota.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reports can reveal private file names and paths.

Mitigation: Keep reports in a controlled private location and limit who can access them.

Risk: A live scan can traverse more data than the displayed tree suggests.

Mitigation: Confirm the intended folder and authorize live scanning separately; narrow the scope with the folder selection rather than display depth.

Risk: Incomplete scans or files with unknown sizes can understate storage use.

Mitigation: Check completeness and unknown-size indicators before interpreting totals or rankings; do not present scanned bytes as account quota.

Risk: An untrusted PikPak CLI path or environment could affect live scans.

Mitigation: Use a trusted CLI installation and controlled environment.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/pipiguai87-alt/skills/pikpak-storage-report)
- [Upstream design and limitations](references/upstream-design.md)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Plain text or JSON report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes scan completeness, unknown-size counts, folder totals, and largest-file rankings; does not query account quota.]

## Skill Version(s):

1.0.6 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
