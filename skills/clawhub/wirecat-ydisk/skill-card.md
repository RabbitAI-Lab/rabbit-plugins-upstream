## Description:

Use ydisk to search and read the owner's Yandex Disk files and to list, download, upload, move or share them. Use when a task needs a file or a fact from Yandex Disk (Яндекс Диск), or a change to files there.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wirecat](https://clawhub.ai/user/wirecat)

### License/Terms of Use:

MIT-0

## Use Case:

The account owner and an assistant acting for them can search and read Yandex Disk files to answer questions, check sync status, or carry out requested file changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: File deletion and trash-clearing actions can remove stored content.

Mitigation: Check the target and scope before deletion; use --dry-run for writes when unsure, and restore an item if it should be recovered.

Risk: Publishing a file creates a link anyone can open.

Mitigation: Publish only when public access is intended, and unpublish the file when that access should end.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wirecat/skills/wirecat-ydisk)
- [Yandex Disk API command reference](references/api.md)
- [Yandex Disk file and folder operations](references/api/api-disk-resources.md)
- [Yandex Disk trash operations](references/api/api-disk-trash-resources.md)
- [Yandex Disk public resources](references/api/api-disk-public-resources.md)

## Skill Output:

**Output Type(s):** [Files, Text, JSON, Shell commands, Guidance]

**Output Format:** [JSON command results, concise text or Markdown summaries, and file content in its available format]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Depending on the request, operations can read, create, modify, share, publish, delete, or restore Yandex Disk files.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
