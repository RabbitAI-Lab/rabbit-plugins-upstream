## Description:

Generates Chinese web-novel cover prompts and shell commands that call a configured image API to create covers with title and author text.

This skill is ready for commercial/non-commercial use.

## Publisher:

[9438190](https://clawhub.ai/user/9438190)

### License/Terms of Use:

MIT-0

## Use Case:

Authors, editors, and publishing-support agents use this skill to turn book metadata, platform style, and optional reference images into structured cover prompts and API commands for generating web-novel cover art.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cover prompts, book metadata, and optional reference images are sent to the configured image API.

Mitigation: Use only trusted API providers or proxies, and avoid sending sensitive or rights-restricted source material.

Risk: Changing GPT_IMAGE_BASE_URL or using remote reference-image URLs can route content through untrusted services.

Mitigation: Keep the trusted default API endpoint unless a trusted proxy is intentional, and prefer local or trusted HTTPS reference images.

Risk: Generated covers may contain text, layout, or style errors that are unsuitable for publication.

Mitigation: Review saved images and prompt copies before use, then iterate on composition, typography, color, or platform style as needed.

## Reference(s):

- [Cover Style Reference](references/cover-styles.md)
- [ClawHub Skill Page](https://clawhub.ai/9438190/skills/story-cover)
- [OpenClaw Metadata Source Link](https://github.com/worldwonderer/oh-story-claudecode)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, files]

**Output Format:** [Markdown guidance with bash command blocks and prompt text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save generated PNG covers and prompt or reference text files under BOOK_DIR.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
