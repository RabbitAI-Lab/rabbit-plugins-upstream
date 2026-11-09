## Description:

Helps agents organize project files, track approved changes, and manage backups for video or other projects in a private GitHub repository.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vargai](https://clawhub.ai/user/vargai)

### License/Terms of Use:

MIT

## Use Case:

People with ongoing video or code projects can use this skill to have an agent organize project files, record approved changes, and manage backup and restore workflows across computers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: File handling may expose or overwrite files outside the intended project, and privacy checks may be unreliable.

Mitigation: Keep an independent backup, verify .gitignore and repository access, and review collaborator-provided manifests before restoring or uploading. Wait for reliable path containment and fail-closed privacy checks before trusting valuable projects to this workflow.

Risk: Media edits may not be reliably preserved or undone.

Mitigation: Keep an independent backup and verify that media and edits restore correctly before relying on the workflow.

Risk: Sharing a repository grants access to its project history and media.

Mitigation: Limit repository access to intended collaborators and use additional model providers only when approved for the project material.

## Reference(s):

- [Project homepage](https://github.com/vargHQ/skills/tree/main/video-project-github)
- [ClawHub release page](https://clawhub.ai/vargai/skills/video-project-github)

## Skill Output:

**Output Type(s):** [Files, Markdown, Configuration instructions, Shell commands]

**Output Format:** [Project files and command guidance, including Markdown, JSONL manifests, and code or configuration files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Project-specific files, paths, media metadata, and command results.]

## Skill Version(s):

1.0.2 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
