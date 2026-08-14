## Description:

Read an attached Markdown document, analyze and summarize it, then generate a minimalist image from the summary using the default image model.

This skill is ready for commercial/non-commercial use.

## Publisher:

[j3ffyang](https://clawhub.ai/user/j3ffyang)

### License/Terms of Use:

MIT-0

## Use Case:

External users and creators use this skill to turn an attached Markdown document into a concise summary and one minimalist whiteboard-style image for social banners, hero visuals, or simple tutorial graphics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Markdown contents or summaries may be used to generate an image and saved in the local Hermes cache.

Mitigation: Avoid using sensitive Markdown documents unless local image generation and caching fit the user's workflow.

Risk: The skill depends on a readable Markdown file and a valid aspect ratio before producing an image.

Mitigation: Confirm the source file is a valid .md document and provide a supported or explicit custom aspect ratio when prompted.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/j3ffyang/skills/260611-md2mini-img)
- [Publisher profile](https://clawhub.ai/user/j3ffyang)
- [Author link from clawdis metadata](https://github.com/j3ffyang)

## Skill Output:

**Output Type(s):** [text, markdown, image, guidance]

**Output Format:** [Markdown summary with a generated image object and local image path]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generates exactly one image; resolves aspect ratio and color scheme before generation.]

## Skill Version(s):

1.0.0 (source: release evidence and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
