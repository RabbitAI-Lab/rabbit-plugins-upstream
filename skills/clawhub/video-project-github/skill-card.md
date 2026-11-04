## Description:

Keep an AI video project or other agent-built project backed up in a private GitHub repository, with versioned project files and separately stored media.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vargai](https://clawhub.ai/user/vargai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to organize, back up, restore, and version video projects through a private GitHub repository, including project files and associated media.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Modified media manifests may expose files outside the project, privacy checks can fail, and undo may lose unsaved media.

Mitigation: Restrict manifest paths to the project, stop uploads unless the repository is verified private, and preserve changed media before undo or restore. Keep an independent backup and verify .gitignore.

Risk: Project footage or collaborator access may be shared more broadly than intended.

Mitigation: Use approved model providers before sharing footage and review collaborator permissions carefully.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/vargai/skills/video-project-github)
- [Project layout guide](references/layout.md)
- [Media storage guide](references/media-storage.md)
- [Repeatable results guide](references/repeatable-results.md)
- [GitHub Releases documentation](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases)
- [Git LFS billing documentation](https://docs.github.com/en/billing/concepts/product-billing/git-lfs)

## Skill Output:

**Output Type(s):** [Files, Markdown, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Project files, Markdown instructions, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Project setup and backup workflow tailored to a video or agent-built project]

## Skill Version(s):

1.0.1 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
