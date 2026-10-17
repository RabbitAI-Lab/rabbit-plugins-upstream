## Description:

Finds duplicate files in a selected local directory by comparing file size, an initial-block hash, and a full-file SHA1 hash; reports matches by default and can delete extra copies on request.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can identify redundant files in downloads, photo collections, or project directories, review duplicate groups, and optionally remove extra copies after confirming the target directory.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using --apply automatically deletes extra local files, and the selected directory may contain files the user needs.

Mitigation: Select the directory deliberately, review report mode first, and back up important files before using --apply.

Risk: Declared permissions and documented command examples do not match the file access and arguments required by the tool.

Mitigation: Confirm the tool's actual arguments and filesystem access before cleanup; the publisher should correct its declarations and examples.

## Reference(s):

- [dup-finder release on ClawHub](https://clawhub.ai/zhaoxinghua09-cell/skills/dup-finder)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Terminal report or JSON summary of duplicate groups and file paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports duplicate groups and reclaimable bytes; JSON mode also reports removed count. Deletion occurs only when --apply is supplied.]

## Skill Version(s):

1.0.5 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
