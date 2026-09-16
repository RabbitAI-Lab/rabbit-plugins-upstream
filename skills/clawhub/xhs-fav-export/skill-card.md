## Description:

Exports the current logged-in Xiaohongshu user's favorites tab into local Markdown files with source links, text, and image or video URLs, with offset/count batching for resumable exports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fatmind](https://clawhub.ai/user/fatmind)

### License/Terms of Use:

MIT-0

## Use Case:

External users and personal knowledge-management users use this skill to back up, search, and review their own Xiaohongshu favorite notes as local Markdown files. It is intended for authenticated browser sessions where the user is authorized to access the saved content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The exporter uses a logged-in Chrome session and creates a local archive of favorite-note text and media URLs that may be sensitive.

Mitigation: Run it only for accounts and content you are authorized to archive, store output in a controlled directory, and avoid sharing exported files without review.

Risk: The package includes an undisclosed obfuscated LLM client that can read local prompt or file contents and send them to an external endpoint outside the documented export workflow.

Mitigation: Do not install or use this version until the publisher removes the file or fully documents and deobfuscates it, and review network behavior before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/fatmind/skills/xhs-fav-export)
- [Artifact README](artifact/README.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, configuration]

**Output Format:** [Local Markdown files plus summary JSON and a final JSON status message]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces one Markdown file per exported note, a summary.json manifest, and optional result/data files when requested.]

## Skill Version(s):

1.0.4 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
