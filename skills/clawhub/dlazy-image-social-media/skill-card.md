## Description:

A social-media image design skill that helps agents plan platform-specific visuals, captions, safe areas, and iterative generation for Instagram, TikTok, YouTube, LinkedIn, Xiaohongshu, and related formats.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, creators, marketers, and developers use this skill to plan and generate social-media image assets and companion captions that match platform-specific aspect ratios, safe areas, visual styles, and engagement goals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks users to install and run a third-party CLI with incomplete containment.

Mitigation: Review the dLazy CLI source and exact package version before use, and prefer npx or another isolated environment over a global install.

Risk: The CLI stores a dLazy API key for authenticated use.

Mitigation: Use a narrowly scoped, revocable API key and rotate or revoke it when it is no longer needed.

Risk: Selected media files may be uploaded to dLazy's service for generation.

Mitigation: Provide only media files intended for upload and avoid sensitive or unnecessary local files.

Risk: Version documentation is inconsistent across the release evidence and artifact frontmatter.

Mitigation: Use the server release version for this card and confirm the dLazy CLI package version before installation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-image-social-media)
- [Publisher profile](https://clawhub.ai/user/dlazyai)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands]

**Output Format:** [Markdown with structured plans, inline shell commands, caption text, and generated media URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Separates in-image text from captions; may call the dLazy CLI to upload selected media and return hosted result URLs.]

## Skill Version(s):

1.3.15 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
