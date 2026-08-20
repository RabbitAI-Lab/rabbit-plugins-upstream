## Description:

Organize workspace files by type, extension, and date for cleanup, downloads sorting, media organization, or archival preparation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[terrycarter1985](https://clawhub.ai/user/terrycarter1985)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, employees, and external users can use this skill to inspect a cluttered directory, preview file moves, and organize files into category folders for cleanup, backup, or upload preparation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bulk file moves can reorganize or displace files in the current directory, including files the user did not intend to move.

Mitigation: Run the dry-run preview first, execute only inside a directory intended for reorganization, and keep a backup or recovery plan for important files.

Risk: The skill text says hidden files are skipped, but the security summary says the execute step can include hidden files.

Mitigation: Do not run the execute step in a home folder, repository, or secrets-bearing directory unless that hidden-file mismatch is fixed or explicitly accepted.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/terrycarter1985/skills/my-content-organizer)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes a dry-run preview before file-moving commands.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
