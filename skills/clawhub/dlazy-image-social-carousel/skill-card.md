## Description:

Guides social-media carousel design through slide planning, user confirmation, and cover-first image generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and marketing teams use this skill to plan platform-specific social carousels, approve a cover design, and generate consistent follow-on slides with dLazy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local media are sent to dLazy-hosted services.

Mitigation: Send only assets and content you are comfortable sharing with dLazy.

Risk: Installing the CLI and storing a persistent API key expand local credential exposure.

Mitigation: Use the on-demand npx option and per-session DLAZY_API_KEY when appropriate; rotate or revoke keys when no longer needed.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-image-social-carousel)
- [dLazy CLI source (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Markdown, Image URLs, Guidance]

**Output Format:** [Markdown slide plans, status updates, and links to generated images]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes a direction-confirmation table and cover approval before remaining slides.]

## Skill Version(s):

1.3.25 (source: ClawHub release metadata; bundled frontmatter states 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
