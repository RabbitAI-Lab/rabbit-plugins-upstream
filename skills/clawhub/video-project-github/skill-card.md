## Description:

Keep an AI video project, or any agent-built project, in a private GitHub repo, even when the person has never used git.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vargai](https://clawhub.ai/user/vargai)

### License/Terms of Use:

MIT-0

## Use Case:

Independent creators and developers use this skill to organize an AI video or other agent-built project, back up its source files and media in a private GitHub repository, and restore or undo changes without managing Git themselves.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A restore or overwrite operation could leave media missing or replace newer project work.

Mitigation: Review restore and overwrite safeguards before use, verify restored files against recorded hashes, and keep a separate copy of irreplaceable media.

Risk: Project files or prompts could be uploaded or shared more broadly than intended through repository uploads, invitations, or external judging workflows.

Mitigation: Confirm repository visibility and invitees, and review which project files or prompts are sent to any external judging service.

## Reference(s):

- [Skill source on GitHub](https://github.com/vargHQ/skills/tree/main/video-project-github)
- [How to keep a video project in GitHub](https://varg.ai/how-to/keep-a-video-project-in-github)
- [Where the media goes](references/media-storage.md)
- [Evidence and benchmarks](references/evidence.md)
- [Troubleshooting](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Files, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Project files and directories, Markdown documents, scripts, JSON or JSONL manifests, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create a private GitHub repository and upload project files and media to it.]

## Skill Version(s):

1.0.7 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
