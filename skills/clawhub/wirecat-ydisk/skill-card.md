## Description:

Use ydisk to search and read the owner's Yandex Disk files and to list, download, upload, move or share them.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wirecat](https://clawhub.ai/user/wirecat)

### License/Terms of Use:

MIT-0

## Use Case:

Users and agents working with a Yandex Disk account use this skill to find and read files, manage files and folders, share resources, and synchronize mirrored folders.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security assessment is benign with medium confidence, but scan coverage was partial; file deletion capabilities require attention to permissions.

Mitigation: Review the documented deletion operations and their required permissions before installing or using the skill.

Risk: Publishing a file creates a link that anyone can open.

Mitigation: Only publish files when the owner has requested sharing, and confirm the intended file before publishing.

## Reference(s):

- [Yandex Disk CLI API overview](artifact/references/api.md)
- [Disk resource operations](artifact/references/api/api-disk-resources.md)
- [Public resource operations](artifact/references/api/api-disk-public-resources.md)
- [Trash operations](artifact/references/api/api-disk-trash-resources.md)
- [ClawHub skill page](https://clawhub.ai/wirecat/skills/wirecat-ydisk)

## Skill Output:

**Output Type(s):** [JSON, Text, Files, Shell commands]

**Output Format:** [JSON command results and natural-language guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can make changes to files and folders on Yandex Disk when requested.]

## Skill Version(s):

1.0.2 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
