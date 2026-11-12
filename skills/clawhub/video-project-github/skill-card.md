## Description:

Keeps a video or agent-built project organized in a private GitHub repository with versioned project files, separately stored media, and restore guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vargai](https://clawhub.ai/user/vargai)

### License/Terms of Use:

MIT-0

## Use Case:

Video creators and people using coding agents can use the skill to organize an ongoing project, keep project files versioned, preserve and restore media, and return to earlier versions using plain-language requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: File-path handling during project operations or media restore may affect unintended files.

Mitigation: Review the target paths and test restore in a disposable project copy; compare restored files with their recorded hashes.

Risk: Project material may be sent to model providers, and repository privacy settings may not cover every upload or use path.

Mitigation: Review what project material is shared and the provider's privacy settings before sending sensitive files or prompts.

Risk: A media restore may overwrite files at its destination.

Mitigation: Test restore in a separate copy and keep another backup of important media before restoring.

Risk: Unpinned downloads can change between runs or introduce unexpected content.

Mitigation: Pin tool versions where possible and verify restored media against its recorded hash.

## Reference(s):

- [Project layout guide](artifact/references/layout.md)
- [Media storage guidance](artifact/references/media-storage.md)
- [GitHub Releases documentation](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Project files, Guidance]

**Output Format:** [Markdown instructions, shell commands, and project files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Project files are versioned in GitHub; media files are stored separately and checked by hash when restored.]

## Skill Version(s):

1.0.4 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
