## Description:

Helps agents generate and check SHA-256 manifests for local directories to compare files before and after transfer.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT (code only); documentation all rights reserved

## Use Case:

Developers and other users can ask an agent to create and check local directory hash manifests when checking downloaded files or comparing files after transfer.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A check can pass despite extra files absent from the manifest.

Mitigation: Review the added-files list and compare the expected file inventory before accepting an integrity check.

Risk: Manifest generation writes to disk even though documentation suggests preview-first behavior.

Mitigation: Review the target directory and manifest path, and back up any existing manifest before generation.

## Reference(s):

- [ClawHub hash-check release](https://clawhub.ai/zhaoxinghua09-cell/skills/hash-check)
- [Publisher homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown or plain text with shell commands and verification results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The command-line utility optionally returns JSON and uses exit statuses for checks.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
