## Description:

Finds potential duplicate files by size and hashes, reporting results by default and optionally deleting extra copies with --apply.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT (code only); documentation and theoretical text: All rights reserved

## Use Case:

People and agents managing file collections can identify likely duplicate files, review a cleanup report, and choose whether to remove extra copies.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional --apply mode can delete files without creating the promised backup.

Mitigation: Review the default report and back up important directories yourself before using --apply.

Risk: Hash matches are not confirmed by byte-for-byte comparison before deletion.

Mitigation: Confirm file contents independently before deleting, or use a duplicate finder that verifies byte-for-byte equality.

## Reference(s):

- [ClawHub dup-finder release](https://clawhub.ai/zhaoxinghua09-cell/skills/dup-finder)
- [Publisher homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Plain-text or JSON duplicate-file report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports duplicate groups and potential space savings; --apply also reports deletions.]

## Skill Version(s):

1.0.3 (source: server-resolved ClawHub release; bundled files show conflicting versions)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
