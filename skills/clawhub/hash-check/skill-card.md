## Description:

Helps agents generate and check SHA-256 manifests for directories to compare files after downloads or transfers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT (.py code); all rights reserved (documentation and theory)

## Use Case:

Developers and other users can generate local SHA-256 file manifests and check files for changes after download or transfer.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generating a manifest writes or overwrites a file in the selected directory.

Mitigation: Run on a copy or back up the manifest and important files first.

Risk: Documentation lists differing versions and preview options that may not match the script.

Mitigation: Check the installed release and the script's --help output before running it; review licensing notes before reuse.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zhaoxinghua09-cell/skills/hash-check)
- [Publisher homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Text, JSON]

**Output Format:** [Markdown guidance and shell commands; local SHA-256 manifest and optional JSON check results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local directory scanning; no third-party runtime dependencies.]

## Skill Version(s):

1.0.3 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
