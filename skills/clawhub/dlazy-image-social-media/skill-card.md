## Description:

A structured skill for multi-platform social-media content creation across Instagram, TikTok, YouTube, LinkedIn, Xiaohongshu, and related formats.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and agents use this skill to plan and generate platform-specific social media images, thumbnails, carousel structures, in-image text, and captions. It guides requirements gathering, safe-area checks, visual prompt planning, and iterative delivery through the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security summary marks the release suspicious because it installs and runs an external npm CLI with a documented version mismatch.

Mitigation: Review the @dlazy/cli package and confirm the intended version before installation; prefer npx or a local install where possible.

Risk: The skill uses a cloud image-generation service and may upload prompts and local media files through the dLazy CLI.

Mitigation: Use a revocable dLazy API key and only provide local media files intended for upload to the service.

Risk: Global npm installation can broaden system impact if run with elevated privileges.

Mitigation: Avoid running npm as administrator or root; use a user-scoped or temporary execution path when practical.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-image-social-media)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, layout plans, prompt drafts, generated image URLs, and caption copy]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include platform specs, safe-area checks, in-image text, captions, iteration notes, and dLazy CLI command suggestions.]

## Skill Version(s):

1.3.18 (source: server release metadata; artifact frontmatter says 1.3.7)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
