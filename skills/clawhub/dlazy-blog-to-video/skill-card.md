## Description:

Helps turn blog posts and other documents into narrated videos with outlines, storyboards, voiceover, and assembly through dLazy's hosted file-to-video service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, educators, and business users can request narrated video versions of blog posts, presentations, PDFs, and other documents for social sharing, explainers, or training. The skill sends requests to dLazy's hosted file-to-video service and can upload attached files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The listing emphasizes blog-to-video, but the workflow invokes a broader file/document-to-video service.

Mitigation: Review the requested inputs and service scope before use; do not assume processing is limited to blog posts.

Risk: Prompts and attached local files may be sent to dLazy's hosted API and storage.

Mitigation: Only provide content approved for hosted processing; review file attachments before uploading.

Risk: Using the pinned npm CLI requires an API key stored locally or supplied to the process.

Mitigation: Review the pinned CLI before installing, safeguard the key, and rotate or revoke it if exposed.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-blog-to-video)
- [dLazy CLI source (linked in skill metadata; not verified skill provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands]

**Output Format:** [Plain text or Markdown with CLI commands and hosted service responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video creation is handled by dLazy's hosted service; attached files may be uploaded.]

## Skill Version(s):

1.0.26 (source: ClawHub release; artifact frontmatter says 1.0.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
