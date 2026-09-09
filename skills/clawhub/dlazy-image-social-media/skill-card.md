## Description:

A structured skill for planning and producing multi-platform social-media visuals, captions, and visual-generation commands optimized for Instagram, TikTok, YouTube, LinkedIn, Xiaohongshu, and similar platforms.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and agent users use this skill to plan platform-specific social-media imagery, generate concise in-image copy and captions, and run dLazy CLI image-generation commands when credentials are configured.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media files may be sent to dLazy cloud services for generation.

Mitigation: Avoid sensitive prompts or media unless the user has approved cloud processing for that content.

Risk: Using the skill requires storing or passing a dLazy API key.

Mitigation: Use scoped credentials where available, prefer environment variables for temporary use, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: The skill relies on a third-party npm CLI, and the evidence notes a version mismatch.

Mitigation: Prefer npx or a sandboxed environment, and confirm the exact @dlazy/cli version before trusting execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-image-social-media)
- [dLazy website](https://dlazy.com)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with platform specs, layout plans, caption copy, and inline shell commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return generated media URLs from the dLazy service after CLI execution.]

## Skill Version(s):

1.3.16 (source: server release evidence; artifact frontmatter reports 1.3.7)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
