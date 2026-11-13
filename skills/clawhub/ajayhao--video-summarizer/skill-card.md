## Description:

Converts Bilibili, YouTube, Xiaohongshu, and Douyin videos into structured summaries and archives them to Obsidian or Notion.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ajayhao](https://clawhub.ai/user/ajayhao)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to turn supported video URLs into knowledge-base-ready summaries with transcripts, screenshots, metadata, and storage in Obsidian or Notion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The server security summary reports a command-execution flaw in output-directory handling.

Mitigation: Install only after the output-directory issue is fixed, and do not allow untrusted text, links, or automation to choose the output directory.

Risk: Video transcripts, metadata, screenshots, cover images, or audio may be sent to configured third-party services.

Mitigation: Use non-sensitive videos, dedicated least-privilege API keys, and a dedicated OSS bucket with minimal permissions.

Risk: The server security verdict is suspicious pending review.

Mitigation: Review and scan the skill before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ajayhao/skills/video-summarizer)
- [Platform support details](references/platforms.md)
- [Security and privacy notes](references/security.md)
- [Troubleshooting](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, configuration]

**Output Format:** [Markdown summaries with YAML frontmatter, JSON analysis artifacts, transcript text, screenshot links, and optional Obsidian or Notion records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a video URL and configured service credentials; writes generated artifacts to a temporary or user-specified output directory.]

## Skill Version(s):

1.1.3 (source: server release metadata, changelog released 2026-06-23)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
