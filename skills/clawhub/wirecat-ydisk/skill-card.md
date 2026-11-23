## Description:

Use ydisk to search and read the owner's Yandex Disk files and to list, download, upload, move or share them. Use when a task needs a file or a fact from Yandex Disk (Яндекс Диск), or a change to files there.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wirecat](https://clawhub.ai/user/wirecat)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to find and read files in their Yandex Disk, manage and edit files, synchronize mirrored folders, and share resources. It helps an agent carry out these tasks through the ydisk command line while following the account owner's profile and approval prompts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan was partial, with two local references unresolved, so its benign verdict does not cover every referenced component.

Mitigation: Review the unresolved references and inspect the relevant skill material before installing or using it.

Risk: File deletion and trash clearing can remove data from the owner's Yandex Disk.

Mitigation: Check the target path and review the relevant deletion action carefully before running it.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/wirecat/skills/wirecat-ydisk)
- [Yandex Disk API overview](artifact/references/api.md)
- [Yandex Disk resource operations](artifact/references/api/api-disk-resources.md)
- [Yandex Disk public resources](artifact/references/api/api-disk-public-resources.md)
- [Yandex Disk trash resources](artifact/references/api/api-disk-trash-resources.md)

## Skill Output:

**Output Type(s):** [Shell commands, Text, JSON, Guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON CLI output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may read, write, share, move, or delete files in the owner's Yandex Disk.]

## Skill Version(s):

1.0.3 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
