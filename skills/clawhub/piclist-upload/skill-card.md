## Description:

Uploads local images referenced in Markdown through the PicList HTTP Server and replaces local image paths with hosted URLs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cat-xierluo](https://clawhub.ai/user/cat-xierluo)

### License/Terms of Use:

MIT

## Use Case:

Developers, documentation maintainers, and content authors use this skill to publish local Markdown images to a configured image host through PicList and update Markdown files for cross-device access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Successful uploads delete local image files by default and may remove empty directories, which can cause unexpected local data loss.

Mitigation: Run --dry-run first and use --keep-local unless deletion is explicitly intended; process only files that are backed up or recoverable.

Risk: Untrusted Markdown can contain crafted local image paths that cause unintended local files to be uploaded.

Mitigation: Process only trusted Markdown files and review local image references before running in-place uploads.

Risk: PicList image-host credentials determine where files are published and what access the upload operation has.

Mitigation: Keep PicList bound to 127.0.0.1 and use least-privilege image-host tokens or credentials.

## Reference(s):

- [PicList Upload on ClawHub](https://clawhub.ai/cat-xierluo/skills/piclist-upload)
- [Publisher homepage](https://github.com/cat-xierluo/legal-skills)
- [PicList setup guide](references/setup.md)
- [PicList project](https://github.com/Kuingsmile/PicList)
- [PicList configuration documentation](https://piclist.cn/configure)
- [PicList FAQ](https://piclist.cn/faq)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Files, Guidance]

**Output Format:** [Markdown guidance with bash commands and script-generated text summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May update Markdown files in place and delete uploaded local image files unless --keep-local is used.]

## Skill Version(s):

1.3.0 (source: frontmatter, changelog, release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
