## Description:

Generates professional Chinese web-novel cover images from a book title, author name, target platform, and genre style using Codex ImageGen or a GPT-Image API fallback.

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT-0

## Use Case:

Authors, designers, and publishing workflows use this skill to collect cover requirements, select genre and platform styling, generate cover prompts, create cover images, and export platform-specific upload sizes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cover generation can consume image-generation quota or API credits.

Mitigation: Prefer the built-in ImageGen path when available, and confirm provider and credit use before using the API fallback.

Risk: API fallback may send prompts and optional reference images to the configured image provider.

Mitigation: Set GPT_IMAGE_API_KEY and GPT_IMAGE_BASE_URL only for trusted providers, and avoid private network or sensitive reference image URLs.

## Reference(s):

- [Cover styles reference](artifact/references/cover-styles.md)
- [ClawHub skill page](https://clawhub.ai/worldwonderer/skills/story-cover)
- [OpenClaw source metadata](https://github.com/zenstory-ai/oh-story-claudecode)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Files, Guidance]

**Output Format:** [Markdown guidance with prompt text, shell command blocks, and generated image files when image tools or APIs are available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create PNG cover files and companion prompt or reference text files under BOOK_DIR.]

## Skill Version(s):

1.1.6 (source: server release metadata; artifact frontmatter states 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
